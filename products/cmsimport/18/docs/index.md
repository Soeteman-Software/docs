# CMSImport

CMSImport helps you import content, members and dictionary items from any data source into Umbraco.

## Supported data sources

Out of the box, CMSImport imports from:

| Data source | Package |
|---|---|
| CSV | `CMSImport` |
| Excel file | `CMSImport` |
| SQL Server | `CMSImport` |
| XML | `CMSImport` |
| BlogML | `CMSImport.DataProviders.BlogML` |
| JSON file | `CMSImport.DataProviders.JSON` |
| RSS feed | `CMSImport.DataProviders.RSS` |
| WordPress | `CMSImport.DataProviders.Wordpress` |

The data sources in the add-on packages need an extra NuGet package. See [Installation](installation.md).
You can also [build your own data source](extending/data-providers.md).

## What CMSImport PRO adds

With CMSImport PRO you can:

- **Save an import** as an import definition and run it again later. Existing records are updated, new records
  are added.
- **Schedule imports** to run at a set day and time. See [Schedule imports](scheduling.md).
- **Import complete content structures**, such as a product catalog with categories and products, or blog posts
  with comments. See [Structured content import](import/structured-content.md).
- **Import related media.** References in content or member data are updated automatically. See
  [Related media import](import/media.md).

!!! note
    This documentation describes the PRO features. The free edition has limited functionality.

## Where to start

1. [Install CMSImport](installation.md).
2. Run your first import with the [import wizard](import/wizard.md).
3. Fine-tune the defaults in [Configuration](configuration.md).

## Third-party software

CMSImport uses the following open source libraries:

- [HTML Agility Pack](https://html-agility-pack.net/) — MS-PL license.
- [LumenWorks Framework IO (Fast CSV Reader)](http://www.codeproject.com/Articles/9258/A-Fast-CSV-Reader) — MIT
  license.
- [ClosedXML](https://github.com/ClosedXML/ClosedXML) for reading Excel files — MIT license.
