import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"scope.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 27
skipLinesEnd = None
t,V= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



t = np.array([element for element in t],dtype=float)
V = np.array([element for element in V],dtype=float)

plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=t[0], color="black", linewidth=1)



plt.plot(
    t,
    V,
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

plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()

# plt.xticks([200,1000,2000,3000,3500,4500,6000,7000,8000,9000,10000])


# plt.show()
# plt.plot(
#     np.linspace(0,len(vivo[1]),len(vivo[1])),
#     vivo[1]-V0,
#     linewidth=2,
#     color="royalblue",
#     label="vi"
# )
# plt.savefig("./bilder/Aprespons.png")
plt.show()