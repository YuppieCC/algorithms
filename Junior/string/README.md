## Reverse String
	
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

```
Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
```
Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.
```
Example 1:
Input: 123
Output: 321
```
```
Example 2:
Input: -123
Output: -321
```
```
Example 3:
Input: 120
Output: 21
```

Note:

 Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Index 

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

```
Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

Note: You may assume the string contain only lowercase letters.

## Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.
```
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
```
```
Example 2:
Input: s = "rat", t = "car"
Output: false
```

Note: You may assume the string contains only lowercase alphabets.
Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?

## Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

```
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
```
```
Example 2:
Input: "race a car"
Output: false
```

## String to Integer (atoi)

Implement ```atoi``` which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:

* Only the space character ' ' is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

```
Example 1:
Input: "42"
Output: 42
```
```
Example 2:
Input: "   -42"
Output: -42

Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```
```
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```
```
Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```
```
Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

## Implement strStr()

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
```
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
```
```
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's `strstr()` and Java's `indexOf()`.


## Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

* `1` is read off as `"one 1"` or `11`.
* `11` is read off as `"two 1s"` or `21`.
* `21` is read off as `"one 2, then one 1"` or `1211`.

>Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

```
Example 1:
Input: 1
Output: "1"
```
```
Example 2:
Input: 4
Output: "1211"
```

## Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
```
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
```
```
Example 2:
Input: ["dog","racecar","car"]
Output: ""
```

Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.


