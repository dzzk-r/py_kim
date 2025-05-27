import re
from refactored_encoder import (
    encode,
    step1_replace_vowels_and_shift_consonants,
    step2_rearrange_words,
    step3_index_based_encoding,
    step4_insert_hash_every_third,
    step5_transform_numbers,
)

# Case 1: clean encode-decode roundtrip
original = "Hello Python"
encoded = encode(original)
decoded = decode(encoded)

print("[TEST] Roundtrip test")
print("original:", original)
print("encoded :", encoded)
print("decoded :", decoded)
print("success:", decoded == original)

# Case 2: edge case where decode is not yet implemented
step1_only = step1_replace_vowels_and_shift_consonants("Hello Python")
print("[DEBUG] After STEP 1 only:", step1_only)

step3_edge = step3_index_based_encoding("100abc")
print("[DEBUG] Broken input after step3 logic:", step3_edge)
