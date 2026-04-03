from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splitNodes = node.text.split(delimiter)

        # spliting with correct markup will always result in an odd number of pieces
        if len(splitNodes) % 2 == 0:
            raise ValueError("invalid Markup syntax")

        # itterate through list
        for i, value in enumerate(splitNodes):
            if i % 2 != 0:
                new_nodes.append(TextNode(value, text_type))
            else:
                if value != "":
                    new_nodes.append(TextNode(value, TextType.TEXT))
    
    return new_nodes
