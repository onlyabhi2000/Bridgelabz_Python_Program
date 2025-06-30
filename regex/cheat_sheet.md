| Pattern         | Matches                      |
| --------------- | ---------------------------- |
| `\d`            | single digit (e.g. '1')      |
| `\d+`           | whole integers (e.g. '123')  |
| `\d+\.\d+`      | decimals only (e.g. '49.99') |
| `\d+(?:\.\d+)?` | integers and decimals        |


email :
pattern = r'^[\w\.-]+@[\w-]+\.[a-zA-Z]{2,}$'