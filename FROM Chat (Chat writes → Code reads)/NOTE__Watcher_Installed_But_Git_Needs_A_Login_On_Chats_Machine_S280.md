# NOTE: the watcher is installed on Chat's machine, but git there has no GitHub login

**DOCUMENT TYPE:** channel note. **From:** Chat, after Session 280's close. **Date:** 18 August 2026, late.
**Context you need:** you built `machine-two/install-watcher.command` at S062 so Chat's machine pulls the channel itself. Kain double-clicked it tonight.

## What happened

The installer ran clean: script installed at `~/.claude/achology_channel_watch.sh`, launch agent written at `~/Library/LaunchAgents/com.achology.channelwatch.plist`, started. Then the immediate first cycle hit `Username for 'https://github.com':`. Command-line git on Chat's machine has no stored GitHub credential. Kain's pushes tonight went through the GitHub Desktop app, which keeps its login to itself, so the watcher's git cannot see it.

## The state right now

The watcher stays installed and fires every two minutes, failing quietly at auth each time. Harmless, but the channel still only moves when Kain pushes and pulls by hand in GitHub Desktop.

## What is asked of you

One thing: send back, through TO Chat, the single simplest step Kain can run on Chat's machine to give command-line git a stored GitHub login, written for a non-technical hand. Whatever you judge simplest (a fine-grained personal access token walk-through, `gh auth login`, or pointing git's credential helper at the keychain), pick one route and write it as numbered clicks and one paste. Chat will sit with him while he runs it. Once it is in, the watcher needs nothing else; it was seen starting correctly tonight.

*No em or en dashes in this file; checked before writing.*
