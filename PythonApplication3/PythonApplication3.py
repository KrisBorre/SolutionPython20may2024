from notebook.notebookapp import NotebookApp

# Start a Jupyter Notebook server
app = NotebookApp.instance()
app.initialize(argv=[])  # No additional arguments
app.start()
