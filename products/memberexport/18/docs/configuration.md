# Configuration

MemberExport works with its default settings. To change them, add a `MemberExport` section to
`appsettings.json`.

```json title="appsettings.json"
{
  "MemberExport": {
    "ExcludePropertiesConfiguration": [
      "__memberCreatedBy",
      "__memberType",
      "__memberGroups",
      "umbracoMemberLastLockoutDate",
      "umbracoMemberLastPasswordChangeDate"
    ],
    "LogDebugInfo": false
  }
}
```

## ExcludePropertiesConfiguration

The aliases of properties that are not offered under **Export properties**.

!!! warning "Your list replaces the default list"
    When you set `ExcludePropertiesConfiguration`, it replaces the default list completely. Copy the defaults
    below that you want to keep.

By default these properties are excluded:

- `__memberCreatedBy`, `__memberType`, `__memberGroups`
- The technical Umbraco member properties, such as `umbracoMemberFailedPasswordAttempts`,
  `umbracoMemberApproved`, `umbracoMemberLockedOut`, `umbracoMemberLastLockoutDate`, `umbracoMemberLastLogin`,
  `umbracoMemberLastPasswordChangeDate`, `umbracoMemberPasswordRetrievalQuestion` and
  `umbracoMemberPasswordRetrievalAnswer`.

### Built-in fields

Besides your own properties, you can exclude the built-in fields. Their aliases start with `__member`.

| Alias | Field |
|---|---|
| `__memberId` | The ID of the member. |
| `__memberName` | The name of the member. |
| `__memberLogin` | The login name of the member. |
| `__memberEmail` | The email address of the member. |
| `__memberPassword` | The password as stored in the database (hashed). |
| `__memberCreated` | The date the member was created. |
| `__memberCreatedBy` | The user who created the member. Excluded by default. |
| `__memberType` | The member type. Excluded by default. |
| `__memberGroups` | A comma-separated list of the member's groups. Excluded by default. |

## LogDebugInfo

Set to `true` to write the SQL statement MemberExport runs to the Umbraco log. Use this when you troubleshoot an
export.

!!! note
    The statement is logged at `Debug` level. Make sure your Serilog minimum level includes `Debug`, see
    [Logging](https://docs.umbraco.com/umbraco-cms/fundamentals/code/debugging/logging) in the Umbraco
    documentation.
