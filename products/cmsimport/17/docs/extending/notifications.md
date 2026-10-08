# Notifications

Use notifications to run your own code during an import. They work like any other
[Umbraco notification](https://docs.umbraco.com/umbraco-cms/fundamentals/code/subscribing-to-notifications).

| Notification | Published when |
|---|---|
| `BulkImportingNotification` | The complete import process starts. |
| `BulkImportedNotification` | The complete import process has finished. |
| `ImportingNotification` | A single import definition starts. |
| `ImportedNotification` | A single import definition has finished. |
| `RecordImportingNotification<T>` | A single record starts importing. You can cancel it. |
| `RecordImportedNotification<T>` | A single record has been imported. |
| `RecordSkippedNotification<T>` | A single record was skipped. |
| `MediaFileImportingNotification` | A media file starts importing. |
| `MediaFileImportedNotification` | A media file has been imported. |

`T` is the type of the imported item, for example `IContent` or `IMember`. Use `ProviderAlias` to check which
import provider published the notification, for example `ContentImportProvider`.

## Example: log every import step

This example writes every content import step to the Umbraco log.

First, register the notification handlers in a composer:

```csharp
using CMSImport.Core.Notifications;
using Umbraco.Cms.Core.Composing;
using Umbraco.Cms.Core.DependencyInjection;
using Umbraco.Cms.Core.Models;

public class ContentImportLogComposer : IComposer
{
    public void Compose(IUmbracoBuilder builder)
    {
        builder.AddNotificationHandler<BulkImportingNotification, ContentImportLogHandler>();
        builder.AddNotificationHandler<BulkImportedNotification, ContentImportLogHandler>();
        builder.AddNotificationHandler<ImportingNotification, ContentImportLogHandler>();
        builder.AddNotificationHandler<ImportedNotification, ContentImportLogHandler>();
        builder.AddNotificationHandler<RecordImportingNotification<IContent>, ContentImportLogHandler>();
        builder.AddNotificationHandler<RecordImportedNotification<IContent>, ContentImportLogHandler>();
        builder.AddNotificationHandler<RecordSkippedNotification<IContent>, ContentImportLogHandler>();
    }
}
```

Then create the handler:

```csharp
using CMSImport.Core.Notifications;
using Microsoft.Extensions.Logging;
using Umbraco.Cms.Core.Events;
using Umbraco.Cms.Core.Models;

public class ContentImportLogHandler :
    INotificationHandler<BulkImportingNotification>,
    INotificationHandler<BulkImportedNotification>,
    INotificationHandler<ImportingNotification>,
    INotificationHandler<ImportedNotification>,
    INotificationHandler<RecordImportingNotification<IContent>>,
    INotificationHandler<RecordImportedNotification<IContent>>,
    INotificationHandler<RecordSkippedNotification<IContent>>
{
    private const string ContentProvider = "ContentImportProvider";
    private readonly ILogger<ContentImportLogHandler> _logger;

    public ContentImportLogHandler(ILogger<ContentImportLogHandler> logger)
    {
        _logger = logger;
    }

    public void Handle(BulkImportingNotification notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("BulkImporting content {StateId}", notification.State.StateId);
    }

    public void Handle(BulkImportedNotification notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("BulkImported content {StateId}", notification.State.StateId);
    }

    public void Handle(ImportingNotification notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("Importing content {StateId}", notification.State.StateId);
    }

    public void Handle(ImportedNotification notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("Imported content {StateId}", notification.State.StateId);
    }

    public void Handle(RecordImportingNotification<IContent> notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("RecordImporting content {PrimaryKey}", notification.PrimaryKeyValue);
    }

    public void Handle(RecordImportedNotification<IContent> notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("RecordImported content {PrimaryKey}", notification.PrimaryKeyValue);
    }

    public void Handle(RecordSkippedNotification<IContent> notification)
    {
        if (notification.ProviderAlias == ContentProvider)
            _logger.LogInformation("RecordSkipped content {PrimaryKey}", notification.PrimaryKeyValue);
    }
}
```
