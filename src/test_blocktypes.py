import unittest
from blocktypes import BlockType, block_to_block_type

class testBlockToBlockType(unittest.TestCase):
    # these test have no indents

    def text_block_type_heading(self):
        md="""# This is a heading!"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.HEADING)
    
    def text_block_type_not_heading(self):
        md="""####### This is not a heading!"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)


    def test_block_type_code(self):
        md = """```
if (lines[0].startswith("```") and lines[-1].startswith("```")):
return BlockType.CODE
```"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.CODE)
    
    def test_block_type_not_code(self):
        md = """```
if (lines[0].startswith("```") and lines[-1].startswith("```")):
return BlockType.CODE
***"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    
    def test_block_type_quote(self):
        md="""> Quote
> Quoty quote
> Quoty mc Quoteface"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_type_not_quote(self):
        md="""> Quote
> Quoty quote
Look a rogue line!
> Quoty mc Quoteface"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_type_unordered_list(self):
        md = """- apples
- bananas
- lemons
- donkeys"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.UNORDEREDLIST)
    
    def test_block_type_not_unordered_list(self):
        md = """- apples
- bananas
+ lemons
- donkeys"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_type_ordered_list(self):
        md = """1. apples
2. bananas
3. lemons
4. donkeys"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.ORDEREDLIST)
    
    def test_block_type_not_unordered_list(self):
        md = """1. apples
2. bananas
4. lemons
5. donkeys"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)


    def test_block_type_paragraph(self):
        md = """So this is just a paragraph
This is a new line in that paragraph
Done for emphsiss.
"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)


    