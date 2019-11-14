# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019
import unittest


def calculate_idf(book_titles, term):
    from preprocessor_30804299 import Preprocessor
    from word_30804299 import WordAnalyser
    from idf_30804299 import IDFAnalyser
    p = Preprocessor()
    wa = WordAnalyser()
    ia = IDFAnalyser()
    ts = []
    tfs = []
    for t in book_titles:
        p.read_text(t + ".txt")
        p.clean()
        ts.append(p.book_content)
    for t in ts:
        wa.analyse_words(t)
        tfs.append(wa.get_word_frequency())
    i = 0
    for tf in tfs:
        ia.load_frequency(tf, book_titles[i])
        i += 1
    idf = ia.get_IDF(term)
    return idf


class TestForIDFAnalyser(unittest.TestCase):
    def test_idf_analyser(self):
        from math import log
        book_titles = [
            "84-0",
            "11-0",
            "1342-0",
            "1661-0",
            "1952-0",
            "pg16328",
        ]
        terms = [
            "frankenstein",
            "sherlock",
            "the",
            "bird",
            "wallpaper",
        ]
        idfs = [
            log(6/2)+1,  # 2.09861228866811
            log(6/2)+1,  # 2.09861228866811
            log(6/7)+1,  # 0.8458493201727416
            log(6/5)+1,  # 1.1823215567939547
            log(6/2)+1,  # 2.09861228866811
        ]
        i = 0
        # Term          IDF                 Choice
        # frankenstein  2.09861228866811    84-0
        # sherlock      2.09861228866811    1661-0
        # the           0.8458493201727416  pg16328
        # bird          1.1823215567939547  1661-0
        # wallpaper     2.09861228866811    1952-0
        for term in terms:
            idf = calculate_idf(book_titles, term.lower())
            self.assertEqual(idf, idfs[i])
            i += 1
            print("\n------------------------------------------------------\n" +
                  term + ": " + str(idf) +
                  "\n------------------------------------------------------\n")


if __name__ == "__main__":
    unittest.main()
