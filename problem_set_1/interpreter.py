def get_expression():
    expression = input("Expression: ")
    expression_formatted = expression.strip()
    return expression_formatted

def calculate_expression(expression_formatted):
    a, operator, b = expression_formatted.split(" ")
    a = float(a)
    b = float(b)
    
    match operator:
        case addition if operator == "+":
            answer = a + b  
        case subtraction if operator == "-":
            answer = a - b
        case multiplaction if operator == "*":
            answer = a * b
        case division if operator == "/":
            answer = a / b
    print(f"{answer:.1f}")            

expression_formatted = get_expression()
calculate_expression(expression_formatted)
