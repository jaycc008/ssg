import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue

        segments = node.text.split(delimiter)

        if len(segments) % 2 == 0:
            raise ValueError("Unmatched delimiters found in text.")

        for i in range(len(segments)):
            if i % 2 == 0:
                new_node = TextNode(segments[i], TextType.TEXT)
            else:
                new_node = TextNode(segments[i], text_type)
            node_lst.append(new_node)
    return node_lst

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches