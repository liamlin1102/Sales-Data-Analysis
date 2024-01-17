import pandas as pd
class DataAnalysis:
    #預設產生全報表跟月報表
    def __init__(self,dataPath:str):
        self.dataFrame = pd.read_csv(dataPath)
        self.monthSalesReport = pd.DataFrame()
    #清理資料，將型別異常跟NaN資料給drop掉    
    def CleanData(self)->None:
        self.dataFrame["Date"] = pd.to_datetime(self.dataFrame["Date"], errors="coerce")
        intValueList = ["Units Sold","Unit Price"]
        for colunn in intValueList:
            self.dataFrame[colunn] = pd.to_numeric(self.dataFrame[colunn], errors='coerce')
        self.dataFrame.dropna(inplace=True)  
        self.dataFrame.reset_index(drop=True, inplace=True) 
    #計算Total Revenue
    def CalculateTotalRevenue(self)->None:
        self.dataFrame["Total Revenue"] = self.dataFrame["Units Sold"]*self.dataFrame["Unit Price"]
    #透過月份跟商品來分組後計算總合後整理成月份報表
    def GetMonthlySalesReport(self):
        self.dataFrame["Month"] = self.dataFrame["Date"].dt.month
        self.monthSalesReport = self.dataFrame.groupby(["Month", "Product"]).agg({"Units Sold":"sum","Total Revenue":"sum"}).reset_index()
        return self.monthSalesReport
    #取商品分類的Total Revenue最大值
    def GetBestPerformingProduct(self):
        return self.dataFrame.groupby("Product")["Total Revenue"].sum().idxmax()
