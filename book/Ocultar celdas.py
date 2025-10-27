import nbformat

notebook_path = "book\Capitulo2.ipynb"

nb = nbformat.read(notebook_path, as_version=4)

for cell in nb.cells:
    if cell.cell_type == "code":
        cell.metadata.setdefault("tags", [])
        if "hide-input" not in cell.metadata["tags"]:
            cell.metadata["tags"].append("hide-input")

nbformat.write(nb, notebook_path)
print("Se agregaron los tags 'hide-input' a todas las celdas de código.")
