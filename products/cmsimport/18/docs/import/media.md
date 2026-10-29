# Related media import

CMSImport imports media that your content or members refer to. This is not a separate import: it happens while
you import content or members.

When CMSImport finds a relative path to a file, it creates a media item for it. For an upload field it stores
the file in the media folder instead. When the path points to a folder, CMSImport imports the complete folder and
assigns the folder, if the property editor allows that.

!!! warning "Copy the original media files first"
    Copy the original media folder into the media import location of your site before you run the import. By
    default this is `wwwroot`. You can change it with
    [`MediaImportLocation`](../configuration.md#mediaimportlocation).

In the example below, the `img` folder of the original site, with two images, is copied to the import location.

![File explorer showing the img folder with two images copied into the site](../assets/images/media-1.png)

Use the settings icon next to the media mapping to set where the media is stored in Umbraco.

![Advanced settings of a media mapping with the media location](../assets/images/media-2.png)

## Rich Text Editor

When you map to a Rich Text Editor, set the import options as shown below. For each image in the content,
CMSImport creates a media item and updates the image source to point to it.

![Advanced settings for a Rich Text Editor mapping](../assets/images/media-3.png)

Which file links are imported is controlled by
[`AllowedFileExtensions`](../configuration.md#allowedfileextensions) and
[`AllowedDomains`](../configuration.md#alloweddomains).

## Media Picker

When you map to a Media Picker, CMSImport creates a media item and stores a reference to it. Select **Show error
when file is missing on disk** to get an error when the data source refers to a file that isn't there.

![Advanced settings for a Media Picker mapping](../assets/images/media-4.png)

## Upload field and Image Cropper

When a file is mapped to an upload field or Image Cropper, CMSImport stores the file in the Umbraco media folder
and updates the reference in the property.

## Supported property editors

Related media import works for:

- Upload field
- Media Picker (single and multiple)
- Multinode Treepicker (media only)
- Image Cropper
- Rich Text Editor
