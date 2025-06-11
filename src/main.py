from textnode import *
import os
import shutil
from generate_page import *

def main():
    #test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(test)
    copy_dictonary()
    #generate_page(os.path.expanduser("content/index.md"), os.path.expanduser("template.html"), os.path.expanduser("public/index.html"))
    generate_pages_recursive(os.path.expanduser("content"), os.path.expanduser("template.html"), os.path.expanduser("public"))

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
    destenation = os.path.expanduser("~/static_site/public")
    if os.path.exists(destenation):
        shutil.rmtree(destenation)
    os.mkdir(destenation)
    rercursion(destenation, source)


main()

