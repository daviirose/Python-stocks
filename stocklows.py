import matplotlib.pyplot as plt
import pandas as pd
import csv

months = []
msft = []
btc = []
fx = []
with open("lows.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        months.append(row[0])
        msft.append(int(row[1]))
        btc.append(int(row[2]))
        fx.append(int(row[3]))

plt.plot(months, msft, label ='MSFT')
plt.plot(months, btc, label ='BTC')
plt.plot(months, fx, label ='FX')
plt.xlabel('Months')
plt.ylabel('Amount')
plt.grid('true')
plt.legend()
plt.show()