from enum import Enum
from htmlnode import HTMLNode, ParentNode
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

#class BlockNode:
#   def __init__(self, text, block_type):
#        self.text = text
#        self.block_type = block_type

def block_to_block_type(block):
    lines = block.split("\n")

    # Headings 1-6# then a space
    matches = re.fullmatch(r"^# .*", block)
    if matches != None:
        return BlockType.HEADING

    # Muliline Code Blocks ```\n```
    if (lines[0] == "```" and lines[-1] == ("```")):
        return BlockType.CODE
    
    # quote block > on every line
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # unordered list - on every line
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDEREDLIST

    # ordered list d. on every line 1++
    ordered_list = True
    for i, value in enumerate(lines):
        if not value.startswith(f"{i+1}. "):
            ordered_list = False
    if ordered_list:
        return BlockType.ORDEREDLIST

    # normal paragraph the default
    return BlockType.PARAGRAPH


def create_heading_html_node(block):
    # count the the # prefix to determine heading tag.
    hTag = 0
    for x in block:
        if x != "#":
            hTag = x + 1
            break
    
    # remove "#"s from text
    value = block.removeprefix(("#" * hTag))

    return HTMLNode(("h" + hTag), value, None, None)


def create_code_html_node(block):
    # remove code prefix and suffix
    value = block.removePrefix("```")
    value = value.removesuffix("```")

    # remove newline
    value = value.strip()

    return HTMLNode("code", value, None, None)


def create_quote_html_node(block):
    # remove quote prefix and space from each line
    lines = block.split()
    new_string = ""
    for line in lines:
        line = line.removePrefix("> ")
        new_string += line + "\n"
    
    return HTMLNode("blockquote", new_string, None, None)


def create_unordered_list_node(block)
    # do what ?!
    # Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag



    
            
