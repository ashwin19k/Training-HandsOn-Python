# Parenthesis Validation using exception handling

def valid_parenthesis(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


string1 = "[{(}]"
print(valid_parenthesis(string1))