# Find the key with the maximum value in a dictionary.

scores = {"Alice": 82, "Bob": 91, "Charlie": 78, "Diana": 95}


max_key = max(scores , key = scores.get)
print(max_key)