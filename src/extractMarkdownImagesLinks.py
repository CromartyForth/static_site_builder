import re
from textnode import TextNode, TextType


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?\/.*?\.\w+)\)", text)
    return matches
     

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?\/.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    # get the extracted matches unless it's not a TEXT node.
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # get the match tuples - skip current node if no matches
        matches = extract_markdown_images(node.text)
        if matches == []:
            new_nodes.append(node)
            continue

        # pass the whole text through split that many times.
        textForSpliting = node.text
        lastSplit = []
        for match in matches:
            splitList = textForSpliting.split(f"![{match[0]}]({match[1]})", 1)

            # add processed nodes to new_nodes - first node might be ""
            if splitList[0] != "":
                new_nodes.append(TextNode(splitList[0], TextType.TEXT))

            # next node is the image node so generate from match tuple
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))

            # final node copied to nodeForSplitting for next itteration
            textForSpliting = splitList[1]
            lastSplit = [splitList[1]]

        # add last node onto new_nodes unless it's empty
        if lastSplit[0] != "":
            new_nodes.append(TextNode(lastSplit[0], TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    # if node is not a textType.TEXT then it's already been processed.
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # get the match tuples - skip current node if no matches
        matches = extract_markdown_links(node.text)
        if matches == []:
            new_nodes.append(node)
            continue

        # pass the whole text through split that many times.
        textForSpliting = node.text
        lastSplit = []
        for match in matches:
            splitList = textForSpliting.split(f"[{match[0]}]({match[1]})", 1)

            # add processed nodes to new_nodes - first node might be ""
            if splitList[0] != "":
                new_nodes.append(TextNode(splitList[0], TextType.TEXT))

            # next node is the link node so generate from match tuple
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))

            # final node copied to nodeForSplitting for next itteration
            textForSpliting = splitList[1]
            lastSplit = [splitList[1]]

        # add last node onto new_nodes unless it's empty
        if lastSplit[0] != "":
            new_nodes.append(TextNode(lastSplit[0], TextType.TEXT))
    
    return new_nodes
