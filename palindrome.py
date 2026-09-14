word = input('Enter a word: ').lower()
is_palindrome = True

# if word != word.lower():
#     word = input('Please enter a word in lowercase: ')
# else:
#     is_palindrome = True

for index in range(len(word) // 2):
    first_letter = word[index]
    last_letter = word[len(word) - index - 1]

    if first_letter != last_letter:
        is_palindrome = False
        break

if is_palindrome:
    print('The word is a palindrome.')
else:
    print('The word is not a palindrome.')
