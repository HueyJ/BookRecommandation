
if __name__ == "__main__":
    book_titles = [
        "84-0",
        "11-0",
        "1342-0",
        "1661-0",
        "1952-0",
        "pg16328",
    ]
    for book_title in book_titles:
        word_counts = {}
        with open("test_data/" + book_title + "_counts.txt", "r", encoding="utf_8") as f:
            for line in f:
                word_count = line[:-1].split(":")
                word_counts[word_count[0]] = int(word_count[1])
            print(word_counts)