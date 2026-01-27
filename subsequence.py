# Google Coding Intervierw Exercise
#
# Given a string s and an array of string words, return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order fo the remaining characters.
# For example, "ace" is a subsequence of "abcde".
#
# Example 1:
# Input: s = "abcde", words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace"

# Option 1: Brute force calculation of all posible subsequences of string s. Then check how many we have in words. Really bad idea.
#
# Option 2:
# Take each string in words and check if it is a subsequence of s.
# start counter at 0
# For each word in words
#   if is subsequence increment counter by none
#   else go to next word
# To check if is subsequence
# for each letter in word
#   find first match in s
#   if there is a match,
#       delete letter from s and continue, checking now from that index onwards
#   else if there is no match
#       break, because is no longer sequence
#   it is a subsequences only if every letter in word has a match

s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"] # answer: 2
# s = "abcde"
# words = ["a", "bb", "acd", "ace"] # answer: 3

def is_subsequence(base_string = "", subsequence = ""):
    match_counter = 0
    trimed_string = base_string
    for letter in subsequence:
        if letter in trimed_string:
            match_counter += 1
            trimed_string = trimed_string[trimed_string.index(letter) + 1:]
        else:
            return False
    return match_counter == len(subsequence)

def count_subsequences(base_string, subsequences):
    counter = 0
    for sub in subsequences:
        if is_subsequence(base_string, sub):
            counter += 1
    return counter

print("Base String: ", s)
print("Subsequences: ", words)
print("Count: ", count_subsequences(s, words))
