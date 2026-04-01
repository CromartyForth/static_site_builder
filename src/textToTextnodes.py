from textnode import TextNode, TextType
from splitDelimiter import split_nodes_delimiter
from extractMarkdownImagesLinks import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    originalNode = TextNode(text, TextType.TEXT, None)
    new_nodes = [originalNode]
    
    # call all the things!
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    
    #extract links and images
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes