##  Create:
```
from bookshelf.models import Book
Book.objects.create(
    title = '1984',
    author = 'George Orwell',
    published_date = 1949
)
# <Book: 1984 by George Orwell Published in 1949>
```