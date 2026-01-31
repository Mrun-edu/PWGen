#!/usr/bin/env python3
# Password Generator: Converts each character to the corresponding digit of pi
# based on the character's position in the alphabet

import argparse
import sys

alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# First 26 digits of pi (after the decimal point: 3.14159265358979323846264338327...)    
pi = ["3", "1", "4", "1", "5", "9", "2", "6", "5", "3", "5", "8", "9", "7", "9", "3", "2", "3", "8", "4", "6", "2", "6", "4", "3", "3"]

def generate_password(name):
    """
    Converts each character in the name to the corresponding digit of pi.
    For example: 'a' (index 0) -> pi[0] = '3', 'e' (index 4) -> pi[4] = '5'
    """
    password = ""
    name = name.lower()  # Convert to lowercase for consistency
    
    for char in name:
        if char in alfabe:
            # Find the index of the character in the alphabet
            index = alfabe.index(char)
            # Use that index to get the corresponding digit from pi
            password += pi[index]
        else:
            # If character is not in alphabet (e.g., space, number), skip it
            password += char
    
    return password

def show_mapping(name):
    """Display the character-to-digit mapping for the given name."""
    print("\nCharacter mapping:")
    for char in name.lower():
        if char in alfabe:
            index = alfabe.index(char)
            print(f"  '{char}' (index {index}) -> '{pi[index]}'")

def validate_input(name):
    """
    Validate that the input only contains allowed characters.
    Allowed: letters, spaces, numbers, and special characters: @ . ,
    Returns: (is_valid, error_message)
    """
    allowed_special_chars = {'@', '.', ',', ' '}
    
    for char in name:
        # Check if character is not a letter, digit, or allowed special character
        if not (char.isalpha() or char.isdigit() or char in allowed_special_chars):
            return False, f"Error: Invalid character '{char}' found. Only letters, numbers, spaces, and @ . , are allowed."
    
    return True, ""


def main():
    """Main function to handle CLI arguments and interactive mode."""
    parser = argparse.ArgumentParser(
        description='Generate passwords by converting characters to pi digits based on alphabet position.',
        epilog='If no arguments are provided, the script runs in interactive mode.'
    )
    parser.add_argument(
        'name',
        nargs='?',
        help='Name to convert to password (only English alphabet)'
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Only output the password without additional information'
    )
    parser.add_argument(
        '-m', '--show-mapping',
        action='store_true',
        help='Show character-to-digit mapping'
    )
    
    args = parser.parse_args()
    
    # CLI mode: if name is provided as argument
    if args.name is not None:
        input_name = args.name.strip()
        
        # Validate input is not empty
        if not input_name:
            print("Error: Name cannot be empty or whitespace only.", file=sys.stderr)
            sys.exit(1)
        
        # Validate input characters
        is_valid, error_msg = validate_input(input_name)
        if not is_valid:
            print(error_msg, file=sys.stderr)
            sys.exit(1)
        
        password = generate_password(input_name)
        
        if args.quiet:
            # Quiet mode: only print the password
            print(password)
        else:
            # Normal CLI output
            print(f"Original name: {input_name}")
            print(f"Generated password: {password}")
            
            if args.show_mapping:
                show_mapping(input_name)
    
    # Interactive mode: if no name is provided
    else:
        while True:
            input_name = input("Enter a name or quote exp.(Go0dp@ssw0rd.): ").strip()
            
            # Validate input is not empty
            if not input_name:
                print("Error: Name cannot be empty. Please try again.")
                continue
            
            # Validate input characters
            is_valid, error_msg = validate_input(input_name)
            if not is_valid:
                print(error_msg)
                continue
            
            break
        
        password = generate_password(input_name)
        
        # Always show mapping in interactive mode
        show_mapping(input_name)

        print(f"\nOriginal name: {input_name}")
        print(f"Generated password: {password}")
        
        # Always show mapping in interactive mode
        
if __name__ == "__main__":
    main()
