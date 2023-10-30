example_text1 = "potop"
example_text2 = "test"

def checkIsPalindrome(text):
    """
       Checks whether the given argument is a palindrome.

        text
            passed string value to check
        True or False value is returned
    """
    reverseTxt = text[::-1]
    if reverseTxt == text:
        return True
    return False

checkIsPalindrome(example_text1)