# Troubleshooting

Solutions for common problems with CMSImport.

## I don't see the Import section

- Refresh the page, or log out of the backoffice and log in again.
- Check that your user group has access to the **Import** section.
- Check that the `CMSImport` package is installed. See [Installation](installation.md).
- When the database user can't create tables, follow
  [Manual database installation](installation.md#manual-database-installation).

## I don't see my column names when importing a CSV file

Make sure the first row of the CSV file contains the column names.

## I get strange column names when importing a CSV file

Check the CSV options in the data source step. For example, set the delimiter to `;` and the text qualifier to
`"`. Also save the CSV file as UTF-8.

## Members don't receive the credentials email

- Check the SMTP settings of your site in `appsettings.json`. See
  [Login credentials mail](configuration.md#login-credentials-mail).
- Check the Umbraco log for SMTP errors.

## I get an "Invalid license" error

- Check that `cmsimport.lic` is in the `umbraco/Licenses` or `bin` folder. See
  [Activate your PRO license](installation.md#activate-your-pro-license).
- Check that you bought the right license for this site.
- Still stuck? Contact [support@soetemansoftware.nl](mailto:support@soetemansoftware.nl).
