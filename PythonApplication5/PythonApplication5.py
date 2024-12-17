import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Load the notebook
with open("example_notebook.ipynb", "r") as f:
    notebook = nbformat.read(f, as_version=4)

# Execute the notebook
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(notebook)

# Save the executed notebook
with open("executed_notebook.ipynb", "w") as f:
    nbformat.write(notebook, f)

print("Executed notebook saved as executed_notebook.ipynb")
