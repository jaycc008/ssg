from htmlnode import LeafNode, ParentNode
from markdown_parser import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from textnode import TextNode, TextType

def main():
	text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
	# print(text_node)

	node = ParentNode(
		"p",
		[
			LeafNode("b", "Bold text"),
			LeafNode(None, "Normal text"),
			LeafNode("i", "italic text"),
			LeafNode(None, "Normal text"),
		],
	)

	# print(node.to_html())

	node = TextNode("This is text with 2 `code``blocks` word", TextType.TEXT)
	new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
	print(f"split nodes: {new_nodes}")

	extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
	print(extract_markdown_images(f"extracted images: {text}"))

	text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
	print(extract_markdown_links(f"extracted links: {text}"))


main()
