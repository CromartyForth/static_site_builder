import unittest
from markdownToHTMLNode import markdown_to_html_node

class TestTextNode(unittest.TestCase):
  

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    
    def test_quotes(self):
        md = """
> "This is **the** winter of our discontent."
> "Seize **the** day boys!"
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><quote>"This is <b>the</b> winter of our discontent."\n"Seize <b>the</b> day boys!"</quote></div>',
        )

    
    def test_headings(self):
        md = """
# This is a h1 heading

## This is a h2 heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>This is a h1 heading</h1><h2>This is a h2 heading</h2></div>',
        )

    def test_unorderedlist(self):
        md = """
- I really
- hate writing
- in raw html
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>I really</li><li>hate writing</li><li>in raw html</li></ul></div>',
        )

    def test_orderedlist(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>',
        )