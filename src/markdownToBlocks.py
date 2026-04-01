

def markdown_to_blocks(markdown):
    new_blocks = []

    splitList = markdown.split("\n\n")

    for block in splitList:
        if block == "":
            continue
        new_blocks.append(block.strip())
    
    return new_blocks