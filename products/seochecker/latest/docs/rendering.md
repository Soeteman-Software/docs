# Render meta tags

SEOChecker renders the `<title>`, meta, canonical, `hreflang` and social tags for your pages. You only need this
when you use the [SEO property](editors/seo-property.md).

## Use the tag helper

This is the recommended way.

1. Add the SEOChecker tag helpers to `Views/_ViewImports.cshtml`:

    ```cshtml title="Views/_ViewImports.cshtml"
    @addTagHelper *, SEOChecker.Library
    ```

2. Add the tag helper to the `<head>` of your layout:

    ```cshtml
    <head>
        <seochecker-metadata />
    </head>
    ```

The tag helper renders all tags for the current page.

## Render tags from the property value

You can also read the SEO Checker property of the page as a `MetaData` object and render the tags yourself. In
the examples below the property alias is `seoChecker`.

```cshtml
@{
    var meta = Model.Value<SEOChecker.Library.Models.MetaData>("seoChecker");
}
```

| Property | Renders |
|---|---|
| `meta.AllTags` | All tags below, plus `hreflang` links and social tags when they apply. |
| `meta.SearchEngineTags` | The title, description, keywords, robots and canonical tags. |
| `meta.SocialTags` | The Open Graph and X (Twitter) tags. |
| `meta.Title` | The SEO title, with the [title template](configuration/document-types.md#title-template) applied. |
| `meta.Description` | The SEO description. |
| `meta.Keywords` | The keywords. Only set when the Data Type uses keywords. |
| `meta.Robots` | The robots value, based on the [robots settings](configuration/document-types.md#robots-settings). |
| `meta.CanonicalUrl` | The canonical URL. |

For example, to render all tags:

```cshtml
@meta.AllTags
```

Or to render tags one by one:

```cshtml
<title>@meta.Title</title>
<meta name="description" content="@meta.Description" />
<meta name="robots" content="@meta.Robots" />
<link rel="canonical" href="@meta.CanonicalUrl" />
```

## Special properties

Add a property with one of these aliases to a Document Type to change how SEOChecker handles a page.

| Alias | Type | Description |
|---|---|---|
| `seoCanonicalUrl` | Content Picker | The page to use as the canonical URL. |
| `seoXmlSiteMapHide` | Toggle | When on, the page is left out of the XML sitemap. |
| `seoIncludeRootInXmlSitemap` | Toggle | On a root node, such as a data folder: when on, the node is included in every sitemap. |
| `seoExcludeValidation` | Toggle | When on, the page is skipped by **Validate Pages**. The SEO property still validates the page. |
| `seoForceHTTPS` | Toggle | When on, the XML sitemap uses the HTTPS URL of the page. |
