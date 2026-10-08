# Configuration

CMSImport works with its default settings. To change them, add a `CmsImport` section to `appsettings.json`.

## Default settings

The example below shows all settings with their default values. Only add the settings you want to change.

```json title="appsettings.json"
{
  "CmsImport": {
    "MediaConfig": {
      "MediaImportLocation": "/wwwroot/",
      "AllowedFileExtensions": [
        ".doc", ".docx", ".pdf", ".ppt", ".pptx", ".rar", ".xls", ".xlsx", ".zip"
      ],
      "AllowedDomains": [],
      "MediaImportKeepFolderStructure": true,
      "MediaImportFileTypeAlias": "File",
      "MediaImportFolderTypeAlias": "Folder",
      "MediaImportImageTypeAlias": "Image"
    },
    "IgnoredPropertyAliasses": [
      "umbracoMemberFailedPasswordAttempts",
      "umbracoMemberLastLockoutDate",
      "umbracoMemberLastLogin",
      "umbracoMemberLastPasswordChangeDate",
      "umbracoMemberIsApproved"
    ],
    "LoginCredentialsMailConfig": {
      "FromAddress": "robot@cmsimport.com",
      "Subject": "Your account is ready",
      "ViewLocation": "loginmail.cshtml"
    },
    "ScheduledTaskMailConfig": {
      "FromAddress": "robot@cmsimport.com",
      "Subject": "Scheduled task executed",
      "ViewLocation": "scheduledtaskmail.cshtml"
    }
  }
}
```

## Media settings

These settings control [related media import](import/media.md).

### MediaImportLocation

The folder where CMSImport looks for the original media files, relative to the root of your site. The default
is `/wwwroot/`.

### MediaImportKeepFolderStructure

By default CMSImport keeps the folder structure of the original files in the Media section. Set this to `false`
to import all files into a single folder.

### AllowedFileExtensions

The file extensions that CMSImport imports from links in Rich Text Editor content. Links to other file types are
left as they are.

### AllowedDomains

Absolute URLs that start with one of these domains are imported too. The files must still be in the
[media import location](#mediaimportlocation).

### Media type aliases

By default CMSImport uses the standard **File**, **Folder** and **Image** Media Types. To use your own, set
their aliases in `MediaImportFileTypeAlias`, `MediaImportFolderTypeAlias` and `MediaImportImageTypeAlias`.

## IgnoredPropertyAliasses

Member properties that are not offered in the mapping step.

## Login credentials mail

CMSImport sends this email when **Send credentials via mail** is selected for a
[member import](import/wizard.md#member-import-options). You can set:

- `FromAddress` — the sender address.
- `Subject` — the email subject.
- `ViewLocation` — the Razor template for the email body. The default template is
  `umbraco/Data/cmsimport/mailtemplates/loginmail.cshtml`.

The template uses the `CMSImport.Core.Models.Mail.LoginMail` model:

| Property | Description |
|---|---|
| `LoginName` | The login name of the imported member. |
| `Password` | The password of the imported member, **not encrypted**. |
| `MemberName` | The full name of the imported member. |
| `Properties` | All properties of the member, as a `Dictionary<string, object>`. |

!!! note
    Emails are sent with the SMTP settings of your Umbraco site (`Umbraco:CMS:Global:Smtp`). See
    [Global settings](https://docs.umbraco.com/umbraco-cms/reference/configuration/globalsettings) in the
    Umbraco documentation.

## Scheduled task mail

CMSImport sends this email when a [scheduled import](scheduling.md) has finished. You can set the same
`FromAddress`, `Subject` and `ViewLocation` options. The default template is
`umbraco/Data/cmsimport/mailtemplates/scheduledtaskmail.cshtml`.

The template uses the `CMSImport.Core.Models.Mail.ScheduledTaskMail` model:

| Property | Description |
|---|---|
| `TaskName` | The name of the scheduled task. |
| `RecordCount` | The number of records in the data source. |
| `RecordsAdded` | The number of records added. |
| `RecordsUpdated` | The number of records updated. |
| `RecordsSkipped` | The number of records skipped. |
| `RecordsDeleted` | The number of records deleted. |
| `Errors` | The number of errors. |
| `ErrorMessages` | The error messages. |
