import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', [
                                      '',
                                      '43_chars_long_name_........................',
                                      '41_chars_long_name_......................',])
    def test_add_new_book_dont_add_book_with_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_dont_add_book_that_already_in_dict(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_set_genre_to_one_book(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить': 'Комедии'}

    @pytest.mark.parametrize('genre', ['комедии', 'Аниме', '', 'comedy'])
    def test_set_book_genre_dont_set_invalid_genre(self, collector, genre):
        collector.add_new_book('New book')
        collector.set_book_genre('New book', genre)
        assert collector.get_books_genre() == {'New book': ''}

    def test_get_book_genre_get_book_genre_by_its_name(self, collector):
        collector.add_new_book('Kill La Kill')
        collector.set_book_genre('Kill La Kill', 'Комедии')
        assert collector.get_book_genre('Kill La Kill') == 'Комедии'

    def test_get_books_with_specific_genre_gets_two_book(self, collector, add_three_books_with_genres):
        collector.add_new_book('Book four')
        collector.set_book_genre('Book four', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Book one', 'Book four']

    def test_get_books_genre_gets_books_genres(self, collector, add_three_books_with_genres):
        assert collector.get_books_genre() == {'Book one': 'Комедии', 'Book two': 'Ужасы', 'Book three': 'Фантастика'}

    def test_get_books_for_children_returns_only_safe_books(self, collector, add_three_books_with_genres):
        assert collector.get_books_for_children() == ['Book one', 'Book three']

    def test_add_book_in_favorites_add_two_books_in_empty_favorites(self, collector, add_three_books_with_genres):
        collector.add_book_in_favorites('Book one')
        collector.add_book_in_favorites('Book three')
        assert collector.get_list_of_favorites_books() == ['Book one', 'Book three']

    def test_delete_book_from_favorites(self, collector, add_three_books_with_genres):
        collector.add_book_in_favorites('Book two')
        collector.delete_book_from_favorites('Book two')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('New book')
        collector.add_book_in_favorites('New book')
        assert collector.get_list_of_favorites_books() == ['New book']


