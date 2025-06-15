import nltk
from nltk.corpus import words
import random

# Load the list of words from the NLTK corpus
all_words = words.words()

filtered_words = [
    word.lower()
    for word in all_words
    if word.isalpha() and len(word) >= 5 and len(word) <= 8
]

secret_word = random.choice(filtered_words)

# Display "_" for each letter in the secret word
for letter in secret_word:
    print("_", end=" ")
print()  # New line after displaying the underscores



