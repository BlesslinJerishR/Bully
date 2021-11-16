#! python3
# bully.py - Bully will stick bullets++ to wikipedia markups.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines & add stars
# L1
lines = text.split('\n')
for l in range(len(lines)):
    lines[l] = '*' + lines[l]
text = '\n'.join(lines)
pyperclip.copy(text)

