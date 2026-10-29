# Configuration

MediaProtect works with its default settings. To change them, add a `MediaProtect` section to `appsettings.json`.

## Default settings

The example below shows all settings with their default values. Only add the settings you want to change.

```json title="appsettings.json"
{
  "MediaProtect": {
    "Enabled": true,
    "AllowAccessForUmbracoUsers": true,
    "EnableLogging": true,
    "LogPublicMedia": false,
    "CsvDelimiter": ",",
    "CsvStringIndicator": "\"",
    "DisableMediaprotectDialog": false,
    "DisableReturnUrl": true,
    "DefaultLoginNode": 0,
    "DefaultErrorNode": 0,
    "ExcludeRoles": []
  }
}
```

## Enabled

Set to `false` to turn MediaProtect off without uninstalling it. Protected files are then served to everyone.

## AllowAccessForUmbracoUsers

By default, users who are logged in to the Umbraco backoffice can open all protected files. Set to `false` to
check backoffice users the same way as visitors.

## Logging

| Setting | Default | Description |
|---|---|---|
| `EnableLogging` | `true` | Logs requests for protected files. See the [log viewer](dashboards.md#log-viewer). |
| `LogPublicMedia` | `false` | Also logs requests for files that are not protected. |
| `CsvDelimiter` | `,` | The delimiter used when you export the log to CSV. |
| `CsvStringIndicator` | `"` | The text qualifier used when you export the log to CSV. |

## DisableMediaprotectDialog

Set to `true` to hide the **Public Access** action on media. Use this when you only change protection from code
with the [Protection API](developers/library.md#protection-api).

## DisableReturnUrl

When a visitor is redirected to the login page, MediaProtect can add the URL of the requested file, for example
`?returnurl=%2fmedia%2f37%2fprotected_file.pdf`. Your login page can use it to send the member back to the file
after logging in.

By default this is turned off (`true`). Set it to `false` to add the return URL.

## DefaultLoginNode and DefaultErrorNode

The IDs of the pages that are selected by default as login page and error page when you
[protect media](protect-media.md). This saves you from picking them every time.

```json title="appsettings.json"
{
  "MediaProtect": {
    "DefaultLoginNode": 1048,
    "DefaultErrorNode": 1049
  }
}
```

## ExcludeRoles

Member groups that are not offered in the [group based protection](protect-media.md#group-based-protection)
list. The names are not case-sensitive.

```json title="appsettings.json"
{
  "MediaProtect": {
    "ExcludeRoles": [ "Internal" ]
  }
}
```
