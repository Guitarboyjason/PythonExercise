genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500,600,150,800,2500]


genres_arr = []

for i in range(len(genres)):
    if genres[i] in genres_arr:
        genres_arr.append([genres[i], plays[i]])
    else:
        genres_arr[genres_arr.index(genres[i])]
