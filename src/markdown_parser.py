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
            if new_node.text != "":
                node_lst.append(new_node)
    return node_lst

def split_nodes_image(old_nodes):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            node_lst.append(node)
            continue
        
        segments = []
        node_text = node.text

        for img in images:
            alt = img[0]
            url = img[1]
            delimiter = f"![{alt}]({url})"
            [before, after] = node_text.split(delimiter, 1)

            if before != "":
                segments.append(TextNode(before, TextType.TEXT))

            segments.append(TextNode(alt, TextType.IMAGE, url))

            node_text = after

        if node_text:
            segments.append(TextNode(node_text, TextType.TEXT))
        node_lst.extend(segments)
    return node_lst

def split_nodes_link(old_nodes):
    node_lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_lst.append(node)
            continue

        links = extract_markdown_links(node.text)

        if len(links) == 0:
            node_lst.append(node)
            continue
        
        segments = []
        node_text = node.text

        for link in links:
            txt = link[0]
            url = link[1]
            delimiter = f"[{txt}]({url})"
            [before, after] = node_text.split(delimiter, 1)

            if before != "":
                segments.append(TextNode(before, TextType.TEXT))

            segments.append(TextNode(txt, TextType.LINK, url))

            node_text = after

        if node_text:
            segments.append(TextNode(node_text, TextType.TEXT))
        node_lst.extend(segments)
    return node_lst

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes

def markdown_to_blocks(markdown):
    blocks = list(map(lambda x: x.replace("\n", "").strip(), markdown.split("\n\n")))
    blocks = list(filter(lambda x: x != "", blocks))
    return blocks


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches