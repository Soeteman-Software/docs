# SEOChecker

SEOChecker finds common SEO issues on your Umbraco website, such as missing meta tags and broken links, and
helps you fix them before you publish a page.

## Features

- **Page validation.** Every published page with a template can be validated against the checks in Google's
  [Search Engine Optimization Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
  See [Validation rules](validation-rules.md) for the full list.
- **Snippet preview.** See how a page appears in Google search results while you edit it, with feedback on
  how you use your focus keyword. See [SEO property](editors/seo-property.md).
- **Social preview.** See how a page appears when it is shared on Facebook, Instagram, LinkedIn and X.
  See [Social preview](editors/social.md).
- **Broken inbound links.** SEOChecker logs requests for pages that don't exist and redirects visitors
  automatically when a page was renamed or moved. See [Redirect manager](redirects.md).
- **Metadata, robots.txt and XML sitemap.** SEOChecker can generate meta data from existing content, and
  creates `robots.txt` and `sitemap.xml` for you.
- **Canonical URLs.** The built-in URL rewrite module sends every request to one canonical URL.
- **Scheduled validation and notifications.** Validate parts of your site on a schedule and get email
  notifications about issues.

## Where to start

1. [Install SEOChecker](installation.md) and add your license.
2. Add the [SEO property](editors/seo-property.md) to your Document Types.
3. [Render the meta tags](rendering.md) in your templates.
4. [Validate your pages](validation.md).

## Third-party software

SEOChecker uses the following open source software:

- [HTML Agility Pack](https://html-agility-pack.net/) — MS-PL license.
- [LumenWorks Framework IO (Fast CSV Reader)](http://www.codeproject.com/Articles/9258/A-Fast-CSV-Reader) — MIT
  license.
- [ClosedXML](https://github.com/ClosedXML/ClosedXML) for reading Excel files — MIT license.
- The Instagram icon from [Bootstrap Icons](https://github.com/twbs/icons) — MIT license.
