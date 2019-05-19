# Bucks Wagtail

Wagtail application/website for the Buckinghamshire adult social care project.

The master branch of this repo automatically deploys to [bucks-wagtail.herokuapp.com](http://bucks-wagtail.herokuapp.com).

## Developing locally

1. Create a python virtual environment and clone this repo into the environment's folder. [Pipenv](https://docs.pipenv.org/en/latest/) is a good tool for this.
2. Activate the virtual environment (if using pipenv, the command is `pipenv shell`)
3. Install python dependencies with `pip install -r requirements.txt`
4. Make sure a local postgresql server is running, and run `python manage.py migrate` to prepare a development database
5. Finally, create a local initial admin user with `python manage.py createsuperuser`
6. Run the app with `python manage.py runserver`.
6. The app should be at `localhost:8000`.

## Deploying to Heroku

This app has been prepared for Heroku according to [this guide](https://wagtail.io/blog/wagtail-heroku-2017/). It has a `Procfile` and `runtime.txt` that should make deploying relatively painless.

To deploy:

1. Create a new app on Heroku and link to this repo. A database add-on should be automatically provisioned
2. Make sure the `DATABASE_URL`, `SECRET_KEY` and `DJANGO_SETTINGS_MODULE` config vars are set
3. Run `python manage.py migrate` on Heroku to prepare the new database
4. Run `python manage.py createsuperuser` to create an initial admin user
5. The Wagtail dashboard should be accessible at the path /admin