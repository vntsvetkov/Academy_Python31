from module import *


def check_brackets(text: str) -> bool:

    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    stack = Stack()

    for symbol in text:
        if symbol in brackets.keys():
            stack.push(symbol)
        elif not stack.is_empty() and symbol == brackets[stack.peek()]:
            stack.pop()
        else:
            return False

    return stack.is_empty()


def main():
    print(check_brackets("[{()}]"))  # True
    print(check_brackets("([(]}"))  # False
    print(check_brackets("{]()[]"))  # False
    print(check_brackets(""))  # True

    expression = "0-2-6*(0-3+9-7*2)+(0-5)-1"

    postfix_exp = "2 6 3 9 + 7 2 * - * - 5 + 1 -"




if __name__ == "__main__":
    main()