import unittest

from splitDelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):

    def test_eq(self):
        node = "This is text with a `code block` word"
        delimiter = "`"
        delimiterTextType = TextType.CODE

        result = split_nodes_delimiter([node], delimiter, delimiterTextType)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)


    def test_leading_block(self):
        node = "**Be Bold** lead from the front"
        delimiter = "**"
        delimiterTextType = TextType.BOLD

        result = split_nodes_delimiter([node], delimiter, delimiterTextType)
        expected = [
            TextNode("Be Bold", TextType.BOLD),
            TextNode(" lead from the front", TextType.TEXT),
        ]
        self.assertEqual(result, expected)


    def test_trailing_block(self):
        node = "Shout from the back *This is irony*"
        delimiter = "*"
        delimiterTextType = TextType.ITALIC

        result = split_nodes_delimiter([node], delimiter, delimiterTextType)
        expected = [
            TextNode("Shout from the back ", TextType.TEXT),
            TextNode("This is irony", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)


    def test_double_block(self):
        node = "**Shout** from the back **You Suck!**"
        delimiter = "**"
        delimiterTextType = TextType.BOLD

        result = split_nodes_delimiter([node], delimiter, delimiterTextType)
        expected = [
            TextNode("Shout", TextType.BOLD),
            TextNode(" from the back ", TextType.TEXT),
            TextNode("You Suck!", TextType.BOLD),
        ]
        self.assertEqual(result, expected)
    
    def test_missing_delimiator(self):
        node = "**Shout** from the back **You Suck!"
        delimiter = "**"
        delimiterTextType = TextType.BOLD

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], delimiter, delimiterTextType)
    