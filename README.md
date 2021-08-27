# rafflePicker

A quick project to generate some winning numbers from a user-provided range. It is also possible to specify numbers to exclude from the range.

## Quick Run

To quickly run this project, [click here to open in Google Colab (online - no download required)](https://colab.research.google.com/github/domRG/rafflePicker/blob/main/colab_run_rafflePicker.ipynb).
Alternatively, click above to open the "colab_run_rafflePicker.ipynb" file, then select "Open In Colab" at the top of the file.

You'll need to sign-in with a Google account before you can run it, but after that just follow the instructions provided.

## Build & Execution

The latest release contains the .exe (and SHA-256) generated from compiling `main.py` using (PyInstaller)[https://www.pyinstaller.org/index.html].

If you wish to build this yourself, the command I used is as follows: `pyinstaller main.py --onefile --console --name rafflePicker` to generate a single file executable.

