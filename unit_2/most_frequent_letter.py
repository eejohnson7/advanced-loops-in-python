'''
You are given a string of n words, with n ranging from 1 to 100, inclusive. The words are separated by a single space in the string. Your task is to return the most frequently occurring character in each word that has an odd number of characters. The resulting characters should be concatenated into a string with their occurrences in the sentence.

Please note:

Each word's character count ranges from 1 to 500, inclusive. The string contains lowercase and uppercase alphanumeric characters, spaces, and punctuation.
For instance, if the input string is "Hello world this is a demo string", your function should return "lwa". In this string, 'Hello', 'world', and 'a' have an odd number of characters. The most frequently occurring character in these words are 'l', 'w', and 'a' respectively. When concatenated, they form "lwa".
In case of a tie in character frequency, return the character that appears first in the word. In the example above, we took 'w' from the word 'world'.
The function should be case insensitive. The lowercase and uppercase characters should be counted as the same character. The output should only contain lowercase characters. For example: "Hhi" should return "h" because "h" appears twice in the string even though one is uppercase and one is lowercase.
If there are no words with an odd number of characters in the input string, your function should return an empty string.
The input string will always be at least one character long, and it cannot be just a single whitespace.
Having a good understanding of string operations and the use of nested loops is very useful in solving this task.
'''

def solution(sentence):
    # TODO: implement the solution here
    result = ""
    words = sentence.split(' ')

    for word in words:
        word = word.lower()
        
        if len(word) % 2 != 0:
            letter_counts = []
            counted_letters = ""
            
            if len(word) == 1:
                letter_counts.append((word[0], 1))
            else:
                for i in range(0, len(word) - 1):
                    count = 1
                    
                    for j in range(i + 1, len(word)):
                        if word[i] == word[j]:
                            count += 1
                        
                    if word[i] not in counted_letters:
                        counted_letters += word[i]
                        letter_counts.append((word[i], count))
                        
            most_freq_letter = letter_counts[0]
            for i in range(1, len(letter_counts)):
                if most_freq_letter[1] < letter_counts[i][1]:
                    most_freq_letter = letter_counts[i]
                    
            result += most_freq_letter[0]
            
    return result