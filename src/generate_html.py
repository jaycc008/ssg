import os
import re

from markdown_parser import markdown_to_html_node


def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        match = re.search(r"(#{1} )([^\n]+)", block)
        if match:
            return match.group(2).strip()
        else:
            raise Exception("No title found")
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dirname = os.path.dirname(dest_path)
    if dirname != "":
        os.makedirs(dirname, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    items = os.listdir(dir_path_content)

    for item in items:
        src_path = os.path.join(dir_path_content, item)
        if os.path.isfile(src_path):
            html_file = item.replace(".md", ".html")
            dst_path = os.path.join(dest_dir_path, html_file)
            generate_page(src_path, template_path, dst_path)
        else:
            dst_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(src_path, template_path, dst_path)