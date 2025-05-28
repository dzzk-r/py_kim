```mermaid
graph LR
  encode["encode()"]

  encode --> step1["STEP 1 - vowels & consonants"]
  encode --> step2["STEP 2 - word rearrangement"]
  encode --> step3["STEP 3 - index shift"]
  encode --> step4["STEP 4 - insert '#' "]
  encode --> step5["STEP 5 - transform numbers"]

  step1 --> opt1_1["good: vowels to ASCII"]
  step1 --> opt1_2["bad: vowels with # (exmp #101)"]
  step1 --> opt1_3["good: consonants +1"]
  step1 --> opt1_4["bad: consonants +2 (breaks decode)"]

  step2 --> opt2_1["good: split & swap halves"]
  step2 --> opt2_2["bad: swap by letter type (unreliable)"]

  step3 --> opt3_1["good: add index to ord"]
  step3 --> opt3_2["bad: add random value (non-reversible)"] 
  step3 --> opt3_3["good: ASCII wrap if >126"]

  step4 --> opt4_1["good: '#' every 3 chars (by index)"]
  step4 --> opt4_2["bad: '#' after vowels only (ambiguous)"]

  step5 --> opt5_1["good: multiply *3, reverse, join with #"]
  step5 --> opt5_2["bad: replace digits with 'emoji' (non-reversible)"] 
  step5 --> opt5_3["bad: remove leading zeros (breaks restore)"]
```

# STEP 1 - Replace vowels and shift consonants
```py
  # Instead of: char == "d" -> "e"
  # You encode: char == "d" -> "f"
```
- Ambiguitty: "f" might be original or result of shift
- Decoder has no context to subtract +2 correctly
- Colides with ASCII replacement vowel
 

# STEP 2 - Substring Rearrangement
```py
  # Instead of: "Python" -> "honPyt"
  # You separate vowels and consonants:
  #  - vowels = ['o'], consonants = ['P','y','t','h','n'] -> merged arbitrarily
```
- Completely original word order loses 
- Impossible to to reverse
-  Breaks mapping between 'encode' and 'decode' 


# STEP 3 - Index-Based Encoding
```py
  # For each character in the result string:
  # - Add its position index (starting from 0) to its ASCII value(?)
  # - Convert the resulting number back to a character(?)
```

- Confirm printable range safety
- Decide whether to wrap characters that exceed ASCII 126

# STEP 4 - Special Symbol Insertion
```py
  # - After every third character (?), insert a "#" (hash) char.
```

- Confirm if it should count letters only or all of characters
- Should it take/ignore digit groups "insiders"

# STEP 5 - Number Encoding
```python
  # Instead of: "123" -> "369" -> "9#6#3"
  # You encode: "1" -> "one", "2" -> "two", "3" -> "three"
```

- output length changes
- ireversible with no embedded dictionary
- collision with real words

