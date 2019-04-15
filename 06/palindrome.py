def palindrome(palindrome_string):
    is_palindrome = False
    for i in range(0,len(palindrome_string)):
        if palindrome_string[i] != palindrome_string[len(palindrome_string)-i-1]:
            break
    else:
        is_palindrome = True
    return is_palindrome
