# Optional: Sunday weekly reminder (launchd)

## What this can and cannot do
A scheduled job CANNOT run the newsletter — the research, verification, writing, and
Beehiiv steps need a live Claude session, which a background job can't summon. What a
schedule CAN do is **remind you** to kick off the run. That's the honest scope.

## Recommended setup: a Sunday 8am macOS notification + auto-open this chat workflow

Create ~/Library/LaunchAgents/com.dad.weekly.plist with:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.dad.weekly</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/osascript</string>
    <string>-e</string>
    <string>display notification "Time to build this week's D·A·D issue. Open Claude and send: build issue N" with title "Distilled AI Digest" sound name "Glass"</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key><integer>0</integer>
    <key>Hour</key><integer>8</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
</dict>
</plist>
```

Load it once:
```bash
launchctl load ~/Library/LaunchAgents/com.dad.weekly.plist
```
(Weekday 0 = Sunday. Unload with `launchctl unload ...` to stop.)

## The actual weekly trigger
When the reminder fires, open Claude in this project and send:
**"build issue N"** (e.g. "build issue 20").
Claude runs Message-1 (research -> 10 stories + 3 titles), you approve, and the rest
runs to a deployed site + Beehiiv draft.

## Optional convenience script
scripts/prep-issue.sh <N> "<DATE_RANGE>" pre-creates a working copy of the template
at issues/issue-N.html so it's staged and ready for Claude to fill — handy but not
required (Claude can create it directly).
