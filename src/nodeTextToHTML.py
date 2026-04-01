from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    
    if hasattr(text_node,"children") == False:
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text, None)
        
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})

            case TextType.IMAGE:
                return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
            
            case _:
                return LeafNode("Dammit", "Janet!", None)
            
    return LeafNode("what", "No way!!", None)