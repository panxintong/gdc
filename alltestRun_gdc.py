#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

import unittest
import os
import HTMLTestRunner
import time

def allTest():
	suite = unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='GDC_unitest.py',
		top_level_dir=None)
	return suite


def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))


def run():
	unittest.TextTestRunner(verbosity=2).run(allTest())
	fp = os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),
		title='auto test report',
		description='auto test report details').run(allTest())


if __name__ == '__main__':
	run()

