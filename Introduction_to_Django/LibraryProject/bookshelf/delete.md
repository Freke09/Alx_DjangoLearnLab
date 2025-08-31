## Delete:
```
# command:
Book.objects.filter(title='Nineteen Eighty-Four').delete()

# output:
# (1, {'bookshelf.Book': 1})
```