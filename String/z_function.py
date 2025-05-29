# Given two strings, one is a text string, text, and the other is a pattern string, pattern. Print the indexes of all occurrences of the pattern string in the text string using the Z function algorithm. Use 0-based indexing while returning the indices.


# Examples:
# Input: text = "xyzabxyzabxyz", pattern = "xyz"

# Output: 0 5 10

# Expalanation : The pattern "xyz" occurs three times in text, starting at indices 0, 5, and 10.

text = "xyzabxyzabxyz"
pattern = "xyz"
index_data = []

for i in range(len(text)):
    if text.startswith(pattern):
        index_data.append(text[i])
    else:
        text = text[1:]

print(index_data)


###Step to solve :
# ex--> string --> ababaa , pat --> aba

#Step 1
# string tot = pat + "$" + string
# tot = aba$ababaa

# step 2
#