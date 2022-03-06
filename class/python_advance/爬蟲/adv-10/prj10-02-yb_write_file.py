import pandas as pd
import requests
import matplotlib.pyplot as plt
from tkinter import*

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
response = requests.get(base_url)
info = response.json()

df = pd.DataFrame(None,columns = ["Position","Total","Remain"])
print(df)
i = 0;
area = input("請輸入地區:")
for num in info["retVal"]:
        if info["retVal"][num]["sarea"] == area :
            position = (info["retVal"][num]["sna"].split("(")[0])
            total = (int(info["retVal"][num]["tot"]))
            remain_bike = (int(info["retVal"][num]["sbi"]))
            df.loc[i] = [position,total,remain_bike]
            i+=1
print(df)
df.to_csv("adv-10/Youbike_Info.csv")
df.to_excel("adv-10/Youbike_Info.xls")