from datetime import datetime

minf = datetime.now().time().minute +1

c = 0
while True:
    print(datetime.now().time().second)

    if datetime.now().time().second == 59:
        c += 1

    if datetime.now().time().minute >= minf:
        break

print(c)
