# This is a solution to the problem; when we are not able to launch jupyter notebook in safari from Anaconda-Navigator with macOS Sierra.

1. Go to this location **~/.jupyter/jupyter_notebook_config.py**  
	1. Hold _Command + shift_ key and press _.dot_ to see hidden files in your root directory  
	2. If you can not find **_'jupyter_notebook_config.py'_**, run this command on your terminal to create one **'jupyter notebook --generate-config'**

2. Update **_c.NotebookApp.browser = u'Safari'_** in the file **jupyter_notebook_config.py**. Uncomment and save the file.

Detailed description and solution for the problem can be found [here](https://github.com/jupyter/notebook/issues/2438)