# Original dictionary
original_dict = {
    10: 'ten',
    3: 'three',
    7: 'seven',
    1: 'one'
}


swapped_dict = {value : key for key , value in original_dict.items()}

print(swapped_dict)