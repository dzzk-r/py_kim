import re  # regex toolset

def encode(text):
    # STEP 1 - Replace vowels and shift consonants
    # Vowels (a, e, i, o, u) becomes ASCII ("e" -> "101" ("#"?))
    # Consonants shifted to the next letter ('d' to 'e'; 'z' to 'a' or 'Z')
    
    # ToDo:
    # - Clarify 1st step questions:
    #   - Should vowels be marked? (e.g., "#101")
    #   - Should consonants shift 1 or 2 letters?
    #   - Preserve case in 'z' to 'a' scenario?

    chars_encoded = ""
    for char in text:
        if char.lower() in "aeiou":
            chars_encoded += str(ord(char))  # vowel → ASCII as string
        elif char.isalpha():  # char in [a-zA-Z]
            next_letter = chr(ord(char) + 1) if char.lower() != 'z' else 'a'
            if char.isupper() and next_letter.islower():
                next_letter = next_letter.upper()
            chars_encoded += next_letter
        else:
            chars_encoded += char  # pass-through for non-letters


    # STEP 2 - Substring Rearrangement
    # For every word with > 5 characters:
    # - Split into two halves
    # - If length is odd, middle character goes into first half
    # - Swap halves: second_half + first_half

    # ToDo:
    # - Should punctuation be counted in word length?
    # - Is space the only delimiter?

    words = chars_encoded.split(' ')
    words_rearranged = []

    for word in words:
        if len(word) > 5:
            midd = (len(word) + 1) // 2
            first_half = word[:midd]
            second_half = word[midd:]
            twisted = second_half + first_half
            words_rearranged.append(twisted)
        else:
            words_rearranged.append(word)

    rearranged_text = ' '.join(words_rearranged)

    
    # STEP 3 - Index-Based Encoding
    # For each character:
    # - Add its index (starting from 0) to its ASCII code
    # - Convert result to character
    # - Risk: code may exceed printable ASCII range

    # ToDo:
    # - Wrap-around or fallback if ord > 126?
    # - Or define "safe zone" only?

    position_encoded = ""
    for index, char in enumerate(rearranged_text):
        position_encoded += chr(ord(char) + index)

    
    # STEP 4 - Special Symbol Insertion (# after every 3 characters)
    # After every third character (1-based counting), insert a "#" (hash) character

    # ToDo:
    # - Confirm if this should count only letters or all characters
    # - Should it ignore inside digit groups?

    with_hash = ""
    for i, ch in enumerate(position_encoded):
        with_hash += ch
        if (i + 1) % 3 == 0:
            with_hash += "#"

    return with_hash


    # STEP 5 - Number Encoding
    # For each numeric sequence:
    # - Multiply the number by 3
    # - Reverse the resulting digits
    # - Optionally, insert "#" between digits (depending on final format spec)

    # ToDo:
    # - Confirm target format: "3#69" vs "9#6#3"
    # - Are numbers grouped or handled digit-by-digit?
    
