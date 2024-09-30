favorite_movies = [
    ("Violent Night", 2022),
    ("The Matrix", 1999),
    ("Puss in Boots: The Last Wish", 2022),
    ("Zoolander", 2001),
    ("Zathura: A Space Adventure", 2005)
]

def check_movie_release(movie):
    name, release_year = movie
    if release_year < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return name

recent_movies = []

for movie in favorite_movies:
    result = check_movie_release(movie)
    if result is not None:
        recent_movies.append(movie)

print(recent_movies)

