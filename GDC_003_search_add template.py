#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong
import requests
import json

headers={
'cookie':'SESSION=3db4e168-92b4-4027-b28b-2d56d1a3c807; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.424131228.1547344719; X-Linegame-UserToken=%2FycqmsptC6QsQ0n90oXOPjR1PmdLCPVwJobLNIfsgFYRFtIOuQzi3taxPrZQH4st1ObpgQfA6EXHbi7lAvmaew%3D%3D; lgac=GDC.5tAPzesXuXncuz0zqvfBmuZw3jNcL7ZhVfiI-wMK4whJ6oAIQ5aFrm8cdx5M-ErKV8q67NS1Bzby8uzPdiAD5tZHBCuCw8o3tKYJ-s5Gd1JYFqBPR30Lbz516MX6kPhN'
}

r=requests.get(url='https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage?index=1&keyword=test1231234&_=1547357750650',
               headers=headers)
print(r.status_code)
print(r.text,type(r.text))
# print(json.loads((r.text))['linkMessageTemplates'][0]['templateId'])