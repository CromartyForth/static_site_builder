from extractTitle import extract_title
from markdownToHTMLNode import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):

    # Print a message like "Generating page from from_path to dest_path using template_path
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    markdown = ""
    template = ""
    try:
        with open(from_path, "r") as file:
            markdown = file.read()
        with open(template_path, "r") as file:
            template = file.read()
    except Exception as e:
        print(e)
        raise e
    
    # extract title
    title = extract_title(markdown)

    # generate html
    htmlNodes = markdown_to_html_node(markdown)
    html = htmlNodes.to_html()

    # insert into template
    

