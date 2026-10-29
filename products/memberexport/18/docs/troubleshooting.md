# Troubleshooting

Solutions for common problems with MemberExport.

## I don't see Export members in the Members section

- Refresh the page.
- Check that the `MemberExport` package is installed and that the site has handled at least one request since.
- Check that the database user can create tables. See [Installation](installation.md).

## My CSV file looks wrong in Excel

Set the CSV options before you export. For Excel, use `;` as **Field Seperator** and `"` as **Text Indicator**.
Or export to an Excel file directly (PRO).

## My export stops at 200 members

The free edition exports up to 200 members. Add a PRO license to export all members. See
[Add your license](installation.md#add-your-license).

## I get an "Invalid license" error

Check that `member-export.lic` is in the `umbraco/Licenses` or `bin` folder, and that the license is for the
(sub)domain you run the site on, or is an enterprise license. Contact
[support@soetemansoftware.nl](mailto:support@soetemansoftware.nl) for help.

## I have another question

Email us at [support@soetemansoftware.nl](mailto:support@soetemansoftware.nl). We're happy to help.
