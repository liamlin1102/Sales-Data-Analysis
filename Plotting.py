import matplotlib.pyplot as plt
from DataAnalysis import DataAnalysis
class Plottiing:
    #設定畫布，如果不需要調整其餘資料只需設定畫布大小(圖片)
    def __init__(self,weight:int,height:int,dpi:int=100,facecolor:str="white",edgecolor:str="black",linewidth:int=0,frameon:bool=True):
        self.plt = plt
        self.plt.figure(figsize=(weight,height),dpi=dpi,facecolor=facecolor,edgecolor=edgecolor,linewidth=linewidth,frameon=frameon)
    #畫長條圖的功能，將DataAnalysis類別注入來繪圖
    def PlotBarGraph(self,dataFrame:DataAnalysis):
        if(not dataFrame.monthSalesReport.empty):
            dataFrame.GetMonthlySalesReport()
        #由於相同月份會重疊在一塊，我使用*0.3的方式來讓長條圖並排，若商品之後便更多則需要調整長條圖寬度
        count = 0   
        for product, data in dataFrame.monthSalesReport.groupby("Product"):
            self.plt.bar_label(self.plt.bar(data["Month"]+count*0.3, data["Total Revenue"], label=product,width=-0.4,align="edge")) 
            count+=1
        #設定x座標的範圍
        self.plt.xticks([tick for tick in range(dataFrame.monthSalesReport["Month"].max()+2)])
        self.plt.title("Monthly Sales Report")
        self.plt.xlabel("Month")
        self.plt.ylabel("Total Revenue")
        #設定標示
        self.plt.legend()
        self.plt.show()
    #清空畫布
    def PlotClear(self):
        self.plt.clf()

    