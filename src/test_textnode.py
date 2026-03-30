import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_white_space(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node ", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_repr_method(self):
        node = TextNode("This is a text node", TextType.BOLD, "http//here.we.go.com")
        result = f"{node}"
        expected = "TextNode(This is a text node, bold, http//here.we.go.com)"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()