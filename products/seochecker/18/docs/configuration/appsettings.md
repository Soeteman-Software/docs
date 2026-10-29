# appsettings.json

Site-wide SEOChecker settings live in the `SEOChecker` section of `appsettings.json`. Only add the settings you
want to change.

## Example

The example below shows the most used settings with their default values.

```json title="appsettings.json"
{
  "SEOChecker": {
    "CacheTimeOutInMinutes": 60,
    "UmbracoApplicationUrl": "",
    "ForceHttps": false,
    "Triggers": {
      "TriggerOnPublish": true
    },
    "UrlRewrite": {
      "EnableUrlRewriting": true,
      "ForcewwwUrls": "Ignore",
      "UseTrailingslash": "Ignore"
    },
    "RedirectConfig": {
      "Enabled": true,
      "EnableUrlHistoryTracking": true,
      "EnableRedirectStats": false,
      "StoreDomain": false,
      "StoreQueryString": false,
      "ForwardQuerystring": false,
      "RedirectWhenNodeExists": false
    },
    "XmlSiteMap": {
      "Enabled": true,
      "ExcludeUmbracoNaviHide": true
    },
    "RobotsTxt": {
      "Enabled": true
    },
    "SocialSettings": {
      "FaceBookEnabled": false,
      "InstagramEnabled": false,
      "LinkedInEnabled": false,
      "TwitterEnabled": false
    },
    "ValidationConfig": {
      "ValidateAltAttributesOnTemplate": false,
      "MetaDescriptionMinLength": 50,
      "MetaDescriptionMaxLength": 160
    },
    "PurgeSettings": {
      "Enabled": true,
      "DaysToKeepBrokenLinks": 7,
      "MaxBrokenLinksToPurge": 50
    }
  }
}
```

## UrlRewrite

The URL rewrite module redirects all variants of a URL to one canonical URL.

| Setting | Default | Description |
|---|---|---|
| `EnableUrlRewriting` | `true` | Turns the URL rewrite module on or off. |
| `ForcewwwUrls` | `Ignore` | `True` always uses the `www.` prefix, `False` never uses it, `Ignore` leaves it as requested. |
| `UseTrailingslash` | `Ignore` | `True` always adds a trailing slash, `False` always removes it, `Ignore` leaves it as requested. |

These requests are redirected to the canonical URL:

| Situation | Requested URL | Redirected to |
|---|---|---|
| Site uses the `www.` prefix | `http://mysite.com/` | `http://www.mysite.com/` |
| Site doesn't use the `www.` prefix | `http://www.mysite.com/` | `http://mysite.com/` |
| Site doesn't use a trailing slash | `http://mysite.com/contact/` | `http://mysite.com/contact` |
| Request for the home page node | `http://mysite.com/home/` | `http://mysite.com/` |
| URL contains uppercase characters | `http://mysite.com/CONTACT/` | `http://mysite.com/contact/` |

!!! warning
    Keep URL rewriting on, unless you already handle URL rewriting another way, for example with IIS URL Rewrite.

To add your own rewrite rules, see [Extend SEOChecker](../extending.md).

## RedirectConfig

| Setting | Default | Description |
|---|---|---|
| `Enabled` | `true` | Turns the redirect module on or off. |
| `EnableUrlHistoryTracking` | `true` | Creates a redirect automatically when the URL of a page changes. |
| `EnableRedirectStats` | `false` | Keeps track of how often and when each redirect is used. |
| `StoreDomain` | `false` | Stores the domain of not found URLs, so you can redirect the same path on different domains to different pages. |
| `StoreQueryString` | `false` | Stores the query string of not found URLs, so you can redirect `page.php?id=4` and `page.php?id=5` to different pages. |
| `ForwardQuerystring` | `false` | Passes the query string on to the page you redirect to. |
| `RedirectWhenNodeExists` | `false` | Always redirects to the configured page, even when the original page still exists. |

## XmlSiteMap

| Setting | Default | Description |
|---|---|---|
| `Enabled` | `true` | Serves an XML sitemap at `/sitemap.xml`. |
| `ExcludeUmbracoNaviHide` | `true` | Leaves out pages where `umbracoNaviHide` is `true`. |

On a multilingual site there is a sitemap per language. The sitemap index is at `/sitemapindex.xml`.

Set sitemap options per Document Type in the [Document Type settings](document-types.md#xml-sitemap-settings),
or per page with the [special properties](../rendering.md#special-properties).

## RobotsTxt

| Setting | Default | Description |
|---|---|---|
| `Enabled` | `true` | Serves a dynamic `robots.txt`. |

When the XML sitemap is on, the location of the sitemap is added to `robots.txt`. The default content is:

```text
# SEO Checker for Umbraco
Sitemap: {HTTP_SCHEME}://{HTTP_HOST}/{SITEMAP_FILENAME}
User-Agent: *
Disallow: /bin/
Disallow: /umbraco/
```

The placeholders are replaced with the scheme and domain of the request, and with `sitemap.xml` or
`sitemapindex.xml`. You can change the content per site in the [domain settings](domain-settings.md#robotstxt).
When your site already has a `robots.txt` file, SEOChecker picks it up automatically.

## SocialSettings

| Setting | Default | Description |
|---|---|---|
| `FaceBookEnabled` | `false` | Renders Open Graph tags and `fb:app_id`. |
| `InstagramEnabled` | `false` | Renders Open Graph tags. |
| `LinkedInEnabled` | `false` | Renders Open Graph tags. |
| `TwitterEnabled` | `false` | Renders `twitter:*` tags. |

The `og:*` tags are rendered when at least one of Facebook, Instagram or LinkedIn is on.

## ValidationConfig

| Setting | Default | Description |
|---|---|---|
| `ValidateAltAttributesOnTemplate` | `false` | Checks `alt` attributes of images in the full HTML of the page, not only in rich text content. |
| `MetaDescriptionMinLength` | `50` | Minimum length of the meta description. |
| `MetaDescriptionMaxLength` | `160` | Maximum length of the meta description. |

## Triggers

| Setting | Default | Description |
|---|---|---|
| `TriggerOnPublish` | `true` | Adds a page to the validation queue when it is published. |

## PurgeSettings

SEOChecker removes broken inbound links that haven't been fixed after a number of days. Purging runs every hour.

| Setting | Default | Description |
|---|---|---|
| `Enabled` | `true` | Turns purging on or off. |
| `DaysToKeepBrokenLinks` | `7` | Number of days to keep a broken link. |
| `MaxBrokenLinksToPurge` | `50` | Maximum number of broken links removed per run. Keep this number low. |

## Other settings

### CacheTimeOutInMinutes

How long items are cached, in minutes. The default is `60`.

### DisableCaching

Set to `true` to turn caching off. Only use this when you troubleshoot.

### DisableValidationQueueModule

Set to `true` to stop validating pages. Only use this when you troubleshoot.

### ShowDomainNameInDomainSettings

Set to `true` to show the domain of each root node in the [domain settings](domain-settings.md).

### LogDebugHTML

Set to `true` to save the HTML that SEOChecker validates to `umbraco/Data/temp/seochecker/debug/published`.
Use this when you troubleshoot validation results.

### ForceHttps

Set to `true` to always use HTTPS, for example when the site runs behind a proxy.

### UmbracoApplicationUrl

The scheme and domain SEOChecker uses instead of the ones from the current request, for example
`https://www.mysite.com`. Use this in a load-balanced setup or behind a proxy.

### ReservedUrls

A comma-separated list of relative paths that the redirect module ignores, for example `/clientapi/,/mediafiles`.

### AuthenticatedValidation

To validate protected pages, set `AuthenticatedValidation` to `true` and enter the username and password in
`AuthenticatedValidationUser` and `AuthenticatedValidationPassword`.

### UserAgentFilters and UrlFilters

Lists of regular expressions. Requests whose user agent matches `UserAgentFilters`, or whose URL matches
`UrlFilters`, are treated as coming from a bot. SEOChecker comes with a list of common bots and vulnerability
scanners.
