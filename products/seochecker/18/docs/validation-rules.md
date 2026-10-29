# Validation rules

This page lists the checks SEOChecker runs.

## Content checks

These checks run on the content of the page.

| Check | Reported when |
|---|---|
| Broken links | A link points to a URL that can't be reached. |
| Broken media | A reference to a media item is broken or empty. |
| Missing link title | A link has no `title` attribute. |
| Missing image alt | An image has no `alt` attribute. Set [`ValidateAltAttributesOnTemplate`](configuration/appsettings.md#validationconfig) to also check images in the template. |
| Empty SEO title | The `<title>` is empty. |
| SEO title too long | The SEO title is longer than 65 characters. |
| Empty SEO description | The description meta tag is empty. |
| SEO description too short | The SEO description is shorter than [`MetaDescriptionMinLength`](configuration/appsettings.md#validationconfig) (default 50). |
| SEO description too long | The SEO description is longer than [`MetaDescriptionMaxLength`](configuration/appsettings.md#validationconfig) (default 160). |
| Empty H1 | The `<h1>` of the page is empty. |
| Test content | The page contains "Lorem ipsum" text. |
| Empty social tags | An `og:title`, `og:description`, `og:type`, `og:url`, `twitter:card`, `twitter:site`, `twitter:title` or `twitter:description` tag is empty. |
| Relative `og:url` | The `og:url` doesn't start with `http(s)://`. |

## Template checks

These checks run on the HTML that the template renders.

| Check | Reported when |
|---|---|
| Missing SEO title | The template has no `<title>` tag. |
| Multiple SEO titles | The page has more than one `<title>` tag. |
| Missing description | The template has no description meta tag. |
| Code in description or keywords | The description or keywords meta tag contains code instead of text. |
| Missing H1 | The template has no `<h1>` tag. |
| Missing social tags | An `og:title`, `og:description`, `og:type`, `og:url`, `twitter:card`, `twitter:site`, `twitter:title` or `twitter:description` tag is missing in the template. |
| Google Analytics | Google Analytics isn't (correctly) set up for the template. |
| Empty page | The template only renders empty text. |
| Inline CSS | The template contains a lot of inline CSS. |
| Inline JavaScript | The template contains a lot of inline JavaScript. |
| HTML comments | The page contains a lot of HTML comments. |
| Iframe | The template contains an iframe. |
| Broken stylesheet | A link to a CSS file is broken. |
| Broken script | A link to a JavaScript file is broken. |

## Focus keyword checks

The [SEO property](editors/seo-property.md) reports when the focus keyword is not specified, or is missing from
the SEO title, SEO description, URL, page title (`<h1>`) or body text.

## Configuration checks

These checks run on the configuration of the website. They appear under
[configuration errors](issues.md#configuration-errors).

| Check | Type | Reported when |
|---|---|---|
| Canonical hostname | Canonical issue | The site can be reached with and without `www.`. |
| Lowercase URLs | Canonical issue | A page can be reached with uppercase and lowercase characters. |
| Trailing slash | Canonical issue | A page can be reached with and without a trailing slash. |
| Hostname configuration | Hosting issue | The site isn't set up for the `www.` or the non-`www.` hostname. |
| robots.txt missing | Search engine issue | There is no `robots.txt`. |
| robots.txt blocks all | Search engine issue | `robots.txt` blocks all search engines from the whole site. |
| robots.txt blocks Google | Search engine issue | `robots.txt` blocks Google from the whole site. |
| Robots `nofollow` on home page | Search engine issue | The robots meta tag of the home page contains `nofollow`. |
| Not found page missing | General issue | No [not found page](configuration/domain-settings.md#not-found-page) is set. |
| Old content | General issue | The newest content on the site is more than one month old. |
| SEO Data Type missing | General issue | A Document Type doesn't have the SEO Checker property. |
| No Document Types configured | General issue | No [Document Type settings](configuration/document-types.md) are set. |
