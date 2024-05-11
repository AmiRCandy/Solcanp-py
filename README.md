# Solcanp-py
A very very simple library for usings solcan api for free
If the stars reach 10 , I will write it compltely for you !

## Usage/Examples

```python
from solcanpy import Solcan

solcan = Solcan()

print(solcan.getSPL('addr'))
print(solcan.getAccountTokens('addr'))
print(solcan.getAccountTransction('addr',limit=10))
print(solcan.getSolTransfers('addr',limit=10,offset=0))
```


## Authors

- [@AmiRCandy](https://www.github.com/AmiRCandy)

