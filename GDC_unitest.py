#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong

import unittest
import requests
import json

class get_request_01(unittest.TestCase):
	u'''login'''
	def setUp(self):
		self.get_url = 'https://sign.game.line.me/auth/login?redirectUrl=%20https://gdc.game.line.me/games/main/apps'
		self.header = {'Content-Type':'application/x-www-form-urlencoded'}

	def test_get_01(self):
		url = self.get_url
		headers=self.header
		data = {'id': 'CN40780',
		        'password': 'pxt291710$',
		        'urlStore': 'https://sign.game.line.me/auth/login?redirectUrl=https://gdc.game.line.me/games/main/apps'}
		r = requests.get(url,headers=headers,data=data)
		self.assertEqual(r.status_code, 200,'test pass')

	def tearDown(self):
		pass


class get_request_02(unittest.TestCase):
	u'''getuserinfo:Appid:LGSDKTEST'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/LGSDKTEST/appreview/ranking/appstore?appStoreDt='
		self.headers = {
		'Cookie': 'SESSION=3deaf033-978b-4b98-a33a-4a937a2d880f; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=5u5OxysoefUldZh9OK6os6Hxmr5ecI9TP3Kav94rZ2BgtyRZCnyHNx%2Bhjm5rxUrLneUJ93Oe8pOK8H5Zh%2Fxg6w%3D%3D; lgac=GDC.Yhp_0Lv-CgdxFf8VThhf7DA4dFyitB5E4K2LjDJw9yhFbeiqKcTrAtWGccRBfKPTLOqEIBG9oVvgyXz0SVlUX-J5OjPw6QUqDAd6AKaamYhxUuEZgqiSWYZVFj8RdkuI; _gat=1'
		}

	def test_get_02(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,timeout=60) #方式1加到headers
		self.assertEqual(r.status_code, 200,'test pass')
		self.assertEqual(json.loads(r.text)['data']['appStoreRankingList'], [],'test pass')

	def tearDown(self):
		pass


class get_request_03(unittest.TestCase):
	u'''add_template:test1231234'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage/template/form?method=add'
		self.headers = {
		'Cookie': 'SESSION=3deaf033-978b-4b98-a33a-4a937a2d880f; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=5u5OxysoefUldZh9OK6os6Hxmr5ecI9TP3Kav94rZ2BgtyRZCnyHNx%2Bhjm5rxUrLneUJ93Oe8pOK8H5Zh%2Fxg6w%3D%3D; lgac=GDC.Yhp_0Lv-CgdxFf8VThhf7DA4dFyitB5E4K2LjDJw9yhFbeiqKcTrAtWGccRBfKPTLOqEIBG9oVvgyXz0SVlUX-J5OjPw6QUqDAd6AKaamYhxUuEZgqiSWYZVFj8RdkuI'
		}
		self.data = {
		'templateImages[0].title': 'test123',
		'templateImages[0].text': 'test123',
		'templateImages[0].imageUrl': 'https://obs.line-scdn.net/0hyyf4ZXaHJlZbTQwP39tZAWEQIDkiKzFcMzUsbGAbLTQYfWUFYSxoM3xKcGV0dWEINX5uNn5NPWd-ezFTZnhp',
		'templateImages[0].buttonLabel': 'test123',
		'ttemplateImages[0].appstoreUrl': 'https://itunes.apple.com/app/id888615473',
		'templateImages[0].iphoneLinkUri': 'line3rdp.com.linecorp.LGSDKTEST://',
		'templateImages[0].googleplayUrl': 'https://play.google.com/store/apps/details?id=com.linecorp.LGPKPK',
		'templateImages[0].androidLinkUri': 'LGSDKTEST://',
		'templateId': 'test1231234',
		'templateType': 'game_buttons',
	}

	def test_get_03(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,data=self.data,timeout=60)
		self.assertEqual(r.status_code, 200,'test pass')

	def tearDown(self):
		pass

class get_request_04(unittest.TestCase):
	u'''search_template:test1231234'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage?index=1&keyword=test1231234&_=1547603212314'
		self.headers = {
		'Cookie': 'SESSION=337ab618-b8b3-4e7e-bfab-41dea839cb43; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=5u5OxysoefUldZh9OK6os6Hxmr5ecI9TP3Kav94rZ2BgtyRZCnyHNx%2Bhjm5rxUrLneUJ93Oe8pOK8H5Zh%2Fxg6w%3D%3D; lgac=GDC.Yhp_0Lv-CgdxFf8VThhf7DA4dFyitB5E4K2LjDJw9yhFbeiqKcTrAtWGccRBfKPTLOqEIBG9oVvgyXz0SVlUX-J5OjPw6QUqDAd6AKaamYhxUuEZgqiSWYZVFj8RdkuI; _gat=1'
		}

	def test_get_04(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,timeout=60)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateId'],'test1231234','test pass')

	def tearDown(self):
		pass


class get_request_05(unittest.TestCase):
	u'''edit_template:test1231234'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage/template/form?method=edit'
		self.headers = {
		'Cookie': 'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg; _gat=1'
		}

	def test_get_05(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,timeout=60)
		self.assertEqual(r.status_code, 200,'test pass')

	def tearDown(self):
		pass

class get_request_06(unittest.TestCase):
	u'''search_edit_template:test1231234'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage?index=1&keyword=test1231234&_=1547357750650'
		self.headers = {
		'Cookie': 'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg'
		}

	def test_get_06(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,timeout=60)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['title'],'Hello Sunday','test pass')
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['text'],'Hello Sunday','test pass')
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['buttonLabel'],'Hello Sunday','test pass')

	def tearDown(self):
		pass


class get_request_07(unittest.TestCase):
	u'''search_edit_template:test1231234'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage?index=1&keyword=test1231234&_=1547357750650'
		self.headers = {
		'Cookie': 'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg'
		}

	def test_get_07(self):
		url = self.get_url
		r=requests.get(url,headers=self.headers,timeout=60)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['title'],'Hello Sunday','test pass')
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['text'],'Hello Sunday','test pass')
		self.assertEqual(json.loads((r.text))['linkMessageTemplates'][0]['templateImages'][0]['buttonLabel'],'Hello Sunday','test pass')

	def tearDown(self):
		pass


class post_request_01(unittest.TestCase):
	u'''delete_template'''
	def setUp(self):
		self.get_url = 'https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage/template/delete?templateId=realnotuse6th&channelId=1367581746&templateType=game_buttons'
		self.headers = {
		'Cookie': 'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg; _gat=1'
		}

	def test_post_08(self):
		url = self.get_url
		r=requests.post(url,headers=self.headers,timeout=60)
		self.assertEqual(r.status_code, 200,'test pass')

	def tearDown(self):
		pass


if __name__ == "__main__":
	unittest.main()
