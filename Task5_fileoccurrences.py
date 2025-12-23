# Ask user for file name
file_name = input("Enter the name of the text file (with .txt extension): ")
word_count = {}
try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    word = ''.join(char for char in word if char.isalnum())  # remove punctuation
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

        print("Word counts (alphabetical order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
