def printing(star):
    answer = []
    answer = [{star,star,star},{star," "*len(star),star},\
        {star,star,star}]
def printing_2(star):
    print(star," "*len(star),star)
def stars(n):
    if n == 3:
        return ("***\n* *\n***")
    else:
        return (printing(stars(n/3)))

print(stars(27))