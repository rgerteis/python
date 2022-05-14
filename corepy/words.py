"""Retrieve and print words from an URL

    Usage:

        python3 words.py <URL>
"""
import sys
from urllib.request import urlopen

# http://sixty-north.com/c/t.txt

def fetch_words(url):
    """Fetch a list of words from an URL
    
        Args:
            url: The URL of an UTF-8 text document.
        
        Returns:
            A list of strings containing the words 
            from the document
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    """print items one per line
    
        Args:
            items: An iterable list of printable items.
    """
    for item in items:
        print(item)


def main(url):    
    """Print each word from a text document from an URL
    
        Args:
            url: The URL of an UTF-8 text document. 
    
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
