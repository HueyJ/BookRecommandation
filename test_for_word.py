# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 19 Sep 2019
import unittest

from word_30804299 import WordAnalyser


class TestForWordAnalyser(unittest.TestCase):
    def test_word_analyser(self):
        from preprocessor_30804299 import Preprocessor
        book_titles = [
            "84-0",
            "11-0",
            "1342-0",
            "1661-0",
            "1952-0",
            "pg16328",
        ]
        p = Preprocessor()
        word_analyser = WordAnalyser()
        for book_title in book_titles:
            p.read_text(book_title + ".txt")
            p.clean()
            book_text = p.book_content
            word_analyser.analyse_words(book_text)
            self.assertTrue("" not in word_analyser.word_counts.keys())
            self.assertTrue("\n" not in word_analyser.word_counts.keys())

            word_counts = {}
            with open("test_data/" + book_title + "_counts.txt", "r", encoding="utf_8_sig") as f:
                for line in f:
                    word_count = line[:-1].split(":")
                    word_counts[word_count[0]] = int(word_count[1])
            self.assertDictEqual(word_counts, word_analyser.word_counts)

            word_freqs = {}
            with open("test_data/" + book_title + "_freq.txt", "r", encoding="utf_8_sig") as f:
                for item in f.read()[1:-1].split(", "):
                    word_freq = item.split(": ")
                    word_freqs[word_freq[0].strip("'")] = float(word_freq[1])
            self.assertDictEqual(word_freqs, word_analyser.get_word_frequency())


if __name__ == "__main__":
    unittest.main()
