# GWFlow Cell Definition

`gwflow_cell_definition.txt` maps groundwater cells to space. Its fixed headings are `cell_id`, `row`, `col`, `x_coord`, `y_coord`, `zone`, `status`, and `area`. For an unstructured grid, `row` and `col` are written as zero. Coordinates are in m and area is in m2.

The definition includes `status > 0` cells, including boundary cells, whereas the [cell water-balance](cell-water-balance.md) writer includes only `status == 1`. The two files therefore need not have the same row population. The file is written during initialization.

[Back to the GWFlow Outputs index](README.md).
