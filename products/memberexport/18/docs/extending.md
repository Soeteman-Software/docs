# Extend MemberExport

By default MemberExport exports the value as it is stored in the database. Sometimes that's not what you want,
for example an ID instead of a readable text. A value parser converts the stored value before it is written to
the file.

## Built-in value parsers

MemberExport comes with value parsers for:

- Checkbox list
- Dropdown (single and multiple)
- Radio button list
- Multinode Treepicker
- Member groups

## Write a value parser

1. Reference the `MemberExport` package from your project.
2. Create a class that implements `IValueParser`.
3. Add one or more `[ValueParser]` attributes with the alias of the property editor it handles.

MemberExport finds your value parser automatically when the site starts. You don't need to register it.

### Example: export a toggle as Yes/No

A Toggle (true/false) property is stored as `1` or `0`. This value parser exports it as `Yes` or `No`.

```csharp
using MemberExport.Core.Models;
using MemberExport.Core.ValueParsers;

[ValueParser(PropertyEditorAlias = "Umbraco.TrueFalse")]
public class YesNoValueParser : IValueParser
{
    public object Parse(MemberField memberField, object value, FieldParserOptions fieldParserOptions)
    {
        return value?.ToString() switch
        {
            "1" => "Yes",
            "0" => "No",
            _ => value
        };
    }
}
```

`Parse` is called for every exported value of a property that uses one of the property editors in the
`[ValueParser]` attributes.

### Information about the field

The `memberField` parameter tells you which field is exported:

| Property | Description |
|---|---|
| `PropertyId` | The ID of the property. |
| `PropertyEditorAlias` | The alias of the property editor, for example `Umbraco.TrueFalse`. |
| `DatatypeNodeId` | The ID of the Data Type. |
| `Alias` | The alias of the property. |
| `Text` | The name of the property. |
| `Config` | The configuration of the Data Type. |
