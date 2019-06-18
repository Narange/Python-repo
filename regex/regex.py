import re

text_corpus = """
qwertyuiop
QWERTYUIOP

Hello

. [ ] { } ( ) ^

duckduckgo.com

Mr. Smith
Mrs. Smith

This is a sentence from a Wiki article[3], probably.
"""

sentence = "This[94] is another sentence[5] with a few[87] references."

# Create a pattern
pattern = re.compile(r"\[\d*\]")
new_sentence = re.sub(pattern, "", sentence)

print(new_sentence)

#matches = pattern.finditer(text_corpus)

#for match in matches:
#    print(match)
