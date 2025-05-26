import re  # regex toolset

# STEP 1 - Replace vowels and shift consonants
# Vowels (a, e, i, o, u) becomes ASCII ("e" -> "101" ("#"?))
# Consonants shifted to the next letter ('d' to 'f' or 'd' to 'e' to 'f' or '101' or '#101'; 'z' to 'a' or 'z' to 'Z')
#
# ToDo:
# - Clarify 1st step questions:
#   - Should vowels have "#" before/after ASCII? (e.g., "#101"?)
#   - Should consonant shift jump 1 or 2 letters?
#   - Preserve case for 'z' -> 'a'? (Z -> A or Z -> a)

def step1_replace_vowels_and_shift_consonants(text):
    chars_encoded = ""
    for char in text:
        if char.lower() in "aeiou":
            chars_encoded += str(ord(char))  # unicode ord(char) to string from number for vowels set
        elif char.isalpha():  # True if char is in [a-zA-Z]
            next_letter = chr(ord(char) + 1) if char.lower() != 'z' else 'a'
            if char.isupper() and next_letter.islower():
                next_letter = next_letter.upper()
            chars_encoded += next_letter
        else:
            chars_encoded += char  # untouched ![a-zA-Z] goes straight-forward
    return chars_encoded


# STEP 2 - Substring Rearrangement
# For every word length > than 5 characters:
# - Split into two halves
# - If the word length is odd (7, 9, etc), assign the middle character to the first half -> Forward -> ard w For(?)
# - Swap halves ("Python" -> "honPyt")
#
# ToDo:
# - Clarify 2nd step questions:
#   - Should punctuation be treated as part of the word?
#   - Is word definition based on spaces?

def step2_rearrange_words(text):
    words = text.split(' ')
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
    return ' '.join(words_rearranged)


# STEP 3 - Index-Based Encoding
# For each character in the result string:
# - Add its position index (starting from 0) to its ASCII value(?)
# - Convert the resulting number back to a character(?)
#
# ToDo:
# - Confirm printable range safety
# - Decide whether to wrap characters that exceed ASCII 126

def step3_index_based_encoding(text):
    position_encoded = ""
    for index, char in enumerate(text):
        position_encoded += chr(ord(char) + index)
    return position_encoded


# STEP 4 - Special Symbol Insertion
# - After every third character (1-based counting), insert a "#" (hash) character
#
# ToDo:
# - Confirm if this should count only letters or all characters
# - Should it ignore inside digit groups?

def step4_insert_hash_every_third(text):
    with_hash = ""
    for i, ch in enumerate(text):
        with_hash += ch
        if (i + 1) % 3 == 0:
            with_hash += "#"
    return with_hash


# STEP 5 - Number Encoding
# For each numeric sequence:
# - Multiply the number by 3
# - Reverse the resulting digits
# - Optionally, insert "#" between digits (depending on final format spec)
#
# ToDo:
# - Confirm target format: "3#69" vs "9#6#3"
# - Are numbers grouped or handled digit-by-digit?

def step5_transform_numbers(text):
    def transform_number(match):
        original_number = match.group()                # ex. "123"
        multiplied = int(original_number) * 3          # 123 * 3 = 369
        multiplied_str = str(multiplied)               # 369 to "369"

        # reverse digits manually
        reversed_digits = []
        for digit in multiplied_str:
            reversed_digits.insert(0, digit)           # shift from start

        # joining w/ "#"
        return '#'.join(reversed_digits)               # "9#6#3"

    return re.sub(r'\d+', transform_number, text)


# Main encoder function
def encode(text):
    step1 = step1_replace_vowels_and_shift_consonants(text)
    step2 = step2_rearrange_words(step1)
    step3 = step3_index_based_encoding(step2)
    step4 = step4_insert_hash_every_third(step3)
    step5 = step5_transform_numbers(step4)
    return step5


# Usage Example
if __name__ == "__main__":
    example = "Hello World! 123"
    result = encode(example)
    print("Encoded result:", result)
