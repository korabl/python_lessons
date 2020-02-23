import json

dataProfit = []
avProfit = {}
firmProfit = {}

with open('task7.txt', 'r') as f:
    for line in f:
        dataSplit = line.split()
        profit = int(dataSplit[2]) - int(dataSplit[3])
        firmProfit.setdefault(dataSplit[0], profit)
    dataProfit.append(firmProfit)

sumProfit = 0
i = 1
for key in firmProfit:
    currentValue = int(firmProfit[key])
    if currentValue > 0:
        sumProfit += currentValue
        profit = sumProfit / i
        i += 1
        avProfit.setdefault('averageProfit', profit)
dataProfit.append(avProfit)


with open('task7_data.json', 'w') as f:
    json.dump(dataProfit, f)

