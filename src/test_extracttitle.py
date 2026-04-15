import unittest
from extractTitle import extract_title

class testExtractTitle(unittest.TestCase):

    def text_block_type_h1(self):
        markdown = "# Hello"
        result = extract_title(markdown)
        expected = "Hello"
        self.assertEqual(result, expected)

