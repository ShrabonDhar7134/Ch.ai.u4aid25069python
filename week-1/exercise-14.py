# Exercise 14: Favourite Movies List (Simple Version)

movies = []   # empty list

print("Favourite Movies Collection")
print("Please enter 5 of your favourite movies.\n")

count = 1

while count <= 5:
    movie = input(f"Enter movie {count}: ")
    movies.append(movie)
    count += 1

print("You have entered all your favourite movies.")
print("Here is your movie list:")

for m in movies:
    print("-", m)
