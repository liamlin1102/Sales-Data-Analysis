import pandas as pd
class TestClass:
    def __init__(self):
        return 
    #生成測試資料，回傳路徑
    def MakeSampleData(self)->str:
        title = ["Date","Product","Units Sold","Unit Price"]
        sampleDatas = [
        ["2023-01-01","Product A",100,10],
        ["2023-01-01","Product B",150,8],
        ["2023-01-02","Product A",120,10],
        ["2023-01-02","Product B",180,8],
        ["2023-02-01","Product A",80,12],
        ["2023-02-01","Product B",100,10],
        ["2023-02-02","Product A",90,12],
        ["2023-02-02","Product B",110,10],
        ["2023-03-01","Product A",150,15],
        ["2023-03-01","Product B",200,12],
        ["2023-03-02","Product A",120,15],
        ["2023-03-02","Product B",180,12]
                ]
        dataDictionary = {}
        #透過迴圈的方式生成dictionary來產生dataframe
        for data in sampleDatas:
            for index in range(len(data)):
                if not title[index] in dataDictionary:
                    dataDictionary[title[index]]=[]
                dataDictionary[title[index]].append(data[index])
        dataFrame = pd.DataFrame(dataDictionary)
        dataFrame["Date"] = pd.to_datetime(dataFrame["Date"])
        path = "SamepleData.csv"
        dataFrame.to_csv(path,index=False)
        return path