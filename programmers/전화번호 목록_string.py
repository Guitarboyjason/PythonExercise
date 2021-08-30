phone_book = ["119", "97674223", "1195524421"]

phone_book.sort()

for i in range(len(phone_book-1)):
    if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        print(1)
print(2)
