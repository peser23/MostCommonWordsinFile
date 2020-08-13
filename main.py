# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string

def get_common_words():
    print(f'Hi, Praveen')  # Press Ctrl+F8 to toggle the breakpoint.
    filename = get_file_name()
    print("filename is: " + filename)
    handle = open(filename)
    count = dict()
    for line in handle:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1

    temp = list()
    for k, v in count.items():
        tempt = (v, k)
        temp.append(tempt)

    temp = sorted(temp, reverse=True)
    for v,k in temp[0:5]:
        print(k,  v)


def get_file_name():
    filename = input("Enter File Name: ")
    return filename


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_common_words()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
