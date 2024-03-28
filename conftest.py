import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope='function')
def add_three_books_with_genres(collector):

    books_names = ['Book one', 'Book two', 'Book three']
    books_genre = ['Комедии', 'Ужасы', 'Фантастика']

    for i in range(len(books_names)):
        collector.add_new_book(books_names[i])
        collector.set_book_genre(books_names[i],books_genre[i])
    return collector
