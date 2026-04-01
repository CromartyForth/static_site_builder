from textnode import TextNode, TextType

def text_to_textnodes(text):
    new_nodes = []
    originalNode = TextNode(text, TextType.TEXT, None)
    # the first call to the splitDelimiter is going to return a list of TextNodes
    # should we make the text into a TextNode and so every call then uses the same node.text

    # call all the things!
    
    # call **bold** before *italic*


    return new_nodes