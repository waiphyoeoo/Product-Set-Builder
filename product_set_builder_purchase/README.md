# Product Set Builder - Purchase

Technical addon: `product_set_builder_purchase` (Odoo 18).
Dependencies: `product_set_builder` and `purchase`.
Use the fully renamed base addon supplied with this extension.

This is a separate addon for a fresh installation. Existing records are not
migrated automatically. Adapt any dependent custom addons to the renamed
models, fields, methods, XML IDs and source filenames before use.
Do not install alongside the previous version without testing inherited views
and preparing a migration on a disposable database.

The original author, website, support and LGPL-3 license metadata are preserved.
The purchase dependency is explicit, and the default maximum line sequence
uses the numeric sequence rather than the line record.

Static screenshots are edited illustrations, not live Odoo 18 captures.
Python/XML syntax, local imports, manifest paths, cross-addon references,
absence of the previous naming, and ZIP integrity were checked.
No Odoo runtime installation test has been performed.
