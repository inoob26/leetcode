Leetcode problem [url](https://leetcode.com/problems/word-pattern)

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

**Example 1:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2:**
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```


**Example 3:**
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints:**
- `1 <= pattern.length <= 300`

- `pattern` contains only lower-case English letters.

- `1 <= s.length <= 3000`

- `s` contains only lowercase English letters and spaces ' '.

- `s` **does not contain** any leading or trailing spaces.

- All the words in `s` are separated by a **single space**.

Poorly worded problem. Here is an attempt to explain it better.

Given a pattern and a string s, find if s follows the same pattern. pattern and s are same if:

each character in pattern represents a word in s
No two distinct characters in pattern can represent the same word in s
No single character in pattern can represent two distinct words in s.
e.g.:

pattern = 'abab'; s = 'dog cat dog cat'; return True
'a' represents 'dog' and 'b' represents cat

pattern = 'abcb'; s = 'dog cat dog cat'; return False
'a' represents 'dog', 'b' represents 'cat'. Then 'c' cannot represent 'dog' again as 'a' already represents 'dog' (#2 condition is: No two distinct characters in pattern i.e. 'a' and 'c' can represent same word i.e 'dog'.)

pattern = 'abcb'; s = 'dog cat hat cat'; return True
'a' represents 'dog'; 'b' represents 'cat'; 'c' represents 'hat'; and last 'cat' is already represented by 'b' and last character in pattern is also 'b'.
