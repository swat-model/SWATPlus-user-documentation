---
description: File pointer
---

# fp

The file pointer is only needed for certain actions. The file that is referenced by the file pointer depends on the action. The table below lists the actions that use the file pointer and which file it points to.

| **Action**    | **File referenced by file pointer**                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| harvest       | [harv.ops](../../management-practices/harv.ops/) ([name](../../management-practices/harv.ops/name_harvops.md))           |
| harvest\_kill | [harv.ops](../../management-practices/harv.ops/) ([name](../../management-practices/harv.ops/name_harvops.md))           |
| pest\_apply   | [chem\_app.ops](../../management-practices/chem_app.ops/) ([name](../../management-practices/chem_app.ops/name_chem.md)) |
| fertilize     | [chem\_app.ops](../../management-practices/chem_app.ops/) ([name](../../management-practices/chem_app.ops/name_chem.md)) |
