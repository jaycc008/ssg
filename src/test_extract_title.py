import unittest
from utils import extract_title


class TestInlineMarkdown(unittest.TestCase):
    def test_extract_title(self):
        text = "# Hello there"
        title = extract_title(text)
        self.assertEqual(title, "Hello there")


    def test_extract_title_in_middle(self):
        text = "Should throw exception"
        title = extract_title(text)
        self.assertRaises(Exception("No title found"), title)


    def test_extract_title_in_middle(self):
        text = "Header in the middle of this text # Hello there\n\nHow are you?"
        title = extract_title(text)
        self.assertEqual(title, "Hello there")

if __name__ == "__main__":
    unittest.main()
