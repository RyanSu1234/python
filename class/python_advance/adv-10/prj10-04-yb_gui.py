import pandas as pd
import requests
import matplotlib.pyplot as plt
from tkinter import*

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x() + item.get_width() / 2,
            height,
            str(height),
            ha="center", #
        )

def read_youbike ():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

    response = requests.get(base_url)
    info = response.json()

    df = pd.read_csv("adv-10/Youbike_Info.csv",encoding="utf8")

    Position = df.loc[:,"Position"]
    Total = df.loc[:,"Total"]
    Remain = df.loc[:,"Remain"]

    print(Position)
    print(Total)
    print(Remain)

    A = plt.bar(Position[:10], Total[:10],label="全部停車格")
    B = plt.bar(Position[:10], Remain[:10],label="剩餘車輛")

    createLabels(A)
    createLabels(B)

    plt.legend(loc=1)
    plt.show()


def write_youbike():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(base_url)
    info = response.json()

    df = pd.DataFrame(None,columns = ["Position","Total","Remain"])
    print(df)
    i = 0;
    area = pos_info.get()
    for num in info["retVal"]:
            if info["retVal"][num]["sarea"] == area :
                position = (info["retVal"][num]["sna"].split("(")[0])
                total = (int(info["retVal"][num]["tot"]))
                remain_bike = (int(info["retVal"][num]["sbi"]))
                df.loc[i] = [position,total,remain_bike]
                i+=1
    print(df)
    df.to_csv("adv-10/Youbike_Info.csv")
    status.config(text="儲存成功")

#print(df)


windows =Tk()
windows.title("youbike 資訊")

pos=Label(windows,text="請輸入地區名稱", font=('Arial', 12))
pos.pack()

pos_info=Entry(windows)
pos_info.pack()

status=Label(windows, text='')
status.pack()

btn=Button(windows, text="儲存資訊", command=write_youbike, bg="blue")
btn.pack()
    
btn2 = Button(windows, text="顯示資訊", command=read_youbike)
btn2.pack()
windows.mainloop()