from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        splitNodes = node.split(delimiter)

        # spliting correctly will always result in an odd number of pieces
        if len(splitNodes) % 2 == 0:
            raise ValueError("invalid Markdown syntax")

        
        # itterate through list
        for i, value in enumerate(splitNodes):
            if i % 2 != 0:
                new_nodes.append(TextNode(value, text_type))
            else:
                if value != "":
                    new_nodes.append(TextNode(value,TextType.TEXT))
    
    return new_nodes








    return