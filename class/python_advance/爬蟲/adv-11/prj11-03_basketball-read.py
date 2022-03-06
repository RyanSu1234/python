import pandas as pd
import matplotlib.pyplot as plt
from tkinter import*
import requests, json

df = pd.DataFrame(None,columns = ["Date","Home","Cust"])

def createLabels(data):                                         
    for item in data:                                         
        height = item.get_height()   
        plt.text(                                         
        item.get_x() + item.get_width() / 2,                                         
        height,                                         
        str(height),
        ha="center", #
            )        
for i in range(1, 11):
    base_url = "https://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&gameDate="                                        
    date_time=("2021-11-%d" % i)                                         
    send_url = base_url + "2021-11-" + str(i) + "&locale=zh_TW&tz=%2B8"                                         
    print(send_url)                  
                                                                                 
    response = requests.get(send_url)                                         
    info = response.json()                                         
                                         
    data = info ["payload"]["date"]["games"]                                         
                                                                                     
    home_win=0;                                         
    cust_win=0;                                         
                                         
                                         
    for num in range(len(data)):                                         
        if data[num]["boxscore"]["awayScore"] > data[num]["boxscore"]["homeScore"]:                                         
            cust_win+=1
            print(cust_win)                                      
        else:                                         
            home_win+=1
            print(home_win)                                          
    
    df.loc[i] = [date_time ,home_win ,cust_win]

print(df)
df.to_csv("adv-11/Info.csv")