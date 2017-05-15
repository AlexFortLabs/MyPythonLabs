mesage = 'It was a bright cold day in April, and the cloks wehre striking thirteen.'
count = {}
for bukwa in mesage:
    count.setdefault(bukwa, 0)
    count[bukwa] = count[bukwa] + 1

print(count)
