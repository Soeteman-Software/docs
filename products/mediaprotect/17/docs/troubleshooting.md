# Troubleshooting

Solutions for common problems with MediaProtect.

## A protected file is still visible on the website

- Check that MediaProtect is running. Browse to `/app_plugins/mediaprotect/mediaprotect.txt` on your site. It
  should show **True**.
- Check that you aren't logged in to the backoffice in the same browser. Backoffice users can open protected
  files by default; see [`AllowAccessForUmbracoUsers`](configuration.md#allowaccessforumbracousers).
- Without a license, protection only works on `localhost`. See [Add your license](installation.md#add-your-license).

## I get an "Invalid license" error

Check that the license file is in the `umbraco/Licenses` folder, and that the license is for the (sub)domain
you run the site on, or is an enterprise license. Contact
[support@soetemansoftware.nl](mailto:support@soetemansoftware.nl) for help.

## How do I create a login form for my login page?

Use the **Login** and **Login Status** partial view snippets that come with Umbraco. In the **Settings** section,
create a partial view from a snippet and pick one of them.

## I don't see the Public Access action on media

You need access to the **Members** section. Ask an administrator to add the **Members** section to your user
group.

## I have another question

Email us at [support@soetemansoftware.nl](mailto:support@soetemansoftware.nl). We're happy to help.
