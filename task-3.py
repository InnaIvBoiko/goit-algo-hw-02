def is_balanced(expression: str) -> str:
    """
    Check if brackets in the expression are balanced using stack data structure.
    
    Args:
        expression (str): String containing brackets and other characters
        
    Returns:
        str: "Balanced" if balanced, "Unbalanced" if not balanced
    """
    # Stack to store opening brackets
    stack: list[str] = []
    
    # Define matching pairs of brackets
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Define opening brackets
    opening_brackets = {'(', '[', '{'}
    
    # Process each character in the expression
    for char in expression:
        # If it's an opening bracket, push to stack
        if char in opening_brackets:
            stack.append(char)
        
        # If it's a closing bracket, check for matching opening bracket
        elif char in bracket_pairs:
            # If stack is empty, no matching opening bracket
            if not stack:
                return "Unbalanced"
            
            # Pop from stack and check if it matches
            last_opening = stack.pop()
            if last_opening != bracket_pairs[char]:
                return "Unbalanced"
    
    # If stack is empty, all brackets are balanced
    # If stack is not empty, there are unmatched opening brackets
    return "Balanced" if not stack else "Unbalanced"


def main():
    """
    Main function to test the bracket balancing program with provided examples.
    """
    # Test cases from the requirements
    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]
    
    print("Bracket Balance Checker")
    print("=" * 30)
    
    # Test each case
    for expression in test_cases:
        result = is_balanced(expression)
        print(f"{expression}: {result}")
    
    print("\n" + "=" * 30)
    
    # Interactive mode for user input
    while True:
        user_input = input("\nEnter expression to check (or 'q' to exit): ").strip()
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        if '(' in user_input or ')' in user_input or \
           '[' in user_input or ']' in user_input or \
           '{' in user_input or '}' in user_input:
            result = is_balanced(user_input)
            print(f"{user_input}: {result}")
        else:
            print("Please enter a valid expression.")


if __name__ == "__main__":
    main()
