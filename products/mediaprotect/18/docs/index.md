# MediaProtect

MediaProtect lets you protect media in Umbraco the same way you protect content.

Once you protect a media item or folder, its files can only be opened by members who have access. Visitors who
aren't logged in are redirected to the login page. Members without access are redirected to the error page.

## Features

- **Protect media** for specific members or member groups, with a login page and an error page, just like
  Umbraco's public access for content. See [Protect media](protect-media.md).
- **Protected media are flagged** in the Media section tree.
- **Request log** of who opened which file, with search, CSV export and clear. See [Dashboards](dashboards.md).
- **Protection index** that you can rebuild from a dashboard.
- **Developer API** to check and change protection from code, and notifications to hook into requests. See
  [Library](developers/library.md).

MediaProtect uses the standard Umbraco member services. You can use your existing login pages, or plug in your
own authentication.

## Where to start

1. [Install MediaProtect](installation.md) and add your license.
2. [Protect your first media folder](protect-media.md).
3. Fine-tune the defaults in [Configuration](configuration.md).
