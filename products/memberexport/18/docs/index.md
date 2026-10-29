# MemberExport

MemberExport exports Umbraco members to a CSV or Excel file, fast. It can export thousands of members in a few
seconds.

## Features

- Choose exactly which member fields to export: built-in fields and your own properties.
- Filter and sort members before you export them.
- Export to CSV or Excel.
- Save an export as a definition and run it again later.
- Write your own [value parsers](extending.md) to change how values are exported.

## Free and PRO edition

| | Free | PRO |
|---|---|---|
| Export to CSV | :material-check: | :material-check: |
| Export to Excel | | :material-check: |
| Number of members | 200 | Unlimited |
| Save export definitions | | :material-check: |

Without a license file, MemberExport runs as the free edition. See [Add your license](installation.md#add-your-license).

!!! note
    MemberExport reads members directly from the database. It only works with the default Umbraco member
    provider.

## Where to start

1. [Install MemberExport](installation.md).
2. [Export your members](export.md).
