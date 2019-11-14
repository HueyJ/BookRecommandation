# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019


# A class performs the basic pre-processing on each input text.
#     Instance variables:
#         book_content: str
#             the text of a book
#     Methods:
#         clean()
#             Removes undesirable characters from text present in book_content
#             and stores it back in self.book_content.
#         read_text(text_name)
#             Reads the content of the file into the string instance
#             variable of this class.
class Preprocessor:

    def __init__(self):
        self.book_content = ""

    # Re-define this method to present content of book_content.
    #     Returns:
    #         str
    #             the content of self.book_content
    def __str__(self):
        assert self.book_content, "Instance variable: book_content is empty."
        return self.book_content

    # Removes undesirable characters from text present in book_content
    # and stores it back in self.book_content.
    #     Returns:
    #         int
    #             int 1 if no text exists in self.book_content
    #         None
    #             None if text exists in self.book_content
    def clean(self):
        assert self.book_content, "To clean(), Instance variable: book_content cannot be empty."
        if not self.book_content:
            return 1

        from string import ascii_letters, whitespace, digits
        encoding = "utf8"
        # Anything that is not a letter or a number or white-space
        to_remove = ""
        for ch in self.book_content:
            if ch not in (to_remove + ascii_letters + whitespace + digits):
                to_remove += ch
        to_remove = to_remove.replace("\xa0", "")
        to_remove = bytes(to_remove.replace("-", "").replace("_", ""), encoding=encoding)
        self.book_content = bytes(self.book_content, encoding=encoding)
        # must be removed from the text.
        self.book_content = self.book_content.translate(None, to_remove)
        # Hyphenated words such as "off-campus" should become "off campus".
        self.book_content = b" ".join(self.book_content.split(b"-"))
        self.book_content = b" ".join(self.book_content.split(b"_"))
        self.book_content = b" ".join(self.book_content.split(b"\xa0"))  # Special whitespaces which is not utf8
        # Characters should be made lowercase if they can be.
        self.book_content = self.book_content.lower()
        self.book_content = str(self.book_content, encoding=encoding)

        # Version 1
        # temp_text = ""
        # for c in self.book_content:
        #     if c in "-_":
        #         temp_text += " "
        #     elif c in ascii_letters + whitespace + digits:
        #         temp_text += c.lower()
        #     else:
        #         continue
        # self.book_content = temp_text
        # Version 2
        # self.book_content = self.book_content
        # for p in punctuation + "‘’“”—":
        #     if p in "-_":
        #         join = " "
        #     else:
        #         join = ""
        #     self.book_content = join.join(self.book_content.split(p))
        # self.book_content = self.book_content.lower()
        # Version 4
        # encoding = "utf8"
        # self.book_content = bytes(self.book_content, encoding=encoding)
        # for p in punctuation + "‘’“”—":
        #     if p in "-_":
        #         join = " "
        #     else:
        #         join = ""
        #     join = bytes(join, encoding=encoding)
        #     p = bytes(p, encoding=encoding)
        #     self.book_content = join.join(self.book_content.split(p))
        # self.book_content = str(self.book_content, encoding="utf8").lower()

    # Reads the content of the file into self.book_content
    #     Parameters:
    #         text_name: str
    #             the name of a file
    def read_text(self, text_name):
        with open(text_name, "r", encoding="utf8") as file:
            self.book_content = file.read()


# if __name__ == "__main__":
#     preprocessor = Preprocessor()
#     for i in range(1):
#         preprocessor.read_text("84-0.txt")
#     from time import time
#     start = time()
#     preprocessor.clean()
#     print(time() - start)
#     with open("test_data/84-0_clean.txt", "r", encoding="utf_8_sig") as f:
#         t1 = ("".join(preprocessor.book_content.split("x"))).split("\n")
#         t2 = f.read().split("\n")
#         i = 0
#         for l1 in t1:
#             l1 = l1.strip()
#             l2 = t2[i].strip()
#             if l1 != l2:
#                 print("" + str(i))
#                 print("t1: " + repr(l1))
#                 print("t2: " + repr(l2))
#             i += 1
