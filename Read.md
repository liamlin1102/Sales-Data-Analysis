# 報價資料整理並繪圖
## 專案介紹:
- DataAnalysis.py: 資料清洗及整理之函數庫
    - DataAnalysis(DataPath:str): 輸入檔案路徑初始化，使該物件讀取Csv檔案
    - CleanData(): 檢查數據中是否有缺失值或不一致之處。如果型態轉換失敗(日期轉換、數字轉換)會設定NaN，之後一起drop掉
    - CalculateTotalRevenue(): 計算Total Revenue，使用公式為Unit Sold*Unit Price
    - GetMonthlySalesReport(): 生成包含每個月每個產品的銷售報告
    - GetBestPerformingProduct(): 回傳Total Revenue最大的商品
- Plotting.py: 畫圖函數庫
    - Plottiing(weight:int,height:int,dpi:int=100,facecolor:str="white",edgecolor:str="black",linewidth:int=0,frameon:bool=True): 除了畫布的長寬之外都可以用預設的，不需特別輸入
    - PlotBarGraph(dataAnalysis:DataAnalysis): 輸入存放data的instance，會自動繪畫長條圖
    - PlotClear(): 清除Plot畫布
- TestClass.py: 產生預設測試資料data
    - MakeSampleData(): 產生預設測試資料，會回傳產生檔案名稱(預設產生在code同層資料夾下方)

## 快速使用:
可直接