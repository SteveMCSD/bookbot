def get_word_count(document):
    return len(document.split())

def char_count(document):
    doc = document.lower()
    chars = {}
    for char in doc:
        if char not in chars:
            chars[char] = 1
        else: chars[char] += 1
    return chars

def get_report(word_count, char_counts, book):
    new_list = []
    report_01 = f"============ BOOKBOT ============\nAnalyzing book found at {book}...\n----------- Word Count ----------\n"
    report_02 = f"Found {word_count} total words\n"
    report_03 = "--------- Character Count -------\n"
    report_04 = ""
    report_05 = "============= END ==============="

    for char, count in char_counts.items():
        if char.isalpha():
            new_list.append({"char": char, "num": count})
    new_list.sort(reverse=True, key=sort_on)
    report_04 += "\n".join([f"{item['char']}: {item['num']}" for item in new_list]) + "\n"
    return report_01 + report_02 + report_03 + report_04 + report_05

def sort_on(items):
    return items["num"]