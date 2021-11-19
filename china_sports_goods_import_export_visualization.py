import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

def load_data(path):
	""" load data from the indicated path(file) """
	with open(path, 'r') as f:
 
 	   data = np.loadtxt(f, str, delimiter = ',', skiprows = 1)
	return data

def StrToFloat(one_darray):

	return np.array([float(i) for i in one_darray])

def split_time_in_one_darray(target_array):
    """ split the time coloumn from the array """
    date = target_array[:14,0]
    return date

def split_trade_value_in_one_darray(target_array):
    """ split the trade value coloumn from the array """
    trade_value = target_array[:14,7]
    return StrToFloat(trade_value)

def plot_raw_bar(x_data, y_data, c, pos):
	""" plot the bar with no modified parameters like axis or label or title """
	pos = int('21%d' % (pos))

	ax = plt.subplot(pos)
	ax.bar(x_data, y_data, width = 0.3, color = c)
	ax.grid(which = 'major', axis = 'both')

	return ax

def add_title_and_label(axes, title_name, x_label, y_label):
	""" add title and xlabel & ylabel to the graph """

	axes.set_title(title_name, fontsize = 16)
	axes.set_xlabel(x_label, fontsize = 12)
	axes.set_ylabel(y_label, fontsize = 12)

	
def add_legend_both(fig, ax1, ax2, legend1, legend2, location):

	fig.legend(handles = [ax1, ax2], labels = [legend1, legend2], loc = location)

def set_ylimit_xlimit(axes, y_bottom, y_top):
	""" arguments range_y or range_x are lists with two elements:[bottom, ceiling] """
	axes.set_ylim(y_bottom, y_top)

	# if len(range_y) && len(range_x) == 2:
	# 	x_bottom, x_ceil = range_x[0], range_x[1]
	# 	y_bottom, y_ceil = range_y[0], range_y[1]

	# 	#axes.set_ylim(y_bottom, y_ceil)
	# 	axes.set_xlim(x_bottom, y_ceil)
		

	# else:
	# 	print('Enter a list with only two elements\n')

def modify_yticks_major_minor(axes):
	""" to modify the intervals of ticks and its major & minor """

	axes.yaxis.set_major_locator(ticker.AutoLocator())
	axes.yaxis.set_minor_locator(ticker.AutoMinorLocator())

def add_text_on_bar_top(axes, rects):
    """ add text on the top of the bar """
    for rect in rects:
        height = rect.get_height()
        axes.text(rect.get_x() + rect.get_width()/2, height + 0.3, str(format_sci(height)), ha = 'center')

def format_sci(y):
	""" to change the formation of number into sci-numbering  """
	return '$%.1f$x$10^{8}$' % (y/100000000)

def formatnum(y, pos):
	""" to change the formation of number into sci-numbering  """
	return '$%.1f$x$10^{8}$' % (y/100000000)




if __name__ == '__main__':

	# 读取文件的绝对路径
	path_import_2007_2020 = r'D:\作业\国贸实习\data\china_sports_goods_import_2007_2020.csv'
	path_export_2007_2020 = r'D:\作业\国贸实习\data\china_sports_goods_export_2007_2020.csv'

	# with open(path_import_2007_2020, 'r') as f_import:
	#     try:
	#         sports_goods_import_data_coarse = np.loadtxt(f_import, str, delimiter = ',', skiprows = 1)
	#     except ValueError:
	#         print(sports_goods_import_data_coarse)

	# 将文件中的所有数据以数组形式导入（注意：若文件含有“字符型或字符串型”内容，则需要注明导入类型为str）
	sports_goods_import_data_coarse = load_data(path_import_2007_2020)
	sports_goods_export_data_coarse = load_data(path_export_2007_2020)

	# 对生数据进行切片，取出重要数据——时间和交易额
	date_import = split_time_in_one_darray(sports_goods_import_data_coarse)
	trade_value_import = split_trade_value_in_one_darray(sports_goods_import_data_coarse)

	date_export = split_time_in_one_darray(sports_goods_export_data_coarse)
	trade_value_export = split_trade_value_in_one_darray(sports_goods_export_data_coarse)

	# 使matplotlib能够正常显示中文字体
	plt.rcParams['font.sans-serif']=['SimHei']

	# 坐标、图例、图例位置以及标题名
	title_import = '2007-2020年中国体育用品对外进口交易额（美元）'
	title_export = '2007-2020年中国体育用品对外出口交易额（美元）'
	legend_import = '体育用品进口交易额'
	legend_export = '体育用品出口交易额'
	location = 'upper left'
	xlabel = '时间（年）'
	ylabel = '交易额（美元）'

	# 创建画布
	fig = plt.figure(dpi = 128, figsize = (8, 8))
	
	# 创建坐标图，并绘制粗图像，然后对图像进行修饰（标题、坐标、坐标轴刻度、数据显示形式）
	ax1 = plot_raw_bar(date_import, trade_value_import, 'c', 1)
	add_title_and_label(ax1, title_import, xlabel, ylabel)
	modify_yticks_major_minor(ax1)
	formatter = FuncFormatter(formatnum)
	ax1.yaxis.set_major_formatter(formatter)

	ax2 = plot_raw_bar(date_export, trade_value_export, 'b', 2)
	add_title_and_label(ax2, title_export, xlabel, ylabel)
	modify_yticks_major_minor(ax2)
	ax2.yaxis.set_major_formatter(formatter)

	# 给柱状图头添加数据标签
	rects1, rects2 = ax1.patches, ax2.patches
	add_text_on_bar_top(ax1, rects1)
	add_text_on_bar_top(ax2, rects2)

	# plt.legend(handles = [ax1, ax2], labels = [legend_import, legend_export], loc = location)

	plt.show()
	
	# y_ticks = [i for i in range(0, int(1e9), int(1e8))]
	

