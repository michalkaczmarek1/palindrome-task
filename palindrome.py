example_text1 = "potop"
example_text2 = "test"

def check_is_palindrome(text):
    """
       Checks whether the given argument is a palindrome.

        text
            passed string value to check
        True or False value is returned
    """
    reverse_txt = text[::-1]
    return reverse_txt == text

check_is_palindrome(example_text1)