import unittest
from generate_html import extract_title, generate_page


class TestInlineMarkdown(unittest.TestCase):
    def test_extract_title(self):
        text = "# Hello there"
        title = extract_title(text)
        self.assertEqual(title, "Hello there")


    def test_eq_double(self):
        actual = extract_title(
            """
            # This is a title

            # This is a second title that should be ignored
            """
        )
        self.assertEqual(actual, "This is a title")


    def test_exception(self):
        text = "Should throw exception"
        with self.assertRaises(Exception):
            extract_title(text)


    def test_extract_title_in_middle(self):
        text = "Header in the middle of this text # Hello there\n\nHow are you?"
        title = extract_title(text)
        self.assertEqual(title, "Hello there")

    def test_generate_page(self):
        generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    unittest.main()
