from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'ISCV is a computer vision library.'
LONG_DESCRIPTION = 'ISCV (Interactive Simulations using Computer Vision) is an python library that lets you use machine learning models in an easy and productive way for your project.'

# Setting up
setup(
    name="ISCV",
    version=VERSION,
    author="Mitansh Disha Meet Parnika",
    author_email="<mitanshpanchal@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'numpy', 'mediapipe'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets', 'computer vision', 'machine learning', 'AI'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
