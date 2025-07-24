"""
Task 2: Film Night Prep
You're helping your community plan a Friday Film Night for kids. The initial list of movie genres to be shown includes:
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

1. Add the genre "Drama" at the end of the list because parents requested it.
2. Someone mistakenly added "Fantasy" twice. Make sure there's only one "Fantasy" in the list.
3. The organizer wants to know how many genres are now planned to be shown.
4. Display the second and second-to-last genres to verify diversity.

→ Modify the list and display the required results.
"""

# Initial list of genres
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

# Question 1
genres.append("Drama")
print(genres)

# Question 2 
while genres.count("Fantasy") > 1:
    genres.remove("Fantasy")
print(genres)

# Question 3
genre_count = len(genres)
print(genres)
second_genre = genres[1]
second_last_genre = genres[-2]

print("Final Genre List:", genres)
print("Total Number of Genres:", genre_count)
print("Second Genre:", second_genre)
print("Second-to-Last Genre:", second_last_genre)

