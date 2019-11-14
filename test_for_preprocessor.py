# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 19 Sep 2019
import unittest

from preprocessor_30804299 import Preprocessor


class TestForPreprocessor(unittest.TestCase):
    def test_preprocessor(self):
        p = Preprocessor()
        self.assertFalse(p.book_content)
        book_titles = [
            "84-0",
            "11-0",
            "1342-0",
            "1661-0",
            "1952-0",
            # "pg16328",  # Because of special character "\xa0" which is not utf8, this test won't pass.
        ]
        print("\n")
        for book_title in book_titles:
            print(book_title)
            p.read_text(book_title + ".txt")
            p.clean()
            with open("test_data/" + book_title + "_clean.txt", "r", encoding="utf_8_sig") as f:
                actual = p.book_content
                expected = f.read()
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
