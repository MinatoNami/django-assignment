from django.shortcuts import render
from .utils import connectToDB, retrieveData


def index(request):
    db_connection = connectToDB(isLocal=True)
    coordinates = []

    if db_connection:
        coordinates = retrieveData(db_connection)
        db_connection.close()

    return render(request, 'Points/index.html', {
        'coordinates': coordinates
    })
