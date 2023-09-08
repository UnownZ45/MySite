import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

start = dt.datetime(2023,1,1)
end =  dt.datetime.now().date()
date = str(end)

amzn = yf.download('AMZN', start , end)
cvna = yf.download('CVNA', start , end)
gme = yf.download('GME', start , end)

amzn.tail()
cvna.tail()
gme.tail()

amzn.to_csv('Amazon Stock as of ' + date)
cvna.to_csv('Carvanna Stock as of ' + date)
gme.to_csv('GameStop Stock as of ' + date)

amzn['Close'].plot(label= 'Amazon(AMZN)')
cvna['Close'].plot(label= 'Carvana(CVNA)')
gme['Close'].plot(label= 'GameStop(GME)')
plt.legend()
plt.title('Stock Close Prices 2023')
plt.ylabel('Stock Close Prices')
plt.show()