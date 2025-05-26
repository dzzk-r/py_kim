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
    
    # STEP 3
    
    # STEP 4
    
    # STEP 5
    
