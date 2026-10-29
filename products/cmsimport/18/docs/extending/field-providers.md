# Field providers

A field provider converts a value from the data source to the value a property editor expects. It has no user
interface.

To create one:

1. Implement the `IFieldProvider` interface.
2. Add one or more `[FieldProvider]` attributes with the alias of the property editor it handles.

CMSImport only calls your provider for properties that use that property editor.

## Example: member picker

This field provider turns an email address from the data source into a reference to the matching member, for
the `Umbraco.MemberPicker` property editor.

The `IMemberService` is injected through the constructor. `Parse` looks up the member by email address and
returns its UDI.

```csharp
using CMSImport.Core.Extensions;
using CMSImport.Core.Helpers;
using CMSImport.Core.Providers.FieldProviders;
using CMSImport.Core.Providers.ImportProviders;
using Umbraco.Cms.Core.Models;
using Umbraco.Cms.Core.Services;

[FieldProvider(PropertyEditorAlias = "Umbraco.MemberPicker")]
public class MemberPickerFieldProvider : IFieldProvider
{
    private readonly IMemberService _memberService;

    public MemberPickerFieldProvider(IMemberService memberService)
    {
        _memberService = memberService;
    }

    public object Parse(object value, IContentBase importedItem, ImportPropertyInfo property,
        FieldProviderOptions fieldProviderOptions)
    {
        var emailAddress = value.AsString();
        if (!string.IsNullOrWhiteSpace(emailAddress))
        {
            var member = _memberService.GetByEmail(emailAddress);
            if (member != null)
            {
                value = UdiHelper.ParseUdi(member.Key, "member");
            }
        }
        return value;
    }
}
```

| Parameter | Description |
|---|---|
| `value` | The value from the data source. |
| `importedItem` | The content item or member being imported. |
| `property` | Information about the property being mapped. |
| `fieldProviderOptions` | Extra options for the conversion. |
