import csv
from django.shortcuts import render, redirect
from .utils import connectToDB, retrieveData, deletePoint


def index(request):
    db_connection = connectToDB(isLocal=True)
    if not db_connection:
        return render(request, 'Points/index.html', {"error": "Database connection failed."})
    if request.method == "POST":
        # Case 1: Adding a single point via form
        if "x" in request.POST and "y" in request.POST:
            x = request.POST.get("x")
            y = request.POST.get("y")
            if db_connection and x and y:
                cur = db_connection.cursor()
                cur.execute(
                    "INSERT INTO coordinates (x, y) VALUES (%s, %s)", (x, y))
                db_connection.commit()
                cur.close()
                return redirect('/')

        # Case 2: Deleting a point
        elif "delete_id" in request.POST:
            point_id = request.POST.get("delete_id")
            if db_connection and point_id:
                deletePoint(db_connection, point_id)
                return redirect('/')

        # Case 3: Uploading CSV
        elif request.FILES.get("csv_file"):
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                return render(request, 'Points/index.html', {"error": "File must be a CSV."})

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            next(reader, None)  # Skip header if present

            cur = db_connection.cursor()
            for row in reader:
                try:
                    x, y = float(row[0]), float(row[1])
                    cur.execute(
                        "INSERT INTO coordinates (x, y) VALUES (%s, %s)", (x, y))
                except Exception as e:
                    print("Error inserting row:", row, e)
            db_connection.commit()
            cur.close()
            return redirect('/')

    # Fetch coordinates for display
    coordinates = []
    if db_connection:
        coordinates = retrieveData(db_connection)
        db_connection.close()

    return render(request, 'Points/index.html', {
        'coordinates': coordinates
    })
