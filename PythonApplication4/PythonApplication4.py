import nbformat as nbf

# Create a new notebook object
nb = nbf.v4.new_notebook()

# Add some cells to the notebook
nb.cells.append(nbf.v4.new_code_cell("print('Hello, Jupyter!')"))
nb.cells.append(nbf.v4.new_markdown_cell("# This is a Markdown cell"))

# Save the notebook to a file
with open("example_notebook.ipynb", "w") as f:
    nbf.write(nb, f)

print("Notebook created: example_notebook.ipynb")

