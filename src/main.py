import os
import sys
import shutil
from textnode import TextNode, TextType
from generatePage import generate_page, generate_pages_recursive

source = "./static"
destination = "./docs"

template_path ="./template.html"

dir_path_content = "./content"


def copy_directory_contents(source, destination):
    # check destination directory exists
    if os.path.exists(destination):
        # empty contents of destination
        shutil.rmtree(destination) #onexc=remove_readonly
    
    # make destination directory
    os.mkdir(destination)

    # check source directory exists
    if os.path.exists(source) == False:
        raise ValueError("Source directory does not exist")

    copy_tree(source, destination)

    return
  

def copy_tree(source, destination):
    
    # recursively read directory and copy files
    with os.scandir(source) as source:
        for entry in source:
            if entry.is_file():
                # copy file
                print(entry.path)
                shutil.copy(entry.path, destination)
                print(f'copied {entry.name}')

            if entry.is_dir():
                path = os.path.join(destination, entry.name)
                os.mkdir(path)
                print(f'created {entry.path}')
                copy_tree(entry.path, path)

    return



def main ():
    
    # get cli args
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(basepath)

    try:
        copy_directory_contents(source, destination)
    except ValueError as e:
        print(e)

    try:
        generate_pages_recursive(dir_path_content, template_path, destination, basepath)

    except Exception as e:
        print("file error - " + str(e))

    return


main()


