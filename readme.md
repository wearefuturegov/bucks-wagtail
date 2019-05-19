# Bucks Wagtail

Wagtail application/website for the Buckinghamshire adult social care project.

## Deploying to Heroku

This app has been prepared for Heroku according to [this guide](https://wagtail.io/blog/wagtail-heroku-2017/). It has a `Procfile` and `requirements.txt` that should make deploying relatively painless.

To deploy:

1. Create a new app on Heroku and link to this repo. A database add-on should be automatically provisioned
2. Make sure the `DATABASE_URL`, `SECRET_KEY` and `DJANGO_SETTINGS_MODULE` config vars are set
3. Run `python manage.py migrate` on Heroku to prepare the new database
4. Run `python manage.py createsuperuser` to create an initial admin user
5. The Wagtail dashboard should be accessible at the path /admin