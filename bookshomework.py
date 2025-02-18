import string
import requests

def count_unique_words(url):
    """Downloads a book from a URL and counts the unique words."""
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error downloading the book from {url}")
        return 0

    text = response.text
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # Split text into words
    words = text.split()

    # Get unique words
    unique_words = set(words)

    return len(unique_words)

# File paths (Replace with actual paths)
book1_url = "https://www.gutenberg.org/cache/epub/98/pg98.txt"  # A Tale of Two Cities - Charles Dickens
book2_url = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"  # Replace with the actual filename

# Count unique words
unique_words_book1 = count_unique_words(book1_url)
unique_words_book2 = count_unique_words(book2_url)

# Compare results
if unique_words_book1 > unique_words_book2:
    print(f"Book 1 (A Tale of Two Cities) has more unique words: {unique_words_book1} vs {unique_words_book2}")
elif unique_words_book1 < unique_words_book2:
    print(f"Book 2 (Moby-Dick) has more unique words: {unique_words_book2} vs {unique_words_book1}")
else:
    print(f"Both books have the same number of unique words: {unique_words_book1}")