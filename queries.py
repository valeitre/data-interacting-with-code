# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT COUNT(*) FROM directors"
    db.execute(query)
    results = db.fetchone()[0]
    return results


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "SELECT name FROM directors ORDER BY name"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """SELECT title FROM movies
    WHERE LOWER(title) LIKE '% love %'
    OR LOWER(title) LIKE 'love %'
    OR LOWER(title) LIKE '% love'
    OR LOWER(title) LIKE 'love'
    OR LOWER(title) LIKE '% love''%'
    OR LOWER(title) LIKE '% love.'
    OR LOWER(title) LIKE 'love,%'
    ORDER BY title"""
    db.execute(query)
    results = db.fetchall()

    titles = []
    for row in results:
        titles.append(row[0])
    return titles



def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"SELECT COUNT(*) FROM directors WHERE name LIKE '%{name}%'"
    db.execute(query)
    result = db.fetchall()[0][0]
    return result


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"SELECT title FROM movies WHERE minutes > {min_length} ORDER BY title"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]
