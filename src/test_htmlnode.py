import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def setUp(self):
        self.htmlprops = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        
        self.node = HTMLNode("a", "Here's a link", None, self.htmlprops)
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
 
    
class TestLeafNode(unittest.TestCase):

    def setUp(self):

        self.leafProps = {
            "href": "https://www.google.com",
        }
        self.leafNode1 = LeafNode("p", "This is a paragraph of text.", None)
        self.leafNode2 = LeafNode("a", "Click me!", self.leafProps)
    
    def test_leaf_node_props(self):
        result = self.leafNode2.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)

    def test_leaf_node(self):
        result = self.leafNode1.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected)


class TestParentNode(unittest.TestCase):

    def setUp(self):
        self.nodeP = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
    
    def test_to_html(self):
        result = self.nodeP.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(result, expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")
                         
    def test_to_html_with_children_props(self):
        props = {"href": "https://www.google.com",}
        child_node = LeafNode("a", "Heres a link", props)
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(parent_node.to_html(),'<div><a href="https://www.google.com">Heres a link</a></div>')
    
    def test_to_html_no_children(self):
        children = []
        parent_node = ParentNode("div", [], None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_tag(self):
        tag = None
        child_node = LeafNode("p", "Nope!", None)
        parent_node = ParentNode(tag, [], None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()