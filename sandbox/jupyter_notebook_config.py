c = get_config()  # noqa: F821
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False