
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import color_data

def get_color(number):
	if number < x[0]:
		return colors[0]
	elif number >= x[0] and number < x[1]:
		return colors[0]
	elif number >= x[1] and number < x[2]:
		return colors[1]
	elif number >= x[2] and number < x[3]:
		return colors[2]
	elif number >= x[3] and number < x[4]:
		return colors[3]
	elif number >= x[4] and number < x[5]:
		return colors[4]
	elif number >= x[5] and number < x[6]:
		return colors[5]
	elif number >= x[6] and number < x[7]:
		return colors[6]
	elif number >= x[7] and number < x[8]:
		return colors[7]
	elif number >= x[8] and number < x[9]:
		return colors[8]
	elif number >= x[9] and number < x[10]:
		return colors[9]
	elif number >= x[10] and number < x[11]:
		return colors[10]
	elif number >= x[11] and number < x[12]:
		return colors[11]
	elif number >= x[12]:
		return colors[12]

# for year in years:
# 	print "<div class='row'><div class='col-md-3'><img src=\"songs_{}.png\"></div></div>".format(str(year))

def plot_whole_timeperiod(save=False):
	# Get the average color for every year
	av_c = []
	av = 0
	for i in range(len(color_data.c)):
		
		if(i!= 0 and i%100 == 0):
			av_c.append(av/100.)
			av = 0
		else:
			av += color_data.c[i]
		
	av_c_r = []
	for i in av_c:
		av_c_r.append(get_color(i))

	years = [x for x in range(1965, 2016)]

	ones = np.ones(len(years))

	barlist = plt.bar(years, ones, width=1)
	for i in range(len(barlist)):
		barlist[i].set_color(av_c_r[i])

	frame1 = plt.gca()
	plt.xlim(1965,2015)
	frame1.axes.get_yaxis().set_visible(False)
	plt.title("Sentiment of top 100 songs since 1965")

	if(save):
		plt.savefig("figure_1.png")
	else:
		plt.show()


def plot_individual_years():
	nums = [x for x in range(1,101)]
	ones_hun = np.ones(len(nums))
	years = [x for x in range(1965, 2016)]
	counter = 0
	for year in years:
		barlist = plt.bar(nums, ones_hun, width=1)
		for i in range(len(barlist)):
			barlist[i].set_color(color_data.c_r[i+counter])
		counter += 100
		frame1 = plt.gca()
		plt.xlim(1,101)
		frame1.axes.get_yaxis().set_visible(False)
		plt.title("Sentiment of top 100 songs {}".format(str(year)))

		plt.savefig("songs_{}.png".format(str(year)))

def plot_individual_years_bar():
	year = 1965
	for i in xrange(0,len(color_data.c),100):
		num = []
		for j in xrange(i,i+100):
			num.append(color_data.c[j])
		plt.plot(num)
		plt.ylim(-1.5,1.5)
		plt.savefig("bar_songs_{}.png".format(str(year)))
		plt.clf()
		year += 1




if __name__ == "__main__":

	# plt.plot(years, av_c)	
	df=pd.read_csv('info.csv', sep=',',header=None)
	li= np.array(df.values)


	s = SentimentIntensityAnalyzer()
	# s.polarity_scores(str(li[i][4]))['compound']
	# BLUE: 1240AB - 1196203
	# YELLOW: FFAA00 - 16755200

	colors_rgb = ["rgb(18,64,171)", "rgb(38,73,157)", "rgb(58,82,142)", "rgb(77,91,128)", "rgb(97,99,114)", "rgb(117,108,100)", "rgb(136,117,85)", "rgb(156,126,71)", "rgb(176,135,57)", "rgb(196,144,43)", "rgb(215,152,28)", "rgb(235,161,14)", "rgb(255,170,0)"]
	colors = ["#1240ab", "#26499d", "#3a528e", "#4d5b80", "#616372", "#756c64", "#887555", "#9c7e47", "#b08739", "#c4902b", "#d7981c", "#eba10e", "#ffaa00"]
	x = np.linspace(-1,1,len(colors))


	# plot_whole_timeperiod()
	# plot_individual_years()
	plot_individual_years_bar()



