from collections import deque


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using deque.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if string is palindrome, False otherwise
    """
    # Convert to lowercase and remove spaces
    cleaned_string = ''.join(s.lower().split())
    
    # Create deque and add all characters
    char_deque = deque(cleaned_string)
    
    # Compare characters from both ends
    while len(char_deque) > 1:
        # Remove and compare first and last characters
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    """
    Main function to test palindrome checker with various examples.
    """
    test_strings = [
        "A man a plan a canal Panama",
        "race a car",
        "Was it a car or a cat I saw",
        "Madam",
        "No x in Nixon",
        "Mr. Owl ate my metal worm",
        "12321",
        "hello"
    ]
    
    print("Palindrome Checker")
    print("-" * 30)
    
    for test_string in test_strings:
        result = is_palindrome(test_string)
        print(f"'{test_string}' is palindrome? -> {result}")



if __name__ == "__main__":
    main()
