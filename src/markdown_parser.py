from enum import Enum
import re
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes

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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UL:
        return ul_to_html_node(block)
    if block_type == BlockType.OL:
        return ol_to_html_node(block)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    heading_count = block.count('#')
    children = text_to_children(block[heading_count+1])
    return ParentNode(f"h{heading_count}", children)

def code_to_html_node(block):
    children = text_to_children(block[3:-3])
    code = ParentNode("code", children)
    return ParentNode("pre", code)

def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def markdown_to_blocks(markdown):
    blocks = list(map(lambda x: x.strip(), markdown.split("\n\n")))
    blocks = list(filter(lambda x: x != "", blocks))
    return blocks

def block_to_block_type(block):
    if match_heading(block):
        block_type = BlockType.HEADING
    elif match_code_block(block):
        block_type = BlockType.CODE
    elif match_quote_block(block):
        block_type = BlockType.QUOTE
    elif match_ul(block):
        block_type = BlockType.UL
    elif match_ol(block):
        block_type = BlockType.OL
    else:
        block_type = BlockType.PARAGRAPH
    return block_type

def match_heading(block):
    return re.match(r"(^#{1,6} )", block)
    
def match_code_block(block):
    return re.match(r"(```[\s\S]+```)", block)

def match_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if not re.match(r"(>)", line):
            return False
    return True

def match_ul(block):
    lines = block.split("\n")
    for line in lines:
        if not re.match(r"(- )", line) and not re.match(r"(\* )", line):
            return False
    return True

def match_ol(block):
    lines = block.split("\n")
    for i, line in enumerate(lines):
        if not re.match(rf"({i+1}. )", line):
            return False
    return True

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches