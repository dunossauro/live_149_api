from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Book

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book

    id = fields.Integer(required=True)
    livro = fields.Str(required=True)
    escritor = fields.Str(required=True)
    price = fields.Float(required=True)
    price = fields.Float(required=True)
    short_desc = fields.Str(required=True)
    long_desc = fields.Str(required=True)
    img = fields.Str(required=True)
