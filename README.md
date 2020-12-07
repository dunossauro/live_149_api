# live_149_api
Flask rest api da live 149


## Como rodar esse projeto

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```


## Rotas

```
Endpoint           Methods  Rule
-----------------  -------  -----------------------
books.book_ids     GET      /book/<_id>/
books.book_search  GET      /books/search/<term>
books.books        GET      /books/
books.books        GET      /books/page/<int:page>/
books.index        GET      /
books.popular      GET      /populate/
static             GET      /static/<path:filename>
```
