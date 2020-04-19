import unittest
from javadoc2html import *
import os


class Test(unittest.TestCase):

    main()
    handler = Java_handler("test")
    files = handler.get_files_from_dir()
    converter = Converter(files, "test")
    converter.create_html_files()

    def test_project_exist(self):
        self.assertEqual(os.path.exists("test_html"), True)

    def test_exist_interface(self):
        self.assertEqual(os.path.exists(
            os.path.join("test_html", "Game.html")), True)

    def test_exist_class(self):
        self.assertEqual(os.path.exists(
             os.path.join("test_html", "ChatManager.html")), True)

    def test_parse_inter(self):
        self.assertEqual(len(self.handler.files[1].interfaces[0].fields), 1)

    def test_parse_inter_second(self):
        self.assertEqual(len(self.handler.files[1].interfaces[0].methods), 3)

    def test_parse_class(self):
        self.assertEqual(len(self.handler.files[0].classes[0].fields), 13)

    def test_parse_class_second(self):
        self.assertEqual(len(self.handler.files[0].classes[0].methods), 20)


if __name__ == '__main__':
    unittest.main()
