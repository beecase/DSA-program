from stack_array import ArrayStack

def infix_to_postfix(expression):
    """
    Converts an infix expression to a postfix expression.
    """

    # Defining  operator precedence
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}

    output = []
    operator_stack = ArrayStack(10) 
    tokens = expression.split()
    print(tokens)

    for token in tokens:

        if token.isalnum():
            # Token is a number or variable
            output.append(token)

        elif token == '(':
            # Token is a left parenthesis
            operator_stack.push(token)

        elif token == ')':
            # Popping operators until '(' is found
            while (not operator_stack.is_empty() and operator_stack.peek() != '('):
                output.append(operator_stack.pop())
            operator_stack.pop()    # discard '('

        else:
            # Token is an operator
            while (not operator_stack.is_empty() 
                   and operator_stack.peek() != '(' 
                   and precedence.get(operator_stack.peek(), 0) >= precedence.get(token, 0)):
                output.append(operator_stack.pop())

            operator_stack.push(token)

    # Popping remaining operators
    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return "".join(output)



infix_expr = "( A + B ) * C - ( D / E )"
postfix_expr = infix_to_postfix(infix_expr)

print(f"\nInfix: {infix_expr}")
print(f"\nPostfix: {postfix_expr}")
