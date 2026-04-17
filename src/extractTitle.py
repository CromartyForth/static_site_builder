import re

def extract_title(markdown):
    markdown.replace("\n", "")
    matches = re.fullmatch(r"^#{1} .*", markdown)
    if matches == None:
        raise Exception("h1 title absent")
    
    result = markdown.removeprefix("# ").strip()
    return result