# Extend SEOChecker

You can add your own URL rewrite rules to the [URL rewrite module](configuration/appsettings.md#urlrewrite).

## URL rewrite provider

A URL rewrite provider changes the URL of a request. When the URL changes, SEOChecker redirects the visitor to
the new URL. This way all variants of a URL end up at one canonical URL.

To create one:

1. Reference the `SEOChecker.Core` package from your project.
2. Create a class that derives from `UrlRewriteProvider`.
3. Override `RewriteUrl` and change the `UrlBuilder` that is passed in.

SEOChecker finds your provider automatically when the site starts. Override `Prio` to change the order in which
providers run. The default is `100`.

### Example: always use HTTPS

```csharp
using System;
using SEOChecker.Core.Providers.UrlRewriteProviders;

/// <summary>
/// Redirects every HTTP request to HTTPS.
/// </summary>
public class HttpsRedirect : UrlRewriteProvider
{
    public override void RewriteUrl(UrlBuilder builder, UrlRewriteConfiguration config)
    {
        if (builder.Scheme.Equals("http", StringComparison.InvariantCultureIgnoreCase))
        {
            builder.Scheme = "https";
        }
    }
}
```
