# Caesar_Encryption

## Project Overview

This project is designed to explore and understand the principles of encryption and decryption using the Caesar Cipher, one of the simplest and most well-known encryption techniques. By working through this project, you’ll gain hands-on experience with basic cryptography concepts, particularly the Caesar Cipher, which involves shifting the letters of the alphabet by a fixed amount to encode a message.

## Features

1. Encryption: The provided code encrypts a given plain text by shifting each letter by a specified number of positions in the alphabet.
2. Customizable Shift Value: The shift value can be easily modified to see how different shifts affect the encrypted text.

## What Does This Do?

This script takes a plain text string (in this case, "david") and encrypts it using a Caesar Cipher with a shift value of 2. The alphabet is shifted accordingly, and the plain text is transformed into an encrypted string.

For example:

1. Plain Text: david
2. Shift Value: 2
3. Encrypted Text: fcxkf

### Installation

To get started with the Caesar_Encryption project, follow these steps:

1. Clone the Repository:
```bash
git clone https://github.com/skytruong90/Caesar_Encryption.git
```
2. Navigate to the Project Directory:
```bash
cd Caesar_Encryption
```
3. Ensure Python is Installed:
Make sure you have Python 3 installed on your system. You can check by running:
```bash
python3 --version
```

## How to Use

1. Run the Script:
Execute the main.py script from your terminal:
```bash
python3 main.py
```

## Code Explanation

Here’s a brief explanation of the key components of the code:
```bash
import string

plain_text = "david"   # The plain text to be encrypted
shift = 2              # The shift value for the Caesar Cipher
shift %= 26            # Ensures the shift is within the bounds of the alphabet

alphabet = string.ascii_lowercase                 # Defines the alphabet
shifted = alphabet[shift:] + alphabet[:shift]     # Creates the shifted alphabet
table = str.maketrans(alphabet, shifted)          # Creates a translation table

encrypted = plain_text.translate(table)           # Encrypts the plain text using the table
print(encrypted)                                  # Outputs the encrypted text
```
## Key Steps:
1. Shift Calculation: The shift is applied to the alphabet to create a new shifted version.
2. Translation Table: A translation table is created to map each letter in the plain text to its corresponding letter in the shifted alphabet.
3. Encryption: The plain text is then translated into the encrypted text using this table.

This README provides a clear and comprehensive guide to your project, making it easy for others to understand and use your Caesar Cipher implementation.
