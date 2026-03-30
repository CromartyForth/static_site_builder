import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def setUp(self):
        self.props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }

        self.node = HTMLNode("a", "Here's a link", None, self.props)
        self.node2 = HTMLNode("a", "Here's a link", None, {})
    
    
    def test_eq(self):
        result = f"{self.node}"
        expected = "HTMLNode(a, Here's a link, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(result, expected)
    
    def test_props_to_html(self):
        result = self.node.props_to_html()
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)
    
    def test_props_to_html_empty(self):
        result = self.node2.props_to_html()
        expected = ""
        self.assertEqual(result, expected)