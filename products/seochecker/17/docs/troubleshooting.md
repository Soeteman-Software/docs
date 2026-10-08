# Troubleshooting

Solutions for common problems with SEOChecker.

## I don't see the SEO Checker section

- Check that the `SEOChecker` package is installed and that the site has handled at least one request since.
- Check that your user group has access to the section. See [Give users access](installation.md#give-users-access).

## Validation reports errors on the page

Check that the page and its template render without errors. Set
[`LogDebugHTML`](configuration/appsettings.md#logdebughtml) to `true` to see the HTML SEOChecker validates, and
check the Umbraco log.

## Some pages are not validated

Only published pages that have a template are validated. Pages with the `seoExcludeValidation`
[special property](rendering.md#special-properties) turned on are skipped too.

## I don't receive email notifications

- Check the SMTP settings of your site (`Umbraco:CMS:Global:Smtp` in `appsettings.json`).
- Check that the email address of the user is correct.
- Check the Umbraco log for SMTP errors.

## I found a bug

Check the [release notes](https://soetemansoftware.nl/seo-checker/release-notes) for a newer version. If the bug
is still there, email [support@soetemansoftware.nl](mailto:support@soetemansoftware.nl) so we can fix it.

## I have another question

Email us at [support@soetemansoftware.nl](mailto:support@soetemansoftware.nl). We're happy to help.
