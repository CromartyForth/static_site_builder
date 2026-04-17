import unittest
from generatePage import generate_page, generate_pages_recursive

class testGeneratePage(unittest.TestCase):

    def text_generate_pages_recursive(self):
        dir_path_content = "../content"
        dest_dir_path = "../public"
        template_path = "../template.html"
        expected = "Generating page from here to there using this"
        result = generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
        self.assertEqual(expected, result)