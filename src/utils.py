import re


def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        match = re.search(r"(#{1} )([^\n]+)", block)
        if match:
            return match.group(2).strip()
        else:
            raise Exception("No title found")