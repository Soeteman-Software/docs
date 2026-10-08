# Advanced setting providers

An advanced setting provider works like a [field provider](field-providers.md), but adds settings that the user
fills in during the mapping step. The settings open from the settings icon next to a mapping.

An advanced setting provider has two classes:

- an **options class** that defines the settings UI, and
- the **provider** that converts the value, using those settings.

The example on this page converts a date/time string from the data source to a `DateTime`, using a format the
user enters.

## Options class

Implement `IProviderOptions`:

- `Alias` links the options to the provider. Use the same alias as in the provider attribute.
- `RenderField` lets you hide fields. `fieldAlias` is the property name in lowercase.
- Decorate each property with a [UI field attribute](ui-fields.md). Here `[DateFormatField]` renders a date
  format field.

```csharp
using System.Collections.Generic;
using CMSImport.Core.Attributes.EditorFields;
using CMSImport.Core.Models.ProviderModels;
using CMSImport.Core.Providers;

public class AdvancedDateSettingsOptions : IProviderOptions
{
    /// <summary>
    /// The format used to parse the date/time.
    /// </summary>
    [DateFormatField(Name = "Date time format",
        Description = "Specify the format the import uses to parse the date/time")]
    public string DateTimeFormat { get; set; }

    public string Alias => "AdvancedDateSettingsProvider";

    public bool RenderField(string fieldAlias) => true;

    public List<AliasValue> PropertyValues { get; set; }
}
```

## Provider

Derive from `AdvancedSettingProvider` and add the `[AdvancedSettingsProvider]` attribute with the alias and the
supported property editor alias(es).

| Method | Description |
|---|---|
| `Parse` | Converts the value during the import. `value` is the source value, `options` holds the user's settings (cast it to your options class) and `importOptions` holds the import provider options. |
| `Validate` | Validates the settings and returns a list of error messages. |
| `GetAdvancedSettingProviderOptions` | Returns a new instance of your options class. |

```csharp
using System;
using System.Collections.Generic;
using System.Globalization;
using CMSImport.Core.Extensions;
using CMSImport.Core.Providers;
using CMSImport.Core.Providers.AdvancedSettingProviders;
using CMSImport.Core.Providers.ImportProviders;
using Umbraco.Cms.Core.Models;

[AdvancedSettingsProvider(Alias = "AdvancedDateSettingsProvider",
    SupportedPropertyEditorAliasses = "Umbraco.DateTime")]
public class AdvancedDateSettingsProvider : AdvancedSettingProvider
{
    public override object Parse(object value, IContentBase importedItem, IProviderOptions options,
        ImportOptions importOptions)
    {
        var s = value.AsString();
        var dateOptions = options as AdvancedDateSettingsOptions;
        if (!string.IsNullOrWhiteSpace(dateOptions?.DateTimeFormat) && !string.IsNullOrWhiteSpace(s))
        {
            if (DateTime.TryParseExact(s, dateOptions.DateTimeFormat,
                CultureInfo.CurrentUICulture, DateTimeStyles.None, out var dt))
            {
                value = dt;
            }
        }
        return value;
    }

    public override IEnumerable<string> Validate(IProviderOptions options)
    {
        var result = new List<string>();
        var dateOptions = options as AdvancedDateSettingsOptions;
        if (string.IsNullOrWhiteSpace(dateOptions?.DateTimeFormat))
        {
            result.Add("A date time format is required");
        }
        return result;
    }

    public override IProviderOptions GetAdvancedSettingProviderOptions(ImportPropertyInfo importPropertyInfo)
        => new AdvancedDateSettingsOptions();
}
```
