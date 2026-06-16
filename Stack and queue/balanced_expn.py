from stack_array import ArrayStack

def is_balanced(expression):
    s = ArrayStack(len(expression))   # Capacity = length of input

    matching_pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:

        if char in "([{":
            # Opening bracket → push to stack
            s.push(char)

        elif char in ")]}":
            # Closing bracket → check stack
            if s.is_empty():
                return False
            
            top = s.pop()

            # If the popped item does not match the expected opening bracket
            if matching_pair[char] != top:
                return False

    # After processing all characters, stack must be empty
    return s.is_empty()



expr = "{ [ ( A + B ) * C ] - D "
print("Expression:", expr)
print("Are the brackets balanced?" , is_balanced(expr))
