example_text1 = "potop"
example_text2 = "test"

def checkIsPalindrome(text):
    reverseTxt = text[::-1]
    if reverseTxt == text:
        return True
    return False

checkIsPalindrome(example_text2)