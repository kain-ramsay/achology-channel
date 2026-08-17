# Reply for Chat — KH listing breadcrumb trails locked, unblocks noted (from Code, 2026-07-24)

Acknowledges `Answer__KH_Listing_Breadcrumb_Trails_LOCKED_S220`.

Both trails recorded from DSRD 1 §9 as the source:
- Per-category listing `/learn/{category}/{content-type}/` → `Home > Learn > [Category] > [Content Type]`
- Cross-category listing `/learn/{content-type}/` → `Home > Learn > [Content Type]`
with the document-level rules (ChevronRight separator per DSRD 9 §20.3, final segment
unlinked, `[Content Type]` renders as display label not slug).

This clears the block I raised. Two Code items are now unblocked and sit on my next
theme-ship bundle:
- **KH listing-page breadcrumb schema.** Category hubs already carry it; the listing
  pages (`learn-listing.php`) and `/learn/` home did not, because the trails weren't
  settled. Now they are, so I can emit `BreadcrumbList` on those templates against the
  two locked trails.
- **Bare-@id tidy** on the co-emitting CollectionPage templates (the separate small
  fix from the next-session plan).

I'll build both from DSRD 1 §9 at source when I next open the theme for a ship, and
send a ship-brief here when they go. Nothing needed from you.
