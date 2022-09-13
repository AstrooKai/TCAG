import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(13, 10), dpi = 300)

# Wind & Gust Analysis Graph:
dateTime = ['09/06 21Z', '09/7 03Z', '09/7 15Z', '09/7 21Z', '09/8 03Z', '09/8 09Z', '09/8 15Z', '09/8 21Z', '09/9 03Z', '09/9 09Z', '09/9 15Z', '09/9 21Z', '09/10 03Z', '09/10 09Z', '09/10 15Z', '09/10 21Z', '09/11 03Z', '09/11 09Z', '09/11 15Z', '09/11 21Z', '09/12 03Z', '09/12 09Z', '09/12 15Z', '09/12 21Z']
wind = [55, 65, 75, 75, 75, 75, 75, 85, 95, 100, 110, 110, 120, 130, 140, 155, 165, 165, 165, 155, 150, 140, 140, 140]
gust = [70, 80, 90, 90, 90, 90, 90, 105, 115, 125, 135, 135, 150, 160, 170, 190, 205, 205, 205, 190, 185, 170, 170, 170]

plt.subplot(2, 1, 1)
plt.plot(dateTime, wind, label = 'Max Wind: 165 km/h', color = 'g')
plt.plot(dateTime, gust, label = 'Max Gust: 205 km/h', color = 'r')
plt.axhline(y = 165, color = 'g', linestyle = 'dashed')
plt.axhline(y = 205, color = 'r', linestyle = 'dashed')
plt.xlabel('Date & Time (UTC)', fontdict = None, labelpad = None, loc = None, fontsize = 'xx-large')
plt.ylabel('Wind Speed in km/h', fontdict = None, labelpad = None, loc = None, fontsize = 'xx-large')
plt.title('Wind & Gust Analysis', fontdict = None, loc = None, pad = None, y = None, fontsize = 20)
plt.xticks(dateTime[::1], fontsize = 'large', rotation = 40)
plt.yticks(fontsize = 'large')
plt.legend(loc = 4, prop= {'size': 15})
plt.grid()

# MSLP Analysis Graph:
dateTime = ['09/06 21Z', '09/7 03Z', '09/7 15Z', '09/7 21Z', '09/8 03Z', '09/8 09Z', '09/8 15Z', '09/8 21Z', '09/9 03Z', '09/9 09Z', '09/9 15Z', '09/9 21Z', '09/10 03Z', '09/10 09Z', '09/10 15Z', '09/10 21Z', '09/11 03Z', '09/11 09Z', '09/11 15Z', '09/11 21Z', '09/12 03Z', '09/12 09Z', '09/12 15Z', '09/12 21Z']
mslp = [1004, 1002, 1000, 1000, 1000, 1000, 1000, 998, 996, 994, 992, 992, 985, 975, 970, 955, 950, 950, 955, 955, 965, 965, 965, 965]

plt.subplot(2, 1, 2)
plt.plot(dateTime, mslp, label = 'Minimum MSLP: 950 hPa', color = 'b')
plt.xlabel('Date & Time (UTC)', fontdict = None, labelpad = None, loc = None, fontsize = 'xx-large')
plt.ylabel('MSLP in hPa', fontdict = None, labelpad = None, loc = None, fontsize = 'xx-large')
plt.axhline(y = 950, color = 'b', linestyle = 'dashed')
plt.title('MSLP Analysis', fontdict = None, loc = None, pad = None, y = None, fontsize = 20)
plt.xticks(dateTime[::1], fontsize = 'large', rotation = 40)
plt.yticks(fontsize = 'large')
plt.legend(loc= 1, prop= {'size': 15})
plt.grid()

plt.subplots_adjust(left = 0.07, bottom = 0.11, right = 0.98, top = 0.85, wspace = 0.4, hspace = 0.5)
plt.figtext(0.5, 0.95, 'DOST-PAGASA Tropical Cyclone Analysis Graph', fontsize = 25, fontweight = 'bold', ha = 'center')
plt.figtext(0.5, 0.91, 'Typhoon Inday (Muifa)', fontsize = 22, ha = 'center')
plt.figtext(0.799, 0.86, 'EXPERIMENTAL', fontsize = 20, fontweight = 'bold')
plt.figtext(0.808, 0.005, 'Processed by @AstrooKai', fontsize = 'x-large') # DO NOT REMOVE THIS
plt.figtext(0, 0.005, 'As of 21Z UTC Sep 12 2022', fontsize = 'x-large')
plt.show()

# Code made by @AstrooKai
