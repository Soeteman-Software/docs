# Schedule imports

You can run a saved import automatically at a set day and time.

## Create a schedule

1. In the **Import definitions** tree, open the actions menu of a saved content or member import.
2. Select **Schedule Import**.

    ![Actions menu of an import definition with Schedule Import](assets/images/scheduling-1.png)

3. Enter a **Scheduled task name**.
4. In **Run task as**, choose the user that is set as the creator of the imported items.
5. Optionally, enter one or more email addresses in **Notify emailaddress** to get a notification when the
   import finishes. Separate multiple addresses with a comma.
6. Under **Run import**, choose how often the import runs:
    - **Daily** — on the selected **Days**, at the time set in **Run at**
    - **Every (x) minutes** — at a fixed interval
7. Click **Save**.

![Schedule settings with task name, user, notification email, frequency, days and time](assets/images/scheduling-2.png)

The import now runs at the selected times. When an email address is set, you get an email after each run. You
can change this email; see [Scheduled task mail](configuration.md#scheduled-task-mail).

## Scheduled task log

To see when a scheduled import ran, open the actions menu of the schedule and view its log.

The time it ran can differ a little from the scheduled time, for example when the site was down at the scheduled
time. When the site comes back up, the scheduler runs any task it missed.
