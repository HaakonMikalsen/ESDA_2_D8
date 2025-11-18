import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"spectrumNoise.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 32
skipLinesEnd = None
f,A,deg= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



f = np.array([element for element in f],dtype=float)
A = np.array([element for element in A],dtype=float)

a,b = np.polyfit(f,A,1)
print("a")
n = len(f)
x = np.linspace(0,f[-1],n)
y = a*x +b
print(np.mean(A))


plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=np.mean(A), color="black", linestyle="--", linewidth=1)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.axvline(x=2040, color="black", linewidth=1)

plt.plot(
    f,
    A*1000,
    linewidth=2,
    color="royalblue",
    label="s(t)"
)
plt.plot(
    x,
    y*1000,
    linewidth=2,
    color="crimson",
    label="Gjennomsnittlig spektrum"
)
# plt.plot(
#     t,
#     noise,
#     linewidth=2,
#     color="crimson",
#     label="vo"
# )

plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f Hz"))
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f mV"))



plt.xlabel("Frekvens [Hz]", fontsize=12)
plt.ylabel("RMS Spenning [Ṽ]", fontsize=12)

plt.title(
    f"Spektrumsanalyse av s(t)", fontweight="bold"
)

# plt.xscale("log")
# plt.yscale("log")
plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()

# plt.xticks([200,1000,2000,3000,3500,4500,6000,7000,8000,9000,10000])
# plt.yticks([-3,-10,-20,-30,-40,-50])


# plt.show()
# plt.plot(
#     np.linspace(0,len(vivo[1]),len(vivo[1])),
#     vivo[1]-V0,
#     linewidth=2,
#     color="royalblue",
#     label="vi"
# )
# plt.savefig("./bilder/stoyspec.png")
plt.show()