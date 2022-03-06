import requests
import matplotlib.pyplot as plt
from tkinter import*

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

def clear_fun():
    status.config(text="",fg="white",bg="white")

def youbike_list():
    response = requests.get(base_url)
    info = response.json()
    #print (send_url)

    area = pos_info.get()
    show_info = ""

    position =[]
    total_bike = []
    remain_bike = []

    for i in range(1,len(info["retVal"])):
            num=("%04d"%i)
            if num in info["retVal"].keys() and info["retVal"][num]["sarea"] == area :
                position.append(info["retVal"][num]["sna"].split("(")[0])
                total_bike.append(int(info["retVal"][num]["tot"]))
                remain_bike.append(int(info["retVal"][num]["sbi"]))
    for i in range(len(position)):
        show_info += ("%s 總共車輛=%d 剩餘車輛=%d\n" %(position[i],total_bike[i],remain_bike[i]))
    
    status.config(text=show_info)

    plt.plot(position, total_bike,"b-.",label="總共車輛")
    plt.plot(position, remain_bike,"y--",label="剩餘車輛")
    plt.legend(loc="upper left")
    plt.show()

windows =Tk()
windows.title("youbike 資訊")

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

pos=Label(windows,text="請輸入地區名稱", font=('Arial', 10))
pos.pack()

pos_info=Entry(windows)
pos_info.pack()

status=Label(windows, text='')
status.pack()

btn=Button(windows, text="獲取資訊", command=youbike_list, bg="blue")
btn.pack()
    
btn2 = Button(windows, text="清理", command=clear_fun)
btn2.pack()
windows.mainloop()