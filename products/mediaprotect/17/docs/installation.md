# Installation

This page explains how to install MediaProtect and add your license.

## Install the package

Install the Umbraco 17 version of MediaProtect from NuGet in your Umbraco project:

```bash
dotnet add package MediaProtect --version "17.*"
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
