<div align="center">
  <h1>FCIS Arabic Stemmer</h1>
  <p>
    <strong>A Python class for stemming Arabic words</strong>
  </p>
  <p>
    A Python class that implements various stemming methods to reduce Arabic words to their root or base form.
  </p>
  <img src="[https://www.example.com/stemming.png](https://miro.medium.com/v2/resize:fit:828/format:webp/1*jawjUxVmzZFZm3i_qgGpXg.png)" alt="Stemming" width="500px">
</div>

## Table of Contents
- [Usage](#usage)
- [Example](#example)
- [Stemming Rules](#stemming-rules)
- [Contributing](#contributing)
- [License](#license)

## Usage
1. Ensure you have Python installed on your system.
2. Clone the repository or download the `fcis_steamer.py` file.

## Example
```python
from fcis_steamer import FcisStemmer

def main():
    s = FcisStemmer()
    sentence = input("Enter a sentence: ")

    stemmed_sentence = ""
    for word in sentence.split():
        stemmed_word = s.stem(word)
        stemmed_sentence += stemmed_word + " "

    print("Original sentence: " + sentence)
    print("Stemmed sentence: " + stemmed_sentence.strip())

if __name__ == "__main__":
    main()

## Stemming Rules

The `FcisStemmer` class implements the following stemming rules:

- Removal of common "alif lam" prefixes.
- Replacement of specific words with "الله".
- Removal of certain suffixes like plurals and definite articles.
- Modifying verb forms to their root or base form.
- Conversion of future tense to past tense.
- And more.

Please refer to the source code for a detailed understanding of the implemented rules.
