# Defcon 29 Badge Code Generator

Date: Sat 07 August 2021

Licence: MIT (2021)

---
This script is based on the work of [**igloo22225**](https://github.com/igloo22225/dc29-badge-response-generator).
Have a look to his analysis, and how he decrypted the token, on [his github repository](https://github.com/igloo22225/dc29-badge-response-generator).

This python version wouldn't exists without his help.

---
This is a short python equivalent to *igloo22225*'s GO version. It will simply and automatically generate a succession of 'resp' token matching your DC29 badge 'req' token.
I increased entropy by using random hexadecimal numbers in Tier Badge informations. Some areas in the token (Prefix, IsSignalBadge), are constants to identify the badge's status.
(*So far it works!*)

To install and use it:

- Python 3.6 and Higher.
- Library used are built in.
- Launch the script and follow instructions.
