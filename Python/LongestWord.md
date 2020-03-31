# Longest Word #

_Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty._

**Examples:**

```
Input: "fun&!! time" 
Output: time
Input: "I love dogs"
Output: love
```

### Concepts learned: ###

**split() Parameters**

The split() method takes maximum of 2 parameters:

    separator (optional)- The is a delimiter. The string splits at the specified separator.
    If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
    maxsplit (optional) - The maxsplit defines the maximum number of splits.
    The default value of maxsplit is -1, meaning, no limit on the number of splits.

Return Value from split()

The split() breaks the string at the separator and returns a list of strings.

max() with iterable arguments

To find the largest item in an iterable, we use this syntax:

max(iterable, *iterables, key, default)

max() Parameters

    iterable - an iterable such as list, tuple, set, dictionary, etc.
    *iterables (optional) - any number of iterables; can be more than one
    **key (optional) - key function where the iterables are passed and comparison is performed based on its return value
    default (optional) - default value if the given iterable is empty**

