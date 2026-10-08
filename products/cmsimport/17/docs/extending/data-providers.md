# Data providers

A data provider reads data from a data source and returns it as an `IDataReader`. CMSImport uses that reader to
import the records.

A data provider has two classes:

- the **provider**, which reads the data, and
- an **options class**, which defines the UI where the user selects the data source.

The example on this page reads an RSS feed. It is the same code as the `CMSImport.DataProviders.RSS` package.

## Provider

Derive from `DataProvider` and add the `[DataProvider]` attribute.

| Member | Description |
|---|---|
| `GetData` | Returns an `IDataReader` for the options the user entered. `onlyFirstRow` is `true` when CMSImport only needs the column names. |
| `Validate` | Validates the options and returns a `ValidationResult` with error messages. |
| `GetDataProviderOptions` | Returns a new instance of your options class. |
| `SupportRecursiveImports` | Optional. Return `false` when the data source can't be used for [recursive imports](../import/wizard.md#recursive-options). |

```csharp
using System;
using System.Data;
using CMSImport.Core.Helpers;
using CMSImport.Core.Models.Validation;
using CMSImport.Core.Providers;
using CMSImport.Core.Providers.DataProviders;

[DataProvider(Alias = "Rss File", Name = "RSS File", ContentType = "Content",
    Title = "RSS Demo", Intro = "Demo provider for RSS feeds")]
public class RssFeedDataProvider : DataProvider
{
    private readonly IFileOrUrlModelHelper _fileOrUrlModelHelper;

    public RssFeedDataProvider(IFileOrUrlModelHelper fileOrUrlModelHelper)
    {
        _fileOrUrlModelHelper = fileOrUrlModelHelper;
    }

    public override IDataReader GetData(IProviderOptions dataProviderOptions, bool onlyFirstRow = false)
    {
        var options = dataProviderOptions as RssFeedDataProviderOptions;
        var xml = _fileOrUrlModelHelper.GetDataFromFileOrUrl(options.Datasource);
        return XmlDataHelper.XmlToDataReader(xml, false, "//item");
    }

    public override ValidationResult Validate(IProviderOptions providerOptions)
    {
        var result = new ValidationResult();
        try
        {
            using var dataReader = GetData(providerOptions);
            if (!dataReader.Read())
            {
                result.ErrorMessages.Add("No data in file");
            }
        }
        catch (Exception ex)
        {
            result.ErrorMessages.Add($"Error validating the RSS feed: {ex.Message}");
        }
        return result;
    }

    public override IProviderOptions GetDataProviderOptions() => new RssFeedDataProviderOptions();

    public override bool SupportRecursiveImports => false;
}
```

## Options class

Implement `IProviderOptions`:

- `Alias` links the options to the provider. Use the same alias as in the `[DataProvider]` attribute.
- `RenderField` lets you hide fields. `fieldAlias` is the property name in lowercase.
- Decorate each property with a [UI field attribute](ui-fields.md). Here `[DatasourcePicker]` lets the user
  upload a file or enter a URL, and `[FileModelValidation]` checks that they did.

```csharp
using System.Collections.Generic;
using CMSImport.Common.ValueConverters;
using CMSImport.Core.Attributes.EditorFields;
using CMSImport.Core.Attributes.ValidationAttributes;
using CMSImport.Core.Models.ProviderModels;
using CMSImport.Core.Providers;

public class RssFeedDataProviderOptions : IProviderOptions
{
    [DatasourcePicker(Name = "Select RSS file", FieldValueConverter = typeof(FileOrUrlPickerValueConverter))]
    [FileModelValidation]
    public FileOrUrlPickerModel Datasource { get; set; } = new();

    public string Alias => "Rss File";

    public bool RenderField(string fieldAlias) => true;

    public List<AliasValue> PropertyValues { get; set; } = [];
}
```

!!! note
    `FileOrUrlPickerValueConverter` lives in `CMSImport.Common`. Install the `CMSImport.Common` package (or the
    full `CMSImport` package) when you use it.
