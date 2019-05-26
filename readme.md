# Bucks Wagtail

Wagtail application/website for the Buckinghamshire adult social care project.

It includes:

- the ability to edit a start/home page and an unlimited number long-form narrative 'life event' pages
- the ability to manage and edit a dataset of community assets

This app does **not** include any page templates or front-end styling, as it's intended to be used in a headless manner via the [Wagtail REST API](http://docs.wagtail.io/en/v2.0/advanced_topics/api/index.html).


**The master branch of this repo automatically deploys to [bucks-wagtail.herokuapp.com](http://bucks-wagtail.herokuapp.com).**

## API endpoints

- `/api/v2/pages`
- `/api/v2/community-assets`

## Prerequisites

- python3 and pip
- a running postgresql server

## Developing locally

Make sure you have a virtual environment tool installed before starting local development. [Pipenv](https://docs.pipenv.org/en/latest/) is a good tool for this.

1. Clone this repo and `cd` into it
2. Activate the virtual environment (if using pipenv, the command is `pipenv shell`)
3. Install python dependencies with `pip install -r requirements.txt`
4. Make sure a local postgresql server is running, and run `python manage.py migrate` to prepare a development database
5. Finally, create a local initial admin user with `python manage.py createsuperuser`
6. Run the app with `python manage.py runserver`.
6. The app should be at `localhost:8000`.

## Deploying to Heroku

This app has been prepared for Heroku according to [this guide](https://wagtail.io/blog/wagtail-heroku-2017/). It has a `Procfile` and `runtime.txt` that should make deploying relatively painless.

In production, Amazon S3 is used to store user image uploads, so you first need to create an S3 bucket and appropriately permissioned IAM user according to [this guide](https://wagtail.io/blog/amazon-s3-for-media-files/).

To deploy:

1. Create a new app on Heroku and link to this repo. A database add-on should be automatically provisioned
2. Make sure all the following config vars are set:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `DJANGO_SETTINGS_MODULE`
    - `AWS_STORAGE_BUCKET_NAME`
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
3. Run `python manage.py migrate` on Heroku to prepare the new database
4. Run `python manage.py createsuperuser` to create an initial admin user
5. The Wagtail dashboard should be accessible at the path /admin

## Importing community assets

Community assets have a complex data structure with several relations. Therefore, importing them is a three step process:

1. Run [this query](https://gist.github.com/jhackett1/7592e3400362a9a07b2938db0e21d068) on the source MS Access database and export the output as a spreadsheet
2. Import the data to the 'raw' sheet here, and export the 'processed' sheet as a CSV file, and put it in the project root directory
3. Add the `python manage.py import [filename]` command, substituting the name of the CSV file