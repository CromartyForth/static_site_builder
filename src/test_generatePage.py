import unittest
from generatePage import generate_page

class testGeneratePage(unittest.TestCase):

    def test_generate_page(self):
        from_path = "../content/index.md"
        dest_path = "there"
        template_path = "../template.html"
        expected = "Generating page from here to there using this"
        result = generate_page(from_path, template_path, dest_path)
        self.assertEqual(expected, result)