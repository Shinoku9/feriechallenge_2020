import webbrowser

sentence = input("Enter your sentence: ").replace(" ","")
print(sentence)

def isPalindrome(sentence):
    return sentence == sentence[::-1]

ans = isPalindrome(sentence)

webbrowser.open('https://poocoo.pl/scrabble-slowa-z-liter/hardcoder', new=2)

if ans:
    print("Yes")
else:
    print("No")
