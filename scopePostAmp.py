import os
import codecs
import csv
import numpy as np
import dataFinder 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"

dataFile = codecs.open(dir_path+"/data/"+"scope after amp.csv", encoding="utf-8", errors="ignore")
skipLinesStart = 27
skipLinesEnd = None
t,V= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
dataFile.close()



t = np.array([element for element in t],dtype=float)
V = np.array([element for element in V],dtype=float)




def detect_peaks(time, voltage, min_height=None, min_distance=0, slope_tol=0):
    peaks = []
    N = len(voltage)

    last_peak_index = -min_distance  # allows the first peak

    for i in range(1, N-1):
        # Basic peak check (local maximum)
        if not (voltage[i] > voltage[i-1] and voltage[i] > voltage[i+1]):
            continue

        # Height threshold
        if min_height is not None and voltage[i] < min_height:
            continue

        # Minimum distance between peaks
        if i - last_peak_index < min_distance:
            continue

        # Slope check
        left_slope  = voltage[i] - voltage[i-1]
        right_slope = voltage[i] - voltage[i+1]

        if left_slope < slope_tol or right_slope < slope_tol:
            continue

        # Accept the peak
        peaks.append(i)
        last_peak_index = i

    # Convert peak indices to peak times
    peak_times = [time[i] for i in peaks]

    return peaks, peak_times




peaks, peak_times = detect_peaks(
    t,
    V,
    min_height=0.1,    # choose based on your signal
    min_distance=50,   # # of samples between peaks
    slope_tol=0     # reject “flat” or noisy wiggles
)

print("Number of peaks:", len(peaks))
print("Peak indices:", peaks[:10])
print("Peak voltages:", [V[i] for i in peaks[:10]])
print("Peak times:", peak_times[:10])


# Periods between peaks
periods = [peak_times[i+1] - peak_times[i] for i in range(len(peak_times)-1)]

# Average period
T_avg = sum(periods) / len(periods)

# Frequency
frequency = 1 / T_avg

print("Frequency:", frequency, "Hz")





plt.figure(figsize=(12,8))
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=t[0], color="black", linewidth=1)


for i in peaks:
    plt.axvline(x=t[i]*1000-t[0]*1000, color="black", linewidth=1)



plt.plot(
    t*1000-t[0]*1000,
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

plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f V"))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f ms"))



plt.xlabel("tid [S]", fontsize=12)
plt.ylabel("Spenning [V]", fontsize=12)

plt.title(
    f"Måling av utgangsignal y(t)", fontweight="bold"
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
# plt.savefig("./bilder/ytplotscope.png")
plt.show()