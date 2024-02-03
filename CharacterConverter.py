# you'll have to install pypinyin first for it to work
# pip install pypinyin

from pypinyin import pinyin, Style
from functools import cmp_to_key

#converting characters to pinyin
def convert_to_pinyin(chinese_text):
    return ''.join([word[0] for word in pinyin(chinese_text, style=Style.NORMAL, strict=False)])

#comparing pinyin
def compare_pinyin(item1, item2):
    pinyin1 = convert_to_pinyin(item1)
    pinyin2 = convert_to_pinyin(item2)
    return (pinyin1 > pinyin2) - (pinyin1 < pinyin2)

def sort_chinese_strings(chinese_strings):
    return sorted(chinese_strings, key=cmp_to_key(compare_pinyin))


chinese_strings = []

# Read from a txt file and put it into the a unsorted list
file_path = "SongList.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        chinese_strings.append(line.strip())

sorted_strings = sort_chinese_strings(chinese_strings)

# with the sorted list write the results into a new txt file
file_path = "SortedList.txt"

with open(file_path, "a", encoding="utf-8") as file:
    for string in sorted_strings:
        file.write(string + '\n')