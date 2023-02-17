# Matīss Lakševics (221RDB363), DITF, IT, 4.grupa, 1.kurss
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[0].position+1

def main():
    userInput = input()
    if userInput == 'F':
        fileName = input()
        textFile = open(fileName)
        text = textFile.read()
        if IOError:
            print('File name error!')
        return
    elif userInput == 'I':
        textInput = input()
    else:
        print('Input error!')
        return

    mismatch = find_mismatch(textInput)
    print(mismatch)

if __name__ == "__main__":
    main()
