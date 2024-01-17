from DataAnalysis import DataAnalysis
from TestClass import TestClass
from Plotting import Plottiing
from datetime import datetime
def WriteLog(log:str):
    with open("error.txt","a") as logFile:
        logFile.writelines(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}:  {log}")

try:
    testClass = TestClass()
    dataAnalysis = DataAnalysis(testClass.MakeSampleData())
    plot = Plottiing(8,12)
    dataAnalysis.CleanData()
    dataAnalysis.CalculateTotalRevenue()
    dataAnalysis.GetMonthlySalesReport()
    dataAnalysis.GetBestPerformingProduct()
    plot.PlotBarGraph(dataAnalysis)
except Exception as exc:
    WriteLog(f"Error msg: {str(exc)}")



