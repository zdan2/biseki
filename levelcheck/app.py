import pandas as pd
class BookManager:
    def __init__(self):
        self.books = []


    def add_book(self, title, author, year, isbn):
        book = {"title": title, "author": author, "year": year, "isbn": isbn}
        self.books.append(book)

    def get_books_by_isbn(self, isbn):
        return [book for book in self.books if book["isbn"] == isbn]

    def get_all_books(self):
        self.books.sort(key=lambda x: x["year"])
        return self.books
    
    def save_cvs(self):
        df=pd.DataFrame(self.books)
        df.to_csv("books.csv",index=False)
    
    def load_csv(self,file_name):
        df=pd.read_csv(file_name)
        self.books=df.to_dict('records')


bm=BookManager()

bm.add_book('Test','Taro',1992,2583)
bm.add_book('Sample','Taka',1999,2222)
print(bm.get_all_books())
bm.save_cvs()
print(bm.get_books_by_isbn(2583))

    
    