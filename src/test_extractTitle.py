import unittest
from extractTitle import extract_title

class testExtractTitle(unittest.TestCase):

    def test_block_type_h1(self):
        markdown = "# Hello There"
        result = extract_title(markdown)
        expected = "Hello There"
        self.assertEqual(result, expected)

    def test_block_type_h1(self):
        markdown = "## Hello There"
        # result = extract_title(markdown)
        # expected = "Hello There"
        self.assertRaises(Exception, extract_title, markdown)

