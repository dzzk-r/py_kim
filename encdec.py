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


    # STEP 2 – Substring Rearrangement
    # For every word length > than 5 characters:
    #  - Split into two halves
    #  - If the word length is odd (7,9,etc ), assign the middle character to the first half -> Forward -> ard w For(?)
    #. - Swap halves ("Python" -> "honPyt")

    # ToDo:
    # Clearify 2nd step questions
    
    words = chars_encoded.split(' ')
    words_rearranged = []

    for word in words:
        if len(word) > 5:
            midd = (len(word) + 1) // 2  # if odd, first half gets extra character(?)
            first_half = word[:midd]
            second_half = word[midd:]
            twisted = second_half + first_half
            words_rearranged.append(twisted)
        else:
            words_rearranged.append(word)  # short words stays as-is

    rearranged_text = ' '.join(words_rearranged)

    # STEP 3 - Index-Based Encoding
    # For each character in the result string:
    #  - Add its position index (starting from 0) to its ASCII value(?)
    #  - Convert the resulting number back to a character(?)


    # STEP 4 - Special Symbol Insertion
    #  - After every third character (1-based counting), insert a "#" (hash) character


    # STEP 5 - Number Encoding
    # For each numeric sequence:
    #  - Multiply the number by 3
    #. - Reverse the resulting digits
    #  - Optionally, insert # between digits (depending on final format spec)
