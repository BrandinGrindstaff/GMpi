#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from glob import glob


if __name__ == '__main__':
	files = glob("sensorOutput*.txt")
	DFs   = [pd.read_csv(f) for f in files]
	data  = pd.concat(DFs[3:])
	f, axarr = plt.subplots(nrows=3, figsize=(18,10))
	plt.xticks(rotation=45, ha='right')
	plt.suptitle("Sensor Readings")
	sns.set(style="white")
	sns.despine(bottom=True, left=True)
	sns.boxplot(x="date", y="lux", data=data, color="y", ax=axarr[0])
	sns.boxplot(x="date", y="temp", data=data, color="r", ax=axarr[1])
	sns.boxplot(x="date", y="humidity", data=data, color="b", ax=axarr[2])
	axarr[0].set_xticks([])
	axarr[0].set_xlabel('')
	axarr[1].set_xticks([])
	axarr[1].set_xlabel('')
	axarr[2].set_xlabel('')
	plt.savefig("SensorOutput.pdf")