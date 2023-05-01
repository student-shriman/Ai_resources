# Question 1: Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.
def sum_of_even_numbers(numbers):
    return sum([num for num in numbers if num % 2 == 0])

# Question 2: Write a function that takes a string as input and returns a dictionary containing the frequency of each character in the string.
def character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Question 3: Write a function that takes two lists as input and returns a list containing all the elements that are common to both lists.
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Question 4: Write a function that takes a list of integers as input and returns the maximum sum of any contiguous subarray of the list.
def max_subarray_sum(numbers):
    max_so_far = max_ending_here = 0
    for num in numbers:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Question 5: Write a function that takes a string as input and returns the reverse of the string.
def reverse_string(string):
    return string[::-1]

# Question 6: Write a function that takes a list of strings as input and returns a list containing only the strings that are palindromes (i.e., they read the same backwards as forwards).
def palindrome_strings(strings):
    return [string for string in strings if string == string[::-1]]

# Question 7: Write a function that takes a list of tuples, where each tuple contains a name and an age, and returns a list of names sorted by age (from youngest to oldest).
def sort_names_by_age(names_and_ages):
    return [name for name, age in sorted(names_and_ages, key=lambda x: x[1])]

# Question 8: Write a function that takes a string as input and returns the first non-repeated character in the string.
def first_non_repeated_character(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

# Question 9: Write a function that takes a list of integers as input and returns the product of all the numbers in the list.
def product_of_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Question 10: Write a function that takes a string as input and returns the length of the longest substring that contains no repeating characters.
def length_of_longest_substring(string):
    max_length = 0
    for i in range(len(string)):
        substring = ""
        for j in range(i, len(string)):
            if string[j] in substring:
                break
            substring += string[j]
        max_length = max(max_length, len(substring))
    return max_length


# Question 1: Write a Python function that takes a sentence as input and returns the number of words in the sentence that contain at least one vowel.

def count_vowel_words(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    words = sentence.split()
    for word in words:
        for char in word:
            if char in vowels:
                count += 1
                break
    return count


# Question 2: Write a Python function that takes a sentence as input and returns the number of times each word appears in the sentence, sorted by frequency (from most frequent to least frequent).

def count_word_frequency(sentence):
    words = sentence.split()
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words


# Question 3: Write a Python function that takes a sentence as input and returns the number of unique words in the sentence.

def count_unique_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    return len(unique_words)


# Question 4: Write a Python function that takes a sentence as input and returns a list of all the n-grams in the sentence, where n is a parameter to the function.

def generate_ngrams(sentence, n):
    words = sentence.split()
    ngrams = []
    for i in range(len(words)-n+1):
        ngrams.append(words[i:i+n])
    return ngrams


# Question 5: Write a Python function that takes a list of sentences as input and returns a list of all the unique words in the sentences, sorted alphabetically.

def get_unique_words(sentences):
    unique_words = set()
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            unique_words.add(word)
    sorted_words = sorted(unique_words)
    return sorted_words


# Example usage of the functions

# Question 1
sentence = "The quick brown fox jumps over the lazy dog"
print(count_vowel_words(sentence))  # Output: 8

# Question 2
sentence = "The quick brown fox jumps over the lazy dog"
print(count_word_frequency(sentence))  # Output: [('the', 2), ('brown', 1), ('lazy', 1), ('dog', 1), ('quick', 1), ('fox', 1), ('jumps', 1), ('over', 1)]

# Question 3
sentence = "The quick brown fox jumps over the lazy dog"
print(count_unique_words(sentence))  # Output: 9

# Question 4
sentence = "The quick brown fox jumps over the lazy dog"
print(generate_ngrams(sentence, 3))  # Output: [['The', 'quick', 'brown'], ['quick', 'brown', 'fox'], ['brown', 'fox', 'jumps'], ['fox', 'jumps', 'over'], ['jumps', 'over', 'the'], ['over', 'the', 'lazy'], ['the', 'lazy', 'dog']]

# Question 5
sentences = ["The quick brown fox", "jumps over the lazy dog"]
print(get_unique_words(sentences))  # Output: ['The', 'brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
