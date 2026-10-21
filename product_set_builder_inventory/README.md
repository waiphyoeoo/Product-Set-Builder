# Product Set Builder - Inventory

Technical addon: `product_set_builder_inventory` (Odoo 18).
Dependencies: `product_set_builder` and `stock`.
Use the fully renamed base addon supplied earlier.

The addon name, source filenames, classes, models, fields, methods, XML IDs,
action/view references and static assets use the new naming.
The original author, website, support and LGPL-3 metadata are preserved.
The copied purchase description was replaced with inventory documentation;
purchase-order screenshots were removed. Existing edited configuration and
shared wizard illustrations were reused after verifying identical originals.

The maximum existing stock-move sequence now uses its numeric sequence;
debug prints were removed. Other stock move behavior is preserved, including
the existing hardcoded company/product/UoM fallbacks. Review these on a test
database before use with real inventory. Section/note handling was not redesigned.

This is a separate addon, not a direct upgrade of an existing installation.
Existing data is not automatically migrated. Adapt custom dependent addons
and test a migration before replacing an installed addon.

Validation covers syntax, imports, manifest/assets, renamed models and
cross-addon action/view references, and ZIP integrity. No Odoo runtime
installation or stock transfer test has been performed.
