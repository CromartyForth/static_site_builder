import os
import shutil
from extractTitle import extract_title
from markdownToHTMLNode import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # check content directory exists
    if os.path.exists(dir_path_content) == False:
        raise ValueError("Content directory does not exist")
    generate_pages_recursive_helper(dir_path_content, template_path, dest_dir_path, basepath)
    
def generate_pages_recursive_helper(dir_path_content, template_path, dest_dir_path, basepath):
    # crawl the directory for every md file
    with os.scandir(dir_path_content) as content:
        for entry in content:
            if entry.is_file() and entry.name.endswith('.md'):
                # create html and write it to the same directory structure in destination directory
                name = (entry.name.removesuffix(".md")) + ".html"
                destination_path = os.path.join(dest_dir_path, name)
                generate_page(entry.path, template_path, destination_path, basepath)
                continue
            if entry.is_dir():
                destination_path = os.path.join(dest_dir_path, entry.name)
                os.mkdir(destination_path)
                print(f'created {entry.path}')
                generate_pages_recursive_helper(entry.path, template_path, destination_path, basepath)
                
    return




def generate_page(from_path, template_path, dest_path, basepath):

    # Print a message like "Generating page from from_path to dest_path using template_path
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    markdown = ""
    template = ""
    firstline = ""
    try:
        with open(from_path, "r") as file:
            markdown = file.read()
        with open(from_path, "r") as file:
            firstline = file.readline().replace("\n", "")
        with open(template_path, "r") as file:
            template = file.read()
    except Exception as e:
        print(e)
        raise e

    # extract title
    title = extract_title(firstline)
    print(title)

    # generate html
    htmlNodes = markdown_to_html_node(markdown)
    html = htmlNodes.to_html()
    print(html)

    # insert into template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    # create destination path for file
    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok = True)

    # write file to path
    try:
        with open(dest_path, "w") as file:
            result = file.write(template)
    except Exception as e:
        raise e   
    
    print("Bytes writen " + str(result))

