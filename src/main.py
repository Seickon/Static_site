from textnode import *
import os
import shutil
from generate_page import *
import sys

def main():
    basepath = sys.argv[1]
    copy_dictonary()
    generate_pages_recursive(os.path.expanduser("content"), os.path.expanduser("template.html"), os.path.expanduser("docs"), basepath)

def rercursion(destination, source):
        contents = os.listdir(source)
        for file in contents:
            file_path = os.path.join(source, file)
            if os.path.isfile(file_path):
                shutil.copy(file_path, destination)
            else:
                os.mkdir(os.path.join(destination, file))
                rercursion(os.path.join(destination, file), file_path)

def copy_dictonary():
    source = os.path.expanduser("~/static_site/static")
    destenation = os.path.expanduser("~/static_site/docs")
    if os.path.exists(destenation):
        shutil.rmtree(destenation)
    os.mkdir(destenation)
    rercursion(destenation, source)


main()

