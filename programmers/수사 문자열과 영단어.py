numbers = ["zero","one","two","three","four","five",\
    "six","seven","eight","nine"]
num = ["0","1","2","3","4","5","6","7","8","9"]
s = "one4seveneight"
answer = ""

while s != "":
    if s[0] in num:
        answer += s[0]
        s = s[1:]
    else :
        if s[0:3] in numbers:
            answer += str(numbers.index(s[0:3]))
            s = s[3:]
        elif s[0:4] in numbers:
            answer += str(numbers.index(s[0:4]))
            s = s[4:]
        else:
            answer += str(numbers.index(s[0:5]))
            s = s[5:]
print(answer)