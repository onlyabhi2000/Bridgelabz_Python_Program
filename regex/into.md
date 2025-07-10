A Regular Expression (RegEx) is a sequence of characters that defines a search pattern. 


| Regex Pattern | Matches                              |
| ------------- | ------------------------------------ |
| `abc`         | the exact substring "abc"            |
| `\d`          | any single digit (0–9)               |
| `\w`          | any word character (letter/digit/\_) |
| `\s`          | any whitespace (space, tab, newline) |
| `.`           | any character except newline         |
| `a*`          | 0 or more a's                        |
| `a+`          | 1 or more a's                        |
| `a?`          | 0 or 1 a                             |
| `[abc]`       | a, b, or c                           |
| `[^abc]`      | anything except a, b, or c           |
| `a{2,4}`      | between 2 and 4 a's                  |



########################################################


Flags modify behavior:

re.IGNORECASE (or re.I) — case-insensitive

re.MULTILINE (or re.M) — ^ and $ match lines

re.DOTALL (or re.S) — . matches newline


########################################################


Compiling Patterns
You can pre-compile a pattern for repeated use:

pattern = re.compile(r'\d+')
result = pattern.findall('123 abc 456')
print(result)  


########################################################



*** CHEAT SHEET ***

| Task          | Example Pattern |    |
| ------------- | --------------- | -- |
| Digit         | `\d`            |    |
| Non-digit     | `\D`            |    |
| Word char     | `\w`            |    |
| Non-word      | `\W`            |    |
| Whitespace    | `\s`            |    |
| Non-space     | `\S`            |    |
| Start line    | `^`             |    |
| End line      | `$`             |    |
| Any char      | `.`             |    |
| 0+ repeats    | `*`             |    |
| 1+ repeats    | `+`             |    |
| 0/1 optional  | `?`             |    |
| Exact n       | `{n}`           |    |
| n to m        | `{n,m}`         |    |
| Or            | \`              | \` |
| Grouping      | `( )`           |    |
| Character set | `[abc]`         |    |
| Negated set   | `[^abc]`        |    |


##########################################################

What is re.compile()?
re.compile() pre-compiles a regular expression pattern into a RegexObject.
import re

pattern = re.compile(r'\d+')


When should you use re.compile()?
✔️ Recommended when:

✅ You’ll use the same regex many times
✅ You want better performance
✅ You want cleaner, more readable code

##########################################################
