def check_brackets(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"

# Тестові приклади
test_expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expression in test_expressions:
    result = check_brackets(expression)
    print(f"{expression}: {result}")