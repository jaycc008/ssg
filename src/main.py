from htmlnode import LeafNode, ParentNode
from markdown_parser import block_to_block_type, extract_markdown_images, extract_markdown_links, markdown_to_blocks, markdown_to_html_node, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

def main():
	# text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
	# # print(text_node)

	# node = ParentNode(
	# 	"p",
	# 	[
	# 		LeafNode("b", "Bold text"),
	# 		LeafNode(None, "Normal text"),
	# 		LeafNode("i", "italic text"),
	# 		LeafNode(None, "Normal text"),
	# 	],
	# )

	# # print(node.to_html())

	# # node = TextNode("This is text with 2 `code``blocks` word", TextType.TEXT)
	# # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
	# # print(f"split nodes: {new_nodes}")

	# # text_with_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
	# # print(extract_markdown_images(f"extracted images: {text_with_images}"))

	# # text_with_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
	# # print(extract_markdown_links(f"extracted links: {text_with_links}"))

	# node = TextNode(
	# 	"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
	# 	TextType.TEXT,
	# )
	# link_nodes = split_nodes_link([node])
	# print(f"split nodes: {link_nodes}")
	# # new_nodes = split_nodes_link([node])

	# nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
	# print(nodes)

	# print(markdown_to_blocks("This is a block\n\nThis is another block\n\nThis is the last block\n\n\n\n\n yo\nyo\nyo   "))
	markdown_to_html_node("```some code to start with```\n\n# Hi, welcome to my site\n\n## I am Jayce and this is my site\n\nThis is a nice paragraph with **some bold text**, there's also some *italics* in this same paragraph\n\nI feel like some people like to quote a bit too so that is what can be seen here\n\n>I love quotes\n>They are so nice\n\nLovely ordered list: \n\n1. One\n2. Two\n3. Three\n\n* How unorderly\n* This UL\n\n* Also known as an Unordered List\n\n###### Heading at the end")

main()
