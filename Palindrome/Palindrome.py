
def isPalindrome(str, start_index):
    if start_index >= len(str) - 1:
        return True

    elif str[start_index] != str[len(str) - 1 - start_index]:
        return False
    
    else:
        return isPalindrome(str, start_index+1)



print(isPalindrome('abcdefghijihgfedca', 0))
