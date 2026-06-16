from stack_array import ArrayStack
#Evaluating postfix expression
def evaluate_postfix(expr):
    s = ArrayStack(10)  

    for token in expr.split():
        if token.isdigit():
            s.push(int(token))
        else:
            op2 = s.pop()
            op1 = s.pop()

            if token == '+':
                s.push(op1 + op2)
            elif token == '-':
                s.push(op1 - op2)
            elif token == '*':
                s.push(op1 * op2)
            elif token == '/':
                s.push(op1 / op2)

    return s.pop()

print(evaluate_postfix("5 6 +"))
