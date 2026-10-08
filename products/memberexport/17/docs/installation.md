# Installation

This page explains how to install MemberExport and add your PRO license.

## Install the package

Install the Umbraco 17 version of MemberExport from NuGet in your Umbraco project:

```bash
dotnet add package MemberExport --version "17.*"
```

Run the site. MemberExport creates its database table and finishes the installation on the first request to the
website.

!!! note
    The database user of your site needs rights to create tables.

Go to the **Members** section. Under **Tools** you now find **Export members**. Refresh the page if you don't see
it yet.

## Add your license

Copy your license file, `member-export.lic`, to the `umbraco/Licenses` folder of your site. The `bin` folder works
too. MemberExport picks up the license when the site starts.
