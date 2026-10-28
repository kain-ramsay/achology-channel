# SHIP 0.707.668: the enquiry form no longer loses a real enquiry in silence (theme, S203)

First line: nothing needed from Chat beyond closing the launch blocker line on the board (Backlog: Code, the S202 review's enquiry limit).

What changed. `enquiries-setup.php`: the five-an-hour limit is split from the bot guard. A person who trips it is now told, with the form's own signed line ("Your enquiry could not be sent. Please try again in a moment."), and everything typed stays in the form. A bot (trap filled, stamp missing, forged or under four seconds) is still answered with a silent success, as ruled at S441.

Why. The S202 cloud review, section 3 row 1: a tripped limit answered "ok" and sent no email, so a real sender read "Your Enquiry Has Been Received" and the enquiry was lost.

The measurement the queue asked for first. A throwaway probe page on the build site (deleted after) read back each caller's own public address in `REMOTE_ADDR`: this Mac 5.181.57.102, the server's own request 35.214.30.153. SiteGround's proxy restores the real address, so the per-address key was right and was kept. (The first read showed both machines the same address only because the host's page cache served one copy; a cache-busted read showed each its own.)

Proof. Deploy: local, server and zip agree at 0.707.668, every PHP file parsed on the server. Read back live: a bot-trap send answers `{"ok":true}` 200; a faulty send answers its three field errors 400. Not triggered live: the tripped branch itself, which needs five real emails to the enquiries inbox; the publishing wall refuses the shell eval that would set the counter, and that refusal stands. Verified 2 of 3 paths; the third is read from the code.

Theme commit bf075258. Queue line struck.

OWED BACK: nothing.
