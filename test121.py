"""Func"""

def func():
    """Books"""
    booklists = []
    for _ in range(int(input())):
        book = input()
        if book not in booklists:
            booklists.append(book)
    for _ in range(int(input())):
        bookname = input()
        if bookname in booklists:
            booklists.remove(bookname)
    print(len(booklists))
    for book in booklists:
        print(book)
func()
