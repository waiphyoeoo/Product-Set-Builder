# Product Set Builder

Technical module name: `product_set_builder`. Target: Odoo 18.

This package renames the addon, models, fields, methods, XML identifiers,
access rules, source filenames, translation references and static assets.
It is a separate addon for a fresh installation, not an in-place upgrade.
Existing records from the previous addon are not migrated automatically.
For an existing database, prepare and test a data migration before replacing
its installed addon. Adapt dependent custom addons to the new technical names.
Do not install both versions together without testing their inherited views
and constraints on a disposable database.

Sales/purchase extension addons are not included. The static image is an
edited illustration of the original screenshot, not a live Odoo 18 capture.

Validation: Python/XML syntax, manifest paths, model/access references, and
ZIP integrity. No Odoo installation or runtime test has been performed.
