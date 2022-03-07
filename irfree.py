import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from galvani import BioLogic as BL

#file=input('ファイル名')

mpr=BL.MPRfile('none.mpr')

df=pd.DataFrame(mpr.data)
print(df)
#ファイル読み込み

res=float(input("直列抵抗を入力"))

df["overvoltage"]=df["I/mA"]*res/1000
#過電圧定義＆計算
df["irfree"]=df["Ewe/V"]-df["overvoltage"]
#irfree定義＆計算

df.to_csv('myfile3.csv')
#計算したdfを新しいファイルに書き出す

#plt.scatter(df["I/mA"],df["irfree"],label="junkan") 
plt.scatter(df["I/mA"],df["Ewe/V"],label="none")#第一引数に横軸の配列，第二引数に縦軸の配列

plt.xlabel('I/mA',fontsize=30)
plt.ylabel('Ewe/V',fontsize=30)

#plt.xlabel('current[mA]',fontsize=30) #横軸ラベル名
#plt.ylabel('voltage[V]',fontsize=30) #縦軸ラベル名
plt.tick_params(labelsize=30)#軸の目盛りのフォントサイズ
plt.legend()
plt.legend(loc="lower right",borderaxespad=0,fontsize=50,markerscale=6)
plt.grid()
# plt.ylim(1100,1400)#y軸の範囲
plt.show()