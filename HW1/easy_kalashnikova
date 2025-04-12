class PersonalLibrary:
    def __init__(self):
        self.books = {}   
        self.next_id = 1   
        self.lending_history = {}  

    def add_book(self, title: str, author: str, year: int, genre: str) -> bool:
        book_id = self.next_id
        self.books[book_id] = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'available': True,
            'current_borrower': None
        }
        self.lending_history[book_id] = []
        self.next_id += 1
        return True

    def lend_book(self, book_id: int, borrower: str) -> bool:
        if book_id not in self.books or not self.books[book_id]['available']:
            return False
            
        self.books[book_id]['available'] = False
        self.books[book_id]['current_borrower'] = borrower
        self.lending_history[book_id].append({
            'action': 'lend',
            'borrower': borrower,
            'date': datetime.now() 
        })
        return True

    def return_book(self, book_id: int) -> bool:
        if book_id not in self.books or self.books[book_id]['available']:
            return False
            
        borrower = self.books[book_id]['current_borrower']
        self.books[book_id]['available'] = True
        self.books[book_id]['current_borrower'] = None
        self.lending_history[book_id].append({
            'action': 'return',
            'borrower': borrower,
            'date': 'today'
        })
        return True

    def find_books(self, **criteria) -> list:
        results = []
        for book_id, book in self.books.items():
            match = True
            for key, value in criteria.items():
                if key not in book or book[key] != value:
                    match = False
                    break
            if match:
                results.append((book_id, book))
        return results

    def get_lending_history(self, book_id: int) -> list:
        return self.lending_history.get(book_id, [])