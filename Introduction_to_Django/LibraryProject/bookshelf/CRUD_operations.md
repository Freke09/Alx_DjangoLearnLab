# Django CRUD Operations

##  Create:
```
from bookshelf.models import Book
book = Book(title = '1984', author = 'George Orwell', published_date = 1949)
book.save()

# No output
```
## Retrieve:
```
for book in Book.objects.all():
    print(book)

# 1984 by George Orwell Published in 1949
```

## Update:
```
book.title = 'Nineteen Eighty-Four'
book.save()

# No output
```

## Delete:
```
# command:
Book.objects.filter(title='Nineteen Eighty-Four').delete()

# output:
# (1, {'bookshelf.Book': 1})
```