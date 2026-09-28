**Needs from Chat:** add two lines to the go-live checklist on the "Hosting & Go-Live" board card, so neither is forgotten at cutover.

# RULING: two items join the go-live checklist

**From:** Claude Code, factory session, S134. **To:** Claude Chat.

## Kain's words

"Agreed, add 'switch on Memcached' and 'set the jobs timer' to the go-live checklist so neither gets forgotten." He also said he is not certain Pooka & Co will be used, so neither item is written as theirs.

## The two lines

1. **Switch on Memcached** (persistent object cache). The server supports it (the `memcached` PHP module is present) and SiteGround Speed Optimizer switches it with `wp sg memcached enable`, after Memcached is enabled in SiteGround Site Tools. Not switched on during the build: it helps under real traffic, and on the build ground it could serve a stale copy during nightly imports. Test the pricing page and a few key pages right after switching it on; off again if anything looks wrong.
2. **Set the jobs timer.** A SiteGround Site Tools cron job calling `wp-cron.php` every five minutes, so scheduled jobs (Action Scheduler, SearchWP, the consent plugin) run on time whether or not anyone visits. It cannot be set over SSH (no crontab there); it needs whoever holds the SiteGround login.

## For the record, from the same Site Health read (24 to 28 September)

- "Search engines are discouraged": correct by design on the build ground; the go-live flip is already `cutover_gate.py --golive`.
- "Opcode cache is not enabled": the server reports OPcache on (`opcache.enable` 1); nothing to do.
- "MCP OAuth discovery documents": a connector add-on's notice; not used; nothing to do.
- The late scheduled job was caught up the same day; nothing was overdue when checked.

## OWED BACK

Nothing.

*No em or en dashes in this file; checked before writing.*
