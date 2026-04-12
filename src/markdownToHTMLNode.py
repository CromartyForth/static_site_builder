from blocktypes import (
    BlockType, 
    block_to_block_type, 
    create_heading_html_node, 
    create_code_html_node,
    create_unordered_list_html_node,
    create_ordered_list_html_node,
    create_paragraph_html_node,
    create_quote_html_node
)
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
        # helper functions could be refactored to return list to avoid splitlines running twice
        match block_type:
            case BlockType.QUOTE:
                block_HTML_node = create_quote_html_node(block)
                children = text_to_children(block_HTML_node.value)
                blockNodeList.append(ParentNode("quote", children, None))


            case BlockType.HEADING:
                block_HTML_node = create_heading_html_node(block)
                children = text_to_children(block_HTML_node.value)
                blockNodeList.append(ParentNode(block_HTML_node.tag, children, None))

            case BlockType.CODE:
                block_HTML_node = create_code_html_node(block)
                # text in a code block is not parsed further like the other blocks
                children = [LeafNode("code", block_HTML_node.value, None)]
                blockNodeList.append(ParentNode("pre", children, None))
            
            case BlockType.UNORDEREDLIST:
                block_HTML_node = create_unordered_list_html_node(block)
                block_children = block_HTML_node.value.splitlines()
                
                # block of text needs to be treated line by line.
                li_children = [] #list items
                for block_child in block_children:
                    children = text_to_children(block_child)
                    li_children.append(ParentNode("li", children, None))

                ul_parent = ParentNode("ul", li_children, None) #unorderedlist
                
                blockNodeList.append(ParentNode(block_HTML_node.tag, ul_parent, None))

            case BlockType.ORDEREDLIST:
                block_HTML_node = create_ordered_list_html_node(block)
                block_children = block_HTML_node.value.splitlines()
                
                # block of text needs to be treated line by line for lists.
                li_children = [] #list items
                for block_child in block_children:
                    children = text_to_children(block_child)
                    li_children.append(ParentNode("li", children, None))

                ol_parent = ParentNode("ol", li_children, None) #unorderedlist
                
                blockNodeList.append(ParentNode(block_HTML_node.tag, ol_parent, None))

            case BlockType.PARAGRAPH:
                block_HTML_node = create_paragraph_html_node(block)
                children = text_to_children(block_HTML_node.value)
                blockNodeList.append(ParentNode("p", children, None))


    # put all the blocknodes in a parentnode div
    outerDivNode = ParentNode("div", blockNodeList, None)

    # generate html!
    # html = outerDivNode.to_html()
    
    return outerDivNode


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

    leaf_nodes = []
    for item in text_nodes:
        leaf_nodes.append(text_node_to_html_node(item))
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

