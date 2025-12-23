word = input("Enter a word or phrase: ")
cleaned = word.replace(" ", "").lower()
reversed_text = ""
for char in cleaned:
        reversed_text = char + reversed_text 
if cleaned == reversed_text:
        print("It is a palindrome.")
else:
        print("It is not a palindrome.")
