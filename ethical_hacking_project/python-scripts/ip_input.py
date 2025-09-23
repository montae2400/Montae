# ip_input.py
# This is just the name of the file. It doesn’t affect the code.
# (Good practice: put the filename at the top so you know what file you’re looking at.)

"""Prompt for an IP and validate basic IPv4 format."""
# This is a "docstring."
# It’s a short description of what this program does.
# It helps humans understand the purpose of the file.

import re
# This imports Python’s "re" module.
# "re" = regular expressions (a tool for checking if text matches a certain pattern).
# Example: you can check if text looks like "123.45.6.7".

# --------------------------
# Function #1
# --------------------------
def is_basic_ipv4_format(ip_address: str) -> bool:
    # "def" means we are defining a function (a reusable block of code).
    # The function’s name is is_basic_ipv4_format.
    # It takes one input: ip_address (a string the user typed).
    # ": str" is a hint that says "this should be a string."
    # "-> bool" means this function gives back True or False.

    pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    # "pattern" is a variable that stores a rule for matching text.
    # This rule is written as a REGEX (regular expression).
    #
    # Let's break it down:
    #   ^         → start of the string (so it won’t match extra stuff before it)
    #   \d{1,3}   → 1 to 3 digits (0–9). So this could be "1", "12", "123".
    #   (\.\d{1,3}){3} → a dot plus 1–3 digits, repeated exactly 3 times.
    #   $         → end of the string.
    #
    # Together: "number.number.number.number"
    # Example: "192.168.0.1"

    return bool(re.match(pattern, ip_address))
    # "re.match" tries to apply the pattern to the ip_address.
    # If it fits the rule, it returns a "Match" object (like a success ticket).
    # If not, it returns None.
    #
    # "bool(...)" converts that result into True (if it matched) or False (if not).
    # So this line gives back True if the input looks like an IPv4, otherwise False.

# --------------------------
# Function #2 (main program)
# --------------------------
def main():
    # "main()" is the function that runs the program steps.

    user_input_ip = input("Enter a target IP (lab only): ").strip()
    # "input(...)" shows text to the user and waits for them to type something.
    # Example: the user types "192.168.0.1" and presses Enter.
    # The result is always a string.
    #
    # ".strip()" removes extra spaces before or after what they typed.
    # Example: " 192.168.0.1 " becomes "192.168.0.1".
    #
    # That cleaned-up result is saved in the variable user_input_ip.

    if is_basic_ipv4_format(user_input_ip):
        # This calls our first function (is_basic_ipv4_format).
        # It checks if what the user typed matches the IPv4 pattern.
        # If True → run the next indented block.
        # If False → skip to the "else" block.

        print(f"You entered IP: {user_input_ip}")
        # If the check passed, print a message back to the user.
        # "f-string" → lets us put the variable directly into the text.
        # Example: if user_input_ip is "192.168.0.1"
        # the message will be: "You entered IP: 192.168.0.1"

    else:
        # If the pattern check was False, we land here.

        print("That doesn't look like a valid IPv4 address.")
        # Print a message telling the user it’s not a valid format.

# --------------------------
# Safety check
# --------------------------
if __name__ == '__main__':
    main()
# "__name__" is a special built-in variable in Python.
# - If we run this file directly (python ip_input.py), __name__ == "__main__".
#   → So the program calls main().
# - If another file imports this file, __name__ will NOT be "__main__".
#   → main() won’t run automatically.
# This makes the file reusable in other programs.
