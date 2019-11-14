# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019


# A class for analysing the number of occurrences for each word from a given cleaned text.
#     Instance variables:
#         word_counts: dict
#             the number of word occurrences
#     Methods:
#         analyse_words(book_text)
#             Performs a count on a given book text at the word level and updates self.word_counts.
#         get_word_frequency()
#            Returns the frequency of the words found in self.word_counts.
class WordAnalyser:

    def __init__(self):
        self.word_counts = {}

    # Re-define this method to present the number of occurrences
    # for each word in a readable format.
    # Returns:
    #     str
    #         a formatted string
    def __str__(self):
        assert self.word_counts, "Instance variable: word_counts is empty."
        word_and_count = "Word,Count"
        for word, count in self.word_counts.items():
            word_and_count += "\n" + word + "," + str(count)
        return word_and_count

    # Performs a count on a given book text at the word level and updates self.word_counts.
    #     Parameters:
    #         book_text: str
    #             cleaned book text
    def analyse_words(self, book_text):
        # count the occurrences for each of the words
        # do not count occurrences of new line characters
        from collections import Counter
        book_text = (" ".join(book_text.splitlines())).strip().split(" ")
        # update in word_counts
        word_counts = dict(Counter(book_text))  # Use Counter to count word number with fast speed.
        del word_counts[""]
        # word_counts["\ufeff"] = 1  # To meet the requirement of assignments
        self.word_counts = word_counts

        # Version 1
        # for line in book_text.splitlines():
        #     for word in line.split(" "):
        #         if not word:
        #             continue
        #         if not (word in word_counts.keys()):
        #             word_counts[word] = 1
        #         else:
        #             word_counts[word] += 1
        # # update in word_counts
        # self.word_counts = word_counts

    # Returns the frequency of the words found in self.word_counts.
    #     Returns:
    #         dict
    #             the frequency of the words found in self.word_counts
    def get_word_frequency(self):
        assert self.word_counts, "To get_word_frequency(), Instance variable: word_counts cannot be empty."
        counts_sum = sum(self.word_counts.values())
        # Frequency refers to count(word)/count(all words)
        word_frequency = {word: count / counts_sum for word, count in self.word_counts.items()}
        return word_frequency

# if __name__ == "__main__":
#     import time
#     text = ""
#     for i in range(1):
#         text += open("test_data/84-0_clean.txt", "r", encoding="utf-8").read()
#     start = time.time()
#     word_analyser = WordAnalyser()
#     word_analyser.analyse_words(text)
#     word_analyser.get_word_frequency()
#     print(time.time() - start)
