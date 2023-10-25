from datetime import datetime

start = datetime.now()
print(start)
while True:
    if (datetime.now() - start).seconds == 1:
        start = datetime.now()
        print(start)
