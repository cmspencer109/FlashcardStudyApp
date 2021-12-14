# CS2300 Final Project - Flashcard app 'FlashStudy'

## Tech stack

* Backend
  + Python (Language)
  + Django (Web framework)
  + SQLite (Database)
* Frontend
  + HTML/CSS/JavaScript (Languages)
  + Bootstrap (Styling framework)
  + jQuery (JS library)
  + SwiperJS (Used on study screen)

## Helpful links

* https://www.djangoproject.com/start/
* https://docs.djangoproject.com/en/3.2/intro/tutorial01/
* https://learndjango.com/tutorials/template-structure


## Running the app

How to run the app (should appear on http://127.0.0.1:8000/)
`python3 manage.py runserver`

How to run migrations (only need to do this if you make changes to models.py)
`python3 manage.py makemigrations && python3 manage.py migrate `

## Miscellaneous

Currently setup with Heroku to auto deploy the `main` branch to https://mst-flash-study.herokuapp.com/
