
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Examples:
# Input : 
# Output : "fl"

# Explanation : All strings given in array contains common prefix "fl".


str = ["flowers" , "flow" , "fly", "flight" ]


def longest_common_prefix(str):
    
    prefix = str[0]

    for word in str[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(str))





# Given: ["flower", "flow", "flight"]

# Start with prefix = "flower"

# Compare with "flow":

# "flow" doesn't start with "flower" → remove last char → "flowe"

# still no match → "flow"

# Match! ✅

# Compare with "flight":

# "flight" doesn't start with "flow" → try "flo" → Match!

# try "fl" → Match! ✅

# Final prefix = "fl"