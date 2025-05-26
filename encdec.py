import re # regex toolset

def encode(text):
    # STEP 1 - Replace vowels and shift consonants
    # Vowels (a, e, i, o, u) becomes ASCII ("e" -> "101" ("#"?))
    # Consonants shifted to the next letter ('d' to 'f' or 'd' to 'e' to 'f' or '101' or '#101'; 'z' to 'a' or 'z' to 'Z')
 
    # ToDo:
    # Clearify 1st step questions
  
    chars_encoded = ""
    for char in text:
        if char.lower() in "aeiou":
            chars_encoded += str(ord(char)) # unicode ord(char) to string from number for vowels set
        elif char.isalpha(): # True if char is in [a-zA-Z]
            next_letter = chr(ord(char) + 1) if char.lower() != 'z' else 'a'
            if char.isupper() and next_letter.islower():
                next_letter = next_letter.upper()
            chars_encoded += next_letter
        else:
            chars_encoded += char  # untouched ![a-zA-Z] goes straight-forward


    # STEP 2
    
    # STEP 3 - Index-Based Encoding
    # For every character, add its index (starting from 0) to its ASCII code
    # ToDo: 
    # Clearify 3rd step Q
    #  - It creates a position-based offset, which makes even repeated letters encode differently
    #  - It mitigates a risk(!)
    #  - It may push characters beyond visible (strong length?)

    position_encoded = ""
    for index, char in enumerate(rearranged_text):
        position_encoded += chr(ord(char) + index)
        
    
    # STEP 4
    
    # STEP 5
    
