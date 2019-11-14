# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019
from math import log

from pandas import DataFrame


# A class that implementing Inverse Document Frequency (IDF) calculations.
#     Instance variables:
#         data: pandas.DataFrame
#             contain loaded term frequencies as rows
class IDFAnalyser:

    def __init__(self):
        self.data = DataFrame()

    # Loads the frequency of a cleaned text into data with a title that corresponds to the text
    # the frequency was generated from.
    #     Parameters:
    #         book_frequency: dict
    #             the frequency of a cleaned text
    #         book_title: list
    #              a title or titles that corresponds to the text the frequency was generated from
    def load_frequency(self, book_frequency, book_title):
        # If loaded a single book, do casting to meet the parameter types of data frame constructor.
        if type(book_title) != list:
            book_title = [book_title]
            book_frequency = {word: [frequency] for word, frequency in book_frequency.items()}
        df = DataFrame(book_frequency, index=book_title)
        # Reindex self.data according to the new data frame constructed
        self.data = self.data.reindex(columns=set(df.keys()).union(set(self.data.keys())))
        # Then append the new df to self.data
        self.data = self.data.append(df)
        # Replace all nan with 0
        self.data = self.data.fillna(0)

    # Obtains the IDF for the term provided and the documents loaded into data.
    #     Parameters:
    #         term: str
    #             term to calculate IDF
    #     Returns:
    #         float
    #             IDF = log(D / (1 + N))
    #             Where D is the number of documents in the corpus,
    #             and N is the count of the number of documents containing the term.
    def get_IDF(self, term):
        d = None
        n = None
        try:
            d = len(self.data.index)
            n = len(self.data.loc[self.data[term] > 0])
        except KeyError:
            print("\n-----------------------\nTerm: \"" + term + "\" does not exist.\n-----------------------\n")
            n = 0
        finally:
            idf = log(d / (1 + n)) + 1
        return idf
