import requests
import matplotlib.pyplot as plt
base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"



response = requests.get(base_url)
info = response.json()
#print (send_url)






for i in range(1,len(info["retVal"])):
        num=("%04d"%i)
        if num in info["retVal"].keys() and info["retVal"][num]["sarea"] == "松山區":
            print("車站站名:%s"%info["retVal"][num]["sna"].split("(")[0])
            print("地區:%s"%info["retVal"][num]["sarea"])
            print("總共車輛:%s"% int(info["retVal"][num]["tot"]))
            print("目前停輛數:%s\n"% int(info["retVal"][num]["sbi"]))
            
    
