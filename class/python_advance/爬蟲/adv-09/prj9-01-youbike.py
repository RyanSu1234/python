import requests

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

response = requests.get(base_url)
info = response.json()

#print(info)

for i in range(1,11):
    num=("%04d"%i)
    print("車站站名:%s"%info["retVal"][num]["sna"].split("(")[0])
    print("總共車輛:%s"% int(info["retVal"][num]["tot"]))
    print("目前停輛數:%s\n"% int(info["retVal"][num]["sbi"]))
    
    
        




