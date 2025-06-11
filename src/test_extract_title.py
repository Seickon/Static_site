import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_normal(self):
        markdown = "# Kreativer Tietel"
        kontrolle = "Kreativer Tietel"
        self.assertEqual(extract_title(markdown), kontrolle)

    def test_no_header(self):
        markdown = "## Kreativer Tietel"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_tailing_whitespace(self):
        markdown = "# Kreativer Tietel    "
        kontrolle = "Kreativer Tietel"
        self.assertEqual(extract_title(markdown), kontrolle)

    def test_leading_whitespace(self):
        markdown = "#      Kreativer Tietel"
        kontrolle = "Kreativer Tietel"
        self.assertEqual(extract_title(markdown), kontrolle)