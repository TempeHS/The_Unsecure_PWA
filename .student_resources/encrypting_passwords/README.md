# Encrypting & Decrypting Passwords for Safer Storage

__Encryption__: Encryption is the process of encoding plain text or any information so that only authorized people can read it with a corresponding key, protecting confidential data from unauthorized persons.
__Hashing__: Hashing converts any amount of data into a fixed-length hash that cannot be reversed. It is widely used in cryptography. The hash allows us to validate if the input has changed even slightly; if it has, the resulting hash will be different.
__Salting__: In cryptography, a salt is random data used as an additional input to a one-way function that hashes data, such as a password. Salts are used to keep passwords safe while they are being stored.

| Same password | + | Different salt | Same Hashing Function | = | Different output |
| --- | --- | --- | --- | --- | --- |
| "gwW$3zHw" | + | 12gT3 | SHA256 Hash | = | "12d6a36ff1ffba1d24fd3ac0d270315bef3c3de4f6765b8788301f9fd57c084e" |
| "gwW$3zHw" | + | 97xH7 | SHA256 Hash | = | "3820b409b311a3534dcc30bbaa11f0ff5ce064fb476647ede393c8d94937ae15" |

In this article, we will learn the Salted Password Hashing technique. This technique involves converting an algorithm to map data of any size to a fixed length.

## Byte String Explained

To store anything in a computer, you must first encode it, i.e. convert it to bytes. For example:

- If you want to store music, you must first encode it using MP3, WAV, etc.
- If you want to store a picture, you must first encode it using PNG, JPEG, etc.
- If you want to store text, you must first encode it using ASCII, UTF-8, etc.

In Python, a byte string is just that: a sequence of bytes. It isn't human-readable. Under the hood, everything must be converted to a byte string before it can be stored in a computer.

On the other hand, a character string, often just called a "string," is a sequence of characters that is human-readable. A character string can't be directly stored in a computer; it has to be encoded first (converted into a byte string). Multiple encodings, such as ASCII and UTF-8, allow a character string to be converted into a byte string.

Encoding and decoding are inverse operations. Everything must be encoded before it can be written to disk, and it must be decoded before it can be read by a human.

In Python, a byte string is represented by a b, followed by the byte string's ASCII representation.

A byte string can be decoded back into a character string if you know the encoding that was used to encode it.

__Example of a string:__

```python
my_string = "This string, will be stored as a string"
```

bytes = b'...' literals = a sequence of bytes. A “byte” is the smallest integer type addressable on a computer, which is nearly universally an octet or 8-bit unit, thus allowing numbers between 0 and 255.

__Example of a byte string:__

```python
my_byte_string = b"This is a byte string It will be stored as a sequence of bytes".
```

## Hashing Passwords

### Why do we need to Hash a Password?

Hashing is used mainly to protect a password from hackers. Suppose a website is hacked, and cybercriminals don’t get access to your password. Instead, they get access to the encrypted “hash” created by the method of hashing.

### Why do we use salt in hashing?

Historically, only the password’s cryptographic hash function was maintained on a system, but over time, additional precautions were developed to prevent the identification of duplicate or common passwords. One such prevention is salting.

### What is BCrypt?

The BCrypt Algorithm is a Python library used to hash and salt passwords securely. It enables the creation of a password protection layer that can develop local hardware innovation to protect against long-term hazards or threats, such as attackers having the computational capacity to guess passwords twice as efficiently.

All the necessary code snippets for this task are found in [example.py](example.py).
