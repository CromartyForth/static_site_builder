from blocktypes import BlockType, block_to_block_type, create_heading_html_node
from markdownToBlocks import markdown_to_blocks
from textToTextnodes import text_to_textnodes
from nodeTextToHTML import text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)

    blockNodeList = []
    for block in blocks:
        # determine what each block is
        block_type = block_to_block_type(block)

        # create work in progress html node from block and blocktype. maybe make this a helper function
        match block_type:
            case BlockType.HEADING:
                block_HTML_node = create_heading_html_node(block)
            
            case BlockType.CODE:
                block_HTML_node = create_code_html_node(block)
        


        # get the children from the parentNode.value
        # assign the proper child HTMLnode objects to the block node
        # unless you are a code block
        if block_type != BlockType.CODE:
            children = text_to_children(block_HTML_node.value)
        else:
            children = [LeafNode(None, block_HTML_node.value, None)]

        # add a new parentNode to blockNodeList
        blockNodeList.append(ParentNode(block_HTML_node.tag, children, None))

    # put all the blocknodes in a parentnode div
    outerDivNode = ParentNode("div", blockNodeList, None)

    # generate html!
    html = outerDivNode.to_html()
    
    return html


def text_to_children(text):
    # called from each block in blocks.
    # it's given the blocks inline text.
    # this function doesn't need to know which block called it.
    # A block node is a parent html node of type block.type

    # so text is split into textnodes
    # using text_to_textnodes(text)
    text_nodes = text_to_textnodes(text)
        # which calls...
        # split_nodes_delimiter()
        # split_nodes_image()
        # split_nodes_link()

    leaf_nodes = text_node_to_html_node(text_nodes)
    # so we have text nodes we can turn into html nodes
    # using text_node_to_html_node
        # which returns leaf nodes if the text node
        # has no children.

    # so we have leaf node that we can turn into html
    return leaf_nodes




"""
    htmlnode
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props # dictionary of key value pairs



"""

