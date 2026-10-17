text = input("camelCase: ")
snake = ""
for ch in text:
    if ch.isupper():
        snake += "_" + ch.lower()
    else:
        snake += ch

print("snake_case:", snake)
