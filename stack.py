def balanced_parentheses(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == '__main__':

    string = input('Enter the string: ')
    print(balanced_parentheses(string))
