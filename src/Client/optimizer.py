metadata = 'whitelist_metadata.csv'
whitelist = 'whitelist.txt'

wait_time = 6

import numpy as np
import pandas as pd

import time, threading


def updateWhitelist():
	srt = pd.read_csv(metadata,header=None).groupby(by=0).mean().sort_values(by=[1])
	srt.to_csv(metadata,header=None)
	pd.Series(pd.Series(srt.index).append(pd.read_csv(whitelist,header=None)).iloc[:,0].unique()).to_csv(whitelist,index=False)


def deamon():
	updateWhitelist()
	threading.Timer(wait_time, deamon).start()


if __name__ == "__main__":
    deamon()

