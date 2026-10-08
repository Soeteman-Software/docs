# Library

MediaProtect has a small library to check, from your views or code, whether media is protected and who has
access. You can also change protection from code.

## MediaProtectHelper

### Use it in a view

Inject the helper in `Views/_ViewImports.cshtml`:

```cshtml title="Views/_ViewImports.cshtml"
@inject MediaProtect.Library.MediaProtectHelper MediaProtectHelper
```

You can now use `MediaProtectHelper` in all your views:

```cshtml
@if (MediaProtectHelper.IsProtected(1068) && !MediaProtectHelper.HasAccess(1068))
{
    <p>Log in to download this file.</p>
}
```

In your own classes, inject `MediaProtect.Library.MediaProtectHelper` through the constructor.

### Methods

Most methods accept either the ID of a media item or the path of a file, for example `/media/eyey/test.pdf`.

| Method | Returns |
|---|---|
| `IsProtected(int nodeId)` / `IsProtected(string fileName)` | `true` when the media item or file is protected. |
| `HasAccess(int nodeId)` / `HasAccess(string fileName)` | `true` when the current member has access. |
| `AllowedGroups(int nodeId)` / `AllowedGroups(string fileName)` | The member groups that have access. |
| `AllowedMembers(int nodeId)` / `AllowedMembers(string fileName)` | The usernames of the members that have access. |
| `IsProtectedByUserName(int nodeId)` | `true` when the media item is protected for specific members (not member groups). |
| `GetProtectedNodesForUser(string userName)` | The IDs of the media items protected for this member. |
| `GetProtectedNodesForRole(string roleName)` | The IDs of the media items protected for this member group. |
| `GetCurrentUserName()` | The username of the current member. |

## Protection API

Use the `MediaProtect.Library.Protection` class to change protection from code. Create it with the
`IMediaAccessInfoService`, which you inject through the constructor:

```csharp
using MediaProtect.Common.Services.Access;
using MediaProtect.Library;

public class DownloadsProtector
{
    private readonly Protection _protection;

    public DownloadsProtector(IMediaAccessInfoService mediaAccessInfoService)
    {
        _protection = new Protection(mediaAccessInfoService);
    }

    public void ProtectForMembers(int mediaId, int loginPageId, int errorPageId)
    {
        // Group based protection for the "Members" member group
        _protection.ProtectMedia(false, mediaId, loginPageId, errorPageId);
        _protection.AddMembershipRoleToMedia(mediaId, "Members");
    }
}
```

| Method | Description |
|---|---|
| `ProtectMedia(bool userNameProtection, int nodeId, int loginNode, int noRightsNode)` | Protects a media item. Pass `true` for specific members protection, `false` for group based protection, plus the IDs of the login page and error page. |
| `AddMembershipUserToMedia(int nodeId, string userName)` | Gives a member access. |
| `AddMembershipRoleToMedia(int nodeId, string roleName)` | Gives a member group access. |
| `RemoveMembershipUserFromMedia(int nodeId, string userName)` | Removes access for a member. |
| `RemoveMembershipRoleFromMedia(int nodeId, string roleName)` | Removes access for a member group. |
| `RemoveProtection(int nodeId)` | Removes protection from a media item. |
| `IsProtectedByUserName(int nodeId)` | `true` when the media item is protected for specific members. |
