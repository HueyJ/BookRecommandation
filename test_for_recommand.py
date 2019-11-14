# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019
import unittest

from recommand_30804299 import load_documents, choice


class TestForRecommand(unittest.TestCase):
    def test_choice(self):
        # Term          IDF                 Choice
        # frankenstein  2.09861228866811    84-0
        # sherlock      2.09861228866811    1661-0
        # the           0.8458493201727416  pg16328
        # bird          1.1823215567939547  1661-0
        # wallpaper     2.09861228866811    1952-0
        test_docs = load_documents()
        self.assertEqual(choice("frankenstein", test_docs), "84-0")
        self.assertEqual(choice("sherlock", test_docs), "1661-0")
        self.assertEqual(choice("the", test_docs), "pg16328")
        self.assertEqual(choice("bird", test_docs), "1661-0")
        self.assertEqual(choice("wallpaper", test_docs), "1952-0")
        self.assertEqual(choice("faewfadsf", test_docs), None)


if __name__ == "__main__":
    unittest.main()
