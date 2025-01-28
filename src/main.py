from htmlnode import LeafNode, ParentNode
from markdown_parser import split_nodes_delimiter
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

	node = TextNode("This is text with 2 `code``blocks`", TextType.TEXT)
	new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
	print(node)
	print(new_nodes)
	
main()
