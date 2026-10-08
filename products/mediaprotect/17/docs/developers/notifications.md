# Notifications

Use notifications to run your own code when a file is requested or when protection changes. They work like any
other [Umbraco notification](https://docs.umbraco.com/umbraco-cms/fundamentals/code/subscribing-to-notifications):
create a class that implements `INotificationHandler<T>` and register it in a composer.

All notifications are in the `MediaProtect.Library.Notifications` namespace.

| Notification | Published when | Properties |
|---|---|---|
| `FileRequestingNotification` | A file request starts. | `Path` |
| `FileRequestedNotification` | A file request has been handled. | `MediaId`, `Url`, `Protected`, `UserName`, `IPAddress` |
| `MediaItemProtectedNotification` | A media item is protected, or its protection is changed, in the backoffice. | `MediaId`, `Path` |
| `MediaItemProtectionRemovedNotification` | Protection is removed from a media item in the backoffice. | `MediaId` |

## Example: log all notifications

First, register the handler in a composer:

```csharp
using MediaProtect.Library.Notifications;
using Umbraco.Cms.Core.Composing;
using Umbraco.Cms.Core.DependencyInjection;

public class MediaProtectLogComposer : IComposer
{
    public void Compose(IUmbracoBuilder builder)
    {
        builder.AddNotificationHandler<FileRequestingNotification, MediaProtectLogHandler>();
        builder.AddNotificationHandler<FileRequestedNotification, MediaProtectLogHandler>();
        builder.AddNotificationHandler<MediaItemProtectedNotification, MediaProtectLogHandler>();
        builder.AddNotificationHandler<MediaItemProtectionRemovedNotification, MediaProtectLogHandler>();
    }
}
```

Then create the handler:

```csharp
using MediaProtect.Library.Notifications;
using Microsoft.Extensions.Logging;
using Umbraco.Cms.Core.Events;

public class MediaProtectLogHandler :
    INotificationHandler<FileRequestingNotification>,
    INotificationHandler<FileRequestedNotification>,
    INotificationHandler<MediaItemProtectedNotification>,
    INotificationHandler<MediaItemProtectionRemovedNotification>
{
    private readonly ILogger<MediaProtectLogHandler> _logger;

    public MediaProtectLogHandler(ILogger<MediaProtectLogHandler> logger)
    {
        _logger = logger;
    }

    public void Handle(FileRequestingNotification notification)
        => _logger.LogInformation("File requesting {Path}", notification.Path);

    public void Handle(FileRequestedNotification notification)
        => _logger.LogInformation("File requested {Url} by {UserName}", notification.Url, notification.UserName);

    public void Handle(MediaItemProtectedNotification notification)
        => _logger.LogInformation("Media item protected {MediaId}", notification.MediaId);

    public void Handle(MediaItemProtectionRemovedNotification notification)
        => _logger.LogInformation("Media item protection removed {MediaId}", notification.MediaId);
}
```
