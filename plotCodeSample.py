import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"very noce frekresponm.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 27
skipLinesEnd = None
f,A= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



f = np.array([element for element in f],dtype=float)
A = np.array([element for element in A],dtype=float)

AStoppVal =  dataFinder.findValueInterpolate(f,4500,A)
fCPoint =  dataFinder.findValueInterpolate(A,-3,f)
plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=f[0], color="black", linewidth=1)

plt.axvline(x=fCPoint,linestyle="--",  color="green", linewidth=1,label=f"Knekkfrekvens fc {fCPoint:.0f}Hz (ved -3dB)")
plt.axhline(y=-3,linestyle="--",  color="green", linewidth=1)


plt.axhline(y=AStoppVal,linestyle="--",  color="purple", linewidth=1)
plt.axvline(x=4500,linestyle="--",  color="purple", linewidth=1,label=f"A_stopp {AStoppVal:.2f}dB (ved 4.5kHz)")

plt.plot(
    f,
    A,
    linewidth=2,
    color="royalblue",
    label="Amplitude respons"
)
# plt.plot(
#     t,
#     noise,
#     linewidth=2,
#     color="crimson",
#     label="vo"
# )

# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f V"))
# plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.3f V"))



plt.xlabel("Frekvens [Hz]", fontsize=12)
plt.ylabel("Amplitude [dB]", fontsize=12)

plt.title(
    f"Amplituderespons med punkter ved 1V", fontweight="bold"
)

plt.xscale("log")
# plt.yscale("log")
plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()

# plt.xticks([200,1000,2000,3000,3500,4500,6000,7000,8000,9000,10000])
plt.yticks([-3,-10,-20,-30,-40,-50])


# plt.show()
# plt.plot(
#     np.linspace(0,len(vivo[1]),len(vivo[1])),
#     vivo[1]-V0,
#     linewidth=2,
#     color="royalblue",
#     label="vi"
# )
plt.savefig("./bilder/Aprespons.png")
plt.show()