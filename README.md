# Movie Api

Movie Apit is a Django Rest project with a collection Apis for sign-in, list, search and review movies.

## Usage

This project includes the Dockerfile and docker-compose.yml to help you set up easily without requiring to install
dependencies. Also, when you run  docker file is imported some test data.

```sh
$ docker-compose up --build
```

## Database Schema

### User

This is the user model where we save all the users of our system. Mandatory fields is : username ,password

### Movie

This is the model where we store the movies of our app.
Fields :
* Image (charfield) : The main image url of the movie (eg. photos/12345/main.png)
* Title (charfield) : The title of the movie (eg. Spiderman)
* Plot (textfield) : A short description of the movie's plot
* Genres (charfield) : The genres of this movie
* Duration (charfield): The duration of the movie

### Review

This is the model where we store a review for a movie. Fields :

* Movie (ForeignKey) : Foreign key for which movie this review refers
* Score (intergerfield) : The score of a review with validation. The score should be between 1 and 5
* Comment (textfield) : Where the user can write a comment his review. This field can be `Null`

## Api Collection

Apis of the project is:

### Login

* Url: `localhost:8000/account/login`
* Method: `POST`
* Body : `{'username`:username,'password':password}`
* Response : {'username':username , 'token': jwt_token

### Units

* Url: `localhost:8000/movie`
* Method: `GET`
* QueryParams :
    * `search` (optional) : you can search with genres or title
    * `ordering` (optional) : sort by score of a movie
    * `page_size` (optional) : with this param you can define how many movies the api can return. Default number is 10
    * Authentication : You should add in headers the following : `HTTP_AUTHORIZATION:"Bearer token"`
    * Response :
      ```json
      {
        "count": 20, //total number of units in db
        "next": "http://localhost:8000/movies/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1, //the id of unit
                "image": "foo/bar0.jpg",
                "title": "Batman",
                "genres": "ACTION",
                "plot": "This is a random description for Batman unit",
                "duration": "2h",
                "score": null //average score of all reviews for a unit
            }
        ]
      }
      ```

### Review

* Url: `localhost:8000/review`
* Method: `POST`
* Body :
    * `movie` (required) : the id of the movie that the review is referred to
    * `score` (required) : a integer between 1 and 5
    * `comment` (optional) : a text with some comments about this unit
    * Authentication : You should add in headers the following : `HTTP_AUTHORIZATION:"Bearer token"`

## Local Development setup instructions

### Install pyenv with python 3.8.10

* Install pre-requestic packages https://github.com/pyenv/pyenv/wiki#:~:text=Suggested%20build%20environment
* Install pyenv : git clone https://github.com/pyenv/pyenv.git ~/.pyenv
* Set pynenv in
  bash https://github.com/pyenv/pyenv#:~:text=make%20%2DC%20src-,Configure%20your%20shell%27s%20environment%20for%20Pyenv,-Note%3A%20The%20below
* Download python pyenv install 3.10.4

More details : https://github.com/pyenv/pyenv

### Install Poetry and start projects new virtual env

* Download poetry and install : curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py |
  python3 - configure your current shell run `source $HOME/.poetry/env`
  *Set python 3.10.4 as default inside project folder `poetry env use ~/.pyenv/versions/3.10.4/bin/python`
* Create virtual env for project. Inside in project directory run `poetry shell`
* Install dependencies `poetry install`

More details :  https://python-poetry.org/

### Run server

* Enable virtual projects virtual env with `poetry shell`
* Start the server locally `python manage.py runserver`

### Run tests

* Enable virtual projects virtual env with `poetry shell`
* Start the server locally `python manage.py test `

### Import Test Data

If you would like to import same sample data in your project for local testing you can run the following commands :

* Enable virtual projects virtual env with `poetry shell`
* Start the server locally `python manage.py import_test_data`

### Security

To secure our project we use JWT token for authorization with the help of the following library
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html
