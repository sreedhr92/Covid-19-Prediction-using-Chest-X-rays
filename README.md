Installing Python packages
Python is available for all three major operating systems — Microsoft Windows, Mac OS X, and Linux — and the installer, as well as the documentation, can be downloaded from the official Python website: https://www.python.org.

This book is written for Python version >= 3.4.3, and it is recommended you use the most recent version of Python 3 that is currently available, although most of the code examples may also be compatible with Python >= 2.7.10. If you decide to use Python 2.7 to execute the code examples, please make sure that you know about the major differences between the two Python versions. A good summary about the differences between Python 3.4 and 2.7 can be found at https://wiki.python.org/moin/Python2orPython3.

Note

You can check your current default version of Python by executing

$ python -V
In my case, it returns

Python 3.5.1 :: Continuum Analytics, Inc.
Pip
The additional packages that we will be using throughout this book can be installed via the pip installer program, which has been part of the Python standard library since Python 3.3. More information about pip can be found at https://docs.python.org/3/installing/index.html.

After we have successfully installed Python, we can execute pip from the command line terminal to install additional Python packages:

pip install SomePackage
(where SomePackage is a placeholder for numpy, pandas, matplotlib, scikit-learn, and so forth).

Already installed packages can be updated via the --upgrade flag:

pip install SomePackage --upgrade
Anaconda
A highly recommended alternative Python distribution for scientific computing is Anaconda by Continuum Analytics. Anaconda is a free—including commercial use—enterprise-ready Python distribution that bundles all the essential Python packages for data science, math, and engineering in one user-friendly cross-platform distribution. The Anaconda installer can be downloaded at http://continuum.io/downloads#py34, and an Anaconda quick start-guide is available at https://store.continuum.io/static/img/Anaconda-Quickstart.pdf.

After successfully installing Anaconda, we can install new Python packages using the following command:

conda install SomePackage
Existing packages can be updated using the following command:

conda update SomePackage
Throughout this book, we will mainly use NumPy's multi-dimensional arrays to store and manipulate data. Occasionally, we will make use of pandas, which is a library built on top of NumPy that provides additional higher level data manipulation tools that make working with tabular data even more convenient. To augment our learning experience and visualize quantitative data, which is often extremely useful to intuitively make sense of it, we will use the very customizable matplotlib library.

Core packages
The version numbers of the major Python packages that were used for writing this book are listed below. Please make sure that the version numbers of your installed packages are equal to, or greater than, those version numbers to ensure the code examples run correctly:

NumPy 1.9.1
SciPy 0.14.0
scikit-learn 0.15.2
matplotlib 1.4.0
pandas 0.15.2
openCV 4.2
tensorflow 2.1
keras 2.4.3
seaborn 0.11.1


Python/Jupyter Notebook
Some readers weere wondering about the .ipynb of the code files -- these files are IPython notebooks. I chose IPython notebooks over plain Python .py scripts, because I think that they are just great for data analysis projects! IPython notebooks allow us to have everything in one place: Our code, the results from executing the code, plots of our data, and documentation that supports the handy Markdown and powerful LaTeX syntax!



Side Note:

"IPython Notebook" recently became the "Jupyter Notebook"; Jupyter is an umbrella project that aims to support other languages in addition to Python including Julia, R, and many more. Don't worry, though, for a Python user, there's only a difference in terminology (we say "Jupyter Notebook" now instead of "IPython Notebook").

The Jupyter notebook can be installed as usually via pip.

$ pip install jupyter notebook
Alternatively, we can use the Conda installer if we have Anaconda or Miniconda installed:

$ conda install jupyter notebook
To open a Jupyter notebook, we cd to the directory that contains your code examples, e.g,.

$ cd ~/code/python-machine-learning-book
and launch jupyter notebook by executing

$ jupyter notebook
Jupyter will start in our default browser (typically running at http://localhost:8888/). Now, we can simply select the notebook you wish to open from the Jupyter menu.



For more information about the Jupyter notebook, I recommend the Jupyter Beginner Guide.

🛑 Note: please do not claim diagnostic performance of a model without a clinical study! This is not a kaggle competition dataset. Please read this paper about evaluation issues: https://arxiv.org/abs/2004.12823 and https://arxiv.org/abs/2004.05405


Introduction:

COVID-19 (coronavirus disease 2019) infection which began in De- cember 2019 in Wuhan, China has widely spread all over the world. COVID-19 causes severe respiratory symptoms and is associated with relatively high ICU admission and mortality. Along with the continuously increasing number of cases, test kits were produced by aiming diagnosis. But according to the Hematology Fellow Atilla Uslu from Ankara University School of Medicine, “They started to have cases where the coronavirus test was negative twice, but lung tomography seemed compatible with coronavirus.
How the samples are taken from the mouth and nose affects the results. When not properly taken, these tests can produce incorrect results” 26 March 2020, Tweet. Also, it has been reported that the sensitivity of the test kits might not be high enough for the early detection and treat- ment of presumptive patients [1]. Therefore, the CT scan images of the lungs play a significant role in the early detection of the COVID- 19.

Purpose of the study

This study aims to design and develop a deep learning model for early detection of the COVID-19 by using chest x-ray images.

Future Work
As a future work, the number of data which is used to train the CNN model can be increased and the general structure of convolutional neural network can be restructures so that it will be able to analyze images in more detail.