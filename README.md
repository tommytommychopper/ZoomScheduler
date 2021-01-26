# Zoom Scheduler

This program will automatically open Zoom meeting at sheduled time.<br>
The reason I build this is that it was annoying to find and click the correct zoom link to open every times during my school semester.

## How it works

\*Cron is used to schedule the execution of files.

\*Only available on Linux🐧 / Mac 
If you are using Windows, "Task Scheduler" helps you to do this type of work.

Commands

```cron
crontab -l  : display your current setting
crontab -e  : editing
crontab -r : remove
```

Example -> [cron.text](cron.txt)<br>
[crontab guru](https://crontab.guru/) helps you to create schedule expressions easily.
