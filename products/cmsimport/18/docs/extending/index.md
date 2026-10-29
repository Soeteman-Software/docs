# Extend CMSImport

You don't need to write code to use CMSImport. When you do want to change how data is read or converted, CMSImport
has several extension points.

| Extension point | Use it to |
|---|---|
| [Field provider](field-providers.md) | Convert a source value to the value a property editor expects, without UI. |
| [Advanced setting provider](advanced-setting-providers.md) | Convert a source value, with settings the user fills in during mapping. |
| [Data provider](data-providers.md) | Read data from a new kind of data source. |
| [UI fields](ui-fields.md) | Build the settings UI for your providers. |
| [Notifications](notifications.md) | Run your own code before or after an import or a single record. |

## Set up a project

1. Create a class library, or add the code to your Umbraco web project.
2. Install the CMSImport core package:

    ```bash
    dotnet add package CMSImport.Core
    ```

3. Make sure the host Umbraco site references your project.

CMSImport finds your providers automatically when the site starts. You don't need to register them.

## Dependency injection

Inject the services you need through the constructor, the same as in any other Umbraco extension. See
[Dependency injection](https://docs.umbraco.com/umbraco-cms/reference/using-ioc) in the Umbraco documentation.
