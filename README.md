# Caesar-Cipher
This repository contains my own approach to the "Caesar cipher"

## Usage

- Download this repository
```
git clone https://github.com/phib0/Caesar-Cipher.git
```
- Open ccipher.py to en- or decypher messages.

- Open force.py to bruteforce the translation of a message

> *Python version: Python 3 (**>=3.4**).*

## Functionality

The programm can en- and decypher messages using the Caesar cypher.
It uses only uppercase letters (input gets automatically capitalized), all other characters get ignored.

It can also bruteforce an with the caesar cypher encrypted message to show you the decrypted version.
After triying to decrypt the given message it checks the input to wordlists (english and german) to find matching words. If words match up, the possible translations are printed out on the screen.

## Supported Languages

The dialouge is only supported in english, the word lists are supported in english and german