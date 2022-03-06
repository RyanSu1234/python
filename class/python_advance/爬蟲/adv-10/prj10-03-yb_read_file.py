import pandas as pd
import matplotlib.pyplot as plt

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x() + item.get_width() / 2,
            height,
            str(height),
            ha="center", #
        )

df = pd.read_csv("adv-10/Youbike_Info.csv",encoding="utf8")

#print(df)

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
