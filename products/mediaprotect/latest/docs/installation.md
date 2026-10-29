# Installation

This page explains how to install MediaProtect and add your license.

## Install the package

!!! note
    This version of MediaProtect is for Umbraco 19, which runs on .NET 11. On Umbraco 18 or 17, pick that
    version in the version selector at the top of the page.

Install MediaProtect from NuGet in your Umbraco project:

```bash
dotnet add package MediaProtect
```

Run the site. MediaProtect creates its database tables and finishes the installation on the first request to the
website.

!!! note
    The database user of your site needs rights to create tables.

## Add your license

Copy your license file to the `umbraco/Licenses` folder of your site. MediaProtect picks it up when the site
starts.

!!! info "Trial mode"
    Without a license, MediaProtect runs in trial mode. Protection only works on `localhost`, and the backoffice
    shows a license warning.
