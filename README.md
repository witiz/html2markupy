# html2markupy

## Repository contents

This repository contains the source code for the [html2markupy](https://html2markupy.witiz.com) website.
The purpose is to let everyone experiment with the [markupy](https://markupy.witiz.com) syntax or help you migrate you existing templates.
All the features from the website are also available through a CLI `html2markupy` bundled in the [markupy](https://markupy.witiz.com) libray.

The website is a `flask` app, and the HTML rendering is powered by [markupy](https://markupy.witiz.com), you can have a look at the source code to get inspiration on how to structure your templates and components.

## Run it locally

Once the repository cloned, you have 2 options to start the app:

### Run the flask development server

- Install dependencies

```sh
$ uv sync 
```

- Start the flask server

```sh
$ uv run flask run
```

### Run with docker

```sh
$ docker compose up
```
