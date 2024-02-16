from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def log_this(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        logger.info(f'Func "{f.__name__}" was called')
        return res

    return wrapper


@log_this
def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Shop - main page</title>
        </head>
        <body>
            <h2 style="text-align: center; color: chocolate; text-transform: uppercase;">Main page</h2>
            <h1>This is my first django project</h1>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
                Nobis reprehenderit laudantium quam soluta minus aut nihil assumenda quibusdam tempore magni. 
                Molestias ad commodi eligendi suscipit aperiam facilis a veritatis delectus.
            </p>
            <a style="text-decoration: none;" href="/about">Link to About page</a>
        </body>
    </html>
    """
    return HttpResponse(html)