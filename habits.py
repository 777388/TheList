import sys
print("usage: python3 habits.py <4976 <228775")
tip = 0
black = ""
with open("justbusiness", "r") as f:
    for line in f:
        if tip == int(sys.argv[1]):
            black += line+" "
            break
        else:
            tip += 1
            continue
shake = 0
with open("titles", "r") as d:
    for lines in d:
        if shake == int(sys.argv[2]):
            black += lines
            break
        else:
            shake += 1
            continue
print(black)
d.close()
f.close()