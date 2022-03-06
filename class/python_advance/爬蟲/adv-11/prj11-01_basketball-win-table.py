import pandas as pd
import matplotlib.pyplot as plt
from tkinter import*
import requests, json


base_url = "https://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&gameDate=2021-11-1&locale=zh_TW&tz=%2B8"



def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
        item.get_x() + item.get_width() / 2,
        height,
        str(height),
        ha="center", #
            )

response = requests.get(base_url)
info = response.json()

data = info ["payload"]["date"]["games"]


home_win=0;
cust_win=0;


for num in range(len(data)):
    if data[num]["boxscore"]["awayScore"] > data[num]["boxscore"]["homeScore"]:
        cust_win+=1
    else:
        home_win+=1



A = plt.bar("2021-11-1", home_win, label="主場勝")
B = plt.bar("2021-11-1", cust_win, label="客場勝")

createLabels(A)
createLabels(B)

plt.legend(loc=1)
plt.show()

















