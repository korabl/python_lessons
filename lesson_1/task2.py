time = int(input('Время в секундах: '))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60

if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)

print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
