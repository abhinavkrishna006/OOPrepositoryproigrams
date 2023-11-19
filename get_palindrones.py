def is_palindrome(s):
    return s == s[::-1]

def get_palindromes(input_string):
    # Split the string into words
    words = input_string.split()

    # Filter palindromes from the list of words
    palindromes = [word for word in words if is_palindrome(word)]

    return palindromes

# Example usage:
input_str = "level radar hello kayak world civic"
palindrome_list = get_palindromes(input_str)
print("Palindromes:", palindrome_list)
