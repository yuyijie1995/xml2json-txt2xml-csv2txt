import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
# %matplotlib inline

def extract_log(log_origin, thresh_value):
	images = []
	points = []


	f_origin = open(log_origin)
	for line in f_origin:
		image = line.split(' ')[0] + '.jpg'
		
		# 低于阈值则跳过
		p = float(line.split(' ')[5])
		if p < thresh_value:
			continue

		# xmin = float(line.split(' ')[2])
		# ymin = float(line.split(' ')[3])
		# xmax = float(line.split(' ')[4])
		# ymax = float(line.split(' ')[5])
		# xmin = int(float(line.split(' ')[1]) )
		# ymin = int(float(line.split(' ')[2]) )
		# xmax = int(float(line.split(' ')[3]) )
		# ymax = int(float(line.split(' ')[4]) )

		xmin = int(float(line.split(' ')[1]) + 0.5)
		ymin = int(float(line.split(' ')[2]) + 0.5)
		xmax = int(float(line.split(' ')[3]) + 0.5)
		ymax = int(float(line.split(' ')[4]) + 0.5)


		images.append(image)
		points.append(str(xmin)+' '+str(ymin)+' '+str(xmax)+' '+str(ymax))

	f_origin.close()


	full = os.listdir('./test')
	empty = list(set(images)^set(full))
	all_images = images + empty

	num_of_empty = len(empty)
	for _ in range(num_of_empty):
		points.append('')
	




	
	dataframe = pd.DataFrame({'ID':all_images,'Label':points})
	dataframe.to_csv("result/test.csv",index=False,sep=',')	#将DataFrame存储为csv,index表示是否显示行名，default=True


if __name__ == '__main__':
	extract_log('./result_2018_8_7_res152_100.txt', 0.4)