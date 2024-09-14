Author: Manasvin Shrimali
# Exercise 1: Create a string made of the first, middle, and last character
def first_middle_last(s):
    first = s[0]
    middle = s[len(s) // 2]
    last = s[-1]
    return first + middle + last

# Exercise 2: Create a new string made of the first three characters
def first_three(s):
    return s[:3]

# Exercise 3: Append new string in the middle of a given string
def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    return s1[:middle_index] + s2 + s1[middle_index:]

# Exercise 4: Arrange string characters such that lowercase letters should come first
def arrange_characters(s):
    lower = ''.join([c for c in s if c.islower()])
    upper = ''.join([c for c in s if c.isupper()])
    return lower + upper

# Exercise 5: Count all letters, digits, and special symbols from a given string
def count_characters(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    special = len(s) - letters - digits
    return letters, digits, special

# Exercise 6: Create a mixed String using the following rules
def create_mixed_string(s1, s2):
    return ''.join([a + b for a, b in zip(s1, s2)])

# Exercise 7: String characters balance Test
def balance_test(s):
    return s.count('a') == s.count('b')

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
def find_substring_occurrences(s, sub):
    return [i for i in range(len(s)) if s[i:i+len(sub)].lower() == sub.lower()]

# Exercise 9: Calculate the sum and average of the digits present in a string
def sum_and_average_of_digits(s):
    digits = [int(c) for c in s if c.isdigit()]
    total = sum(digits)
    average = total / len(digits) if digits else 0
    return total, average

# Exercise 10: Write a program to count occurrences of all characters within a string
def count_all_characters(s):
    return {c: s.count(c) for c in set(s)}

# Exercise 11: Reverse a given string
def reverse_string(s):
    return s[::-1]

# Exercise 12: Find the last position of a given substring
def last_position_of_substring(s, sub):
    return s.rfind(sub)

# Exercise 13: Split a string on hyphens
def split_on_hyphens(s):
    return s.split('-')

# Exercise 14: Remove empty strings from a list of strings
def remove_empty_strings(strings):
    return [s for s in strings if s]

# Exercise 15: Remove special symbols / punctuation from a string
import string
def remove_special_symbols(s):
    return ''.join(c for c in s if c not in string.punctuation)

# Exercise 16: Remove all characters from a string except integers
def remove_non_integers(s):
    return ''.join(c for c in s if c.isdigit())

# Exercise 17: Find words with both alphabets and numbers
def find_words_with_alnum(s):
    return [word for word in s.split() if any(c.isalpha() for c in word) and any(c.isdigit() for c in word)]



print(first_middle_last("example"))  # Output: "eap"
print(first_three("example"))  # Output: "exa"
print(append_in_middle("Ault", "Kelly"))  # Output: "AuKellylt"
print(arrange_characters("PyThOn"))  # Output: "yhnPTO"
print(count_characters("Hello123!"))  # Output: (5, 3, 1)
print(create_mixed_string("abc", "123"))  # Output: "a1b2c3"
print(balance_test("aabb"))  # Output: True
print(find_substring_occurrences("Hello hello", "hello"))  # Output: [0, 6]
print(sum_and_average_of_digits("abc123"))  # Output: (6, 2.0)
print(count_all_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(reverse_string("hello"))  # Output: "olleh"
print(last_position_of_substring("hello hello", "hello"))  # Output: 6
print(split_on_hyphens("a-b-c"))  # Output: ['a', 'b', 'c']
print(remove_empty_strings(["a", "", "b", ""]))  # Output: ['a', 'b']
print(remove_special_symbols("hello!"))  # Output: "hello"
print(remove_non_integers("a1b2c3"))  # Output: "123"
print(find_words_with_alnum("abc123 def456"))  # Output: ["abc123", "def456"]

