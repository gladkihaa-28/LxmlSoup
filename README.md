# LxmlSoup

LxmlSoup is an analogue of BeautifulSoup, containing the most basic and necessary methods. Its speed exceeds bs4 by 2 times. The syntax is the same.

```
0.7749056816101074 - LxmlSoup
1.4368107318878174 - BeautifulSoup
```

## Installation

LxmlSoup requires Python >= 3.7

Install with `pip` from PyPI:

```
pip install LxmlSoup
```

### Example

```python
from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://sunlight.net/catalog').text
soup = LxmlSoup(html)

links = soup.find_all('a', class_='cl-item-link js-cl-item-link js-cl-item-root-link')
for link in links:
    print(link.text(), link.get('href'))
```


You can support the author so that updates come out more often.
Sberbank - 2202 2062 9710 1995


