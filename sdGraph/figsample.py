import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
    
# CSVファイルの読み込み
# sampleplot: 1列目に横軸の系列，以降3列ごとに系列データ
filename = r"sdGraph\sampleplot.csv"
data = pd.read_csv(filename)
    
# 変位データ (横軸)
displacement = data.iloc[:, 0].values
    
# 各系列のデータを取得
series1_data = data.iloc[:, 1:4].values
series2_data = data.iloc[:, 4:7].values
series3_data = data.iloc[:, 7:10].values

# 各変位における平均と標準偏差を計算
mean_series1 = np.mean(series1_data, axis=1)
std_series1 = np.std(series1_data, axis=1)
    
mean_series2 = np.mean(series2_data, axis=1)
std_series2 = np.std(series2_data, axis=1)

mean_series3 = np.mean(series3_data, axis=1)
std_series3 = np.std(series3_data, axis=1)
    
# グラフの描画
plt.figure(figsize=(10, 6))
    
#colorオプションで系列の色を変更
#lwオプションで線の太さを変更
# 系列1
plt.plot(displacement, mean_series1, color="orange", lw=4)  
plt.fill_between(displacement, mean_series1 - std_series1, mean_series1 + std_series1,
                color="orange", alpha=0.2)
    
# 系列2
plt.plot(displacement, mean_series2, color="green", lw=4) 
plt.fill_between(displacement, mean_series2 - std_series2, mean_series2 + std_series2,
                color="green", alpha=0.2)
    
# 系列3
plt.plot(displacement, mean_series3, color="red", lw=4)  
plt.fill_between(displacement, mean_series3 - std_series3, mean_series3 + std_series3,
                color="red", alpha=0.2)
    
# 軸範囲の設定
#plt.xlim(0, 18.0)
#plt.ylim(0) 
    
# 軸目盛りのフォントサイズ設定
plt.tick_params(axis='both', which='major', labelsize=24)
# 枠線を太くする
plt.gca().spines['top'].set_linewidth(3)
plt.gca().spines['right'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)
plt.gca().spines['bottom'].set_linewidth(3)
plt.grid(True)
plt.show()
