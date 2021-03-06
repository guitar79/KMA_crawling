# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
http://www.kma.go.kr/repositary/image/cht/img/ghmd_s24_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/sfc3_2017082606.png
http://www.kma.go.kr/repositary/image/cht/img/surf_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up92_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up85_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up70_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up50_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up30_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up20_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/up10_2017082600.png
http://www.kma.go.kr/repositary/image/cht/img/rdps_lc30_post_grph_ft06_gph850_pa4_2017082606.s00.gif
http://www.kma.go.kr/repositary/image/cht/img/rdps_lc30_post_grph_ft06_dft850_pa4_2017082606.s00.gif
http://www.kma.go.kr/repositary/image/cht/img/rdps_lc30_post_grph_ft06_tmpwnd_pa4_2017082606.s00.gif
http://www.kma.go.kr/repositary/image/cht/img/rdps_lc30_post_grph_ft06_wnd850_pa4_2017082606.s00.gif
http://www.kma.go.kr/repositary/image/cht/img/rww3_wind_ft03_pa4_s000_2017082600.gif
http://www.kma.go.kr/repositary/image/cht/img/rdps_lc30_post_grph_fxko4s_pb4_2017082606.gif
http://www.kma.go.kr/repositary/image/cht/img/n500_anlmod_pb4_2017082606.gif
http://www.kma.go.kr/repositary/image/cht/img/surf_newsur_pa4_2017082606.gif
http://www.kma.go.kr/repositary/image/cht/img/kor1_anlmod_pb4_2017082610.gif
http://www.kma.go.kr/repositary/image/cht/img/r3oi_lc30_anal_axfe01_pb4_2017082606.gif
http://www.kma.go.kr/repositary/image/cht/img/r3oi_lc30_anal_axfe02_pb4_2017082606.gif
"""
import urllib.request
from pathlib import Path
from datetime import time
from datetime import date
from datetime import timedelta
chl1 = ["ghmd_s24","sfc3","surf","up92","up85","up70","up50","up30","up20","up10"]
chl2 = ["rww3_wind_ft03_pa4_s000","n500_anlmod_pb4","surf_newsur_pa4","kor1_anlmod_pb4","r3oi_lc30_anal_axfe01_pb4","r3oi_lc30_anal_axfe02_pb4","up50","up30","up20","up10"]
day = date.today()
for d in range(1,10):
	today = day.strftime("%Y%m%d")
	#print(today)
	for Ho in range(0,23,3):
		for i in chl1:
			url = "http://www.kma.go.kr/repositary/image/cht/img/%s_%s%02d.png" % (i, today, Ho)
			filename = url.split('/')[-1]
			my_file = Path('Downloads/%s' % filename)
			if my_file.is_file(): # image file already exists in my folder
				print ('File exists %s' % filename)
			else:
				try:
					print ('Trying %s' % filename)
					urllib.request.urlretrieve(url, 'Downloads/%s' % filename)
					print ('Downloaded %s' % url)
				except  urllib.error.HTTPError: # image file doesn't exists in the server
					print ('cannot download %s' % filename)
		for i in chl2:
			url = "http://www.kma.go.kr/repositary/image/cht/img/%s_%s%02d.gif" % (i, today, Ho)
			filename = url.split('/')[-1]
			my_file = Path('Downloads/%s' % filename)
			if my_file.is_file(): # image file already exists in my folder
				print ('File exists %s' % filename)
			else:
				try:
					print ('Trying %s' % filename)
					urllib.request.urlretrieve(url, 'Downloads/%s' % filename)
					print ('Downloaded %s' % url)
				except  urllib.error.HTTPError: # image file doesn't exists in the server
					print ('cannot download %s' % filename)
	day = day - timedelta(hours=(24*d)) #하루 전날로 이동