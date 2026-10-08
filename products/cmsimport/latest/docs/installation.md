# Installation

This page explains how to install CMSImport, add extra data sources and activate your PRO license.

## Install the package

Install CMSImport from NuGet in your Umbraco project:

```bash
dotnet add package CMSImport
```

Run the site and log in to the backoffice. You now have an **Import** section.

!!! tip
    Don't see the **Import** section? Refresh the page, or log out and back in. Also check that your user group
    has access to the section.

## Add extra data sources

BlogML, JSON, RSS and WordPress data sources ship as separate packages. Install only the ones you need:

```bash
dotnet add package CMSImport.DataProviders.BlogML
dotnet add package CMSImport.DataProviders.JSON
dotnet add package CMSImport.DataProviders.RSS
dotnet add package CMSImport.DataProviders.Wordpress
```

## Activate your PRO license

You can add your `cmsimport.lic` license file in either of these ways:

- **Upload it in the backoffice.** Go to the **Import** section and upload the file on the dashboard.
  CMSImport stores it as `umbraco/Licenses/cmsimport.lic`.
- **Copy it to disk.** Place `cmsimport.lic` in the `umbraco/Licenses` folder or the `bin` folder of your site.

## Manual database installation

CMSImport creates its database tables when the site starts. If the site's database user can't create tables,
install them by hand:

1. Download the [SQL script](https://soetemansoftware.nl/downloads/cmsimportv4dto.sql.txt).
2. Rename the file to `cmsimport.sql`.
3. Run the script against the Umbraco database, for example from SQL Server Management Studio.
