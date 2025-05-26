import re  # regex toolset

def encode(text):
    # STEP 1 - Replace vowels and shift consonants
    # Vowels (a, e, i, o, u) -> ASCII ("e" -> "101")
    # Consonants -> shifted to the next letter ('d' -> 'e', 'z' -> 'a')
    # ToDo: Clarify vowel formatting (should we insert "#" before/after ASCII? Currently: no)

    chars_encoded = ""
    for char in text:
        if char.lower() in "aeiou":
            chars_encoded += str(ord(char))  # unicode ord(char) to string for vowels
        elif char.isalpha():  # True if char is in [a-zA-Z]
            next_letter = chr(ord(char) + 1) if char.lower() != 'z' else 'a'
            if char.isupper() and next_letter.islower():
                next_letter = next_letter.upper()
            chars_encoded += next_letter
        else:
            chars_encoded += char  # untouched non-letter characters

    # STEP 2 - Substring Rearrangement
    # For every word longer than 5 characters:
    # - Split into two halves
    # - If the word length is odd, assign the middle character to the first half
    # - Swap halves ("Python" -> "honPyt")
    # ToDo: Clarify if punctuation should be treated as part of the word

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
    # - Add its position index (starting from 0) to its ASCII value
    # - Convert result to character
    # ToDo:
    # - Confirm printable range safety
    # - Decide whether to wrap characters that exceed ASCII 126

    position_encoded = ""
    for index, char in enumerate(rearranged_text):
        position_encoded += chr(ord(char) + index)

    # STEP 4 - Special Symbol Insertion
    # After every third character, insert "#"
    # ToDo: Confirm if this should count only letters or all characters

    # STEP 5 - Number Encoding
    # For each numeric sequence:
    # - Multiply number by 3
    # - Reverse the digits
    # - Insert "#" between digits (optional; format inconsistency noted)
    # ToDo:
    # - Confirm target format: "3#69" vs "9#6#3"
