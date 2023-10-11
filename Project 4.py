def helper():
    for y in range(5):
        yield y

count = 0
for value in helper():
    if count <=2:
        print(value)
    else:
        break
    count += 1
