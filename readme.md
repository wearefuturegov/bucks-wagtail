# Bucks Wagtail

Wagtail application/website for the Buckinghamshire adult social care project.

It includes:

- the ability to edit a start/home page and an unlimited number long-form narrative 'life event' pages
- the ability to manage and edit a dataset of community assets

This app does **not** include any page templates or front-end styling, as it's intended to be used in a headless manner via the [Wagtail REST API](http://docs.wagtail.io/en/v2.0/advanced_topics/api/index.html).


**The master branch of this repo automatically deploys to [bucks-wagtail.herokuapp.com](http://bucks-wagtail.herokuapp.com).**

## API schema

Wagtail pages are available at:

- `/api/v2/pages`

Community assets/services are available at:

- `/api/services`

By default, this endpoint returns a list of services, with the following fields:

- `id`, the numerical database ID
- `name`, the common name of this service
- `parent_organisation`, the organisation delivering this service
- `description`, a textual description of the service
- `price`, a string describing the pricing structure of the service
            
- `category`, the category the service fits into
- `keywords`, an array of 
- `age_groups`, an array of age groups this service is suitable for
- `suitability`, an array of medical and social conditions this service is suitable for
- `accessibility`, on-site accessibility features

- `days`, an array of days this service is available on
- `frequency`, a description of when this service occurs
- `daytime`, true if the service is only available between 9am and 5pm weekdays, false otherwise

- `venue`, a description of the venue
- `area`, the area within Buckinghamshire this service is available
- `postcode`, the postcode of the above venue

- `contact_name`, the name of a person associates with this service
- `url`, the website
- `phone`, a contact telephone number
- `email`, a contact email address

**Apart from `id`, all fields are optional**

### Searching


### Filtering

It is possible to filter by any of these fields by adding query parameters to the end of the URL:

- `category__name`
- `days__name`
- `accessibility__name`
- `suitability__name`
- `age_groups__name`

For instance: `.../api/services?category__name=Cultural`

Values are case-sensitive.

### Searching

It is possible to perform a full-text case-insensitive search across these fields by adding a `?search=` query parameter:

- `name`
- `parent_organisation`
- `description`
- `keywords`
- `venue`
- `url`

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
2. Import the data to the 'raw' sheet [here](https://docs.google.com/spreadsheets/d/1dCfvWVy4GgJrL4AdNKhs2d2KYktuWFiarNJbTOh7mG4/edit?usp=sharing), and export the 'processed' sheet as a CSV file, and put it in the project root directory
3. Add the `python manage.py import [filename]` command, substituting the name of the CSV file