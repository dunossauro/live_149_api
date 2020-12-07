from flask import Blueprint, current_app, request, jsonify, url_for
from .model import Book
from .serializer import BookSchema
from .fake_data import BookFactory


bp_books = Blueprint('books', __name__)

@bp_books.route('/')
def index():
    return jsonify(
        {
            '/books': 'book list',
            '/book/<id>': 'check one book',
            '/populate': 'populate data base',
            '/search': 'search book by long description'
        }
    )


@bp_books.route('/books/')
@bp_books.route('/books/page/<int:page>/')
def books(page=1):
    result = Book.query.paginate(page, 10)
    return jsonify({
        'page': page,
        'books': BookSchema(many=True).dump(result.items),
        'total pages': result.pages,
        'total per pages': result.per_page,
        'next page': f'{url_for("books.books")}{result.next_num}',
        'previous page': f'{url_for("books.books")}{result.prev_num}',
    }
    ), 200


@bp_books.route('/books/search/<term>')
def book_search(term):
    result = Book.query.filter(Book.long_desc.contains(term))
    return BookSchema(many=True).jsonify(result), 200


@bp_books.route('/book/<_id>/', methods=['GET'])
def book_ids(_id):
    try:
        result = Book.query.filter(Book.id==_id).one()
        return BookSchema().jsonify(result), 200
    except:
        return 'Not Found', 404


@bp_books.route('/populate/', methods=['GET'])
def popular():
    for book in BookFactory.build_batch(10):
        current_app.db.session.add(book)
        current_app.db.session.commit()
    return 'ok', 200
