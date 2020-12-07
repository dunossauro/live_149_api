import factory
from faker import Faker
from app.model import Book

faker = Faker()


def random_color_url():
    return f'https://via.placeholder.com/500/{faker.hex_color()[1:]}/'
    

class BookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Book

    escritor = factory.Faker('name_nonbinary')
    livro = factory.Faker('catch_phrase')
    short_desc = factory.Faker('text', max_nb_chars=200)
    long_desc = factory.Faker('text', max_nb_chars=1000)
    price = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    img = factory.LazyFunction(random_color_url)
