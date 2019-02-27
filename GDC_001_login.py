#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong


import requests


data={'id':'CN40780',
      'password':'pxt291710$',
      'urlStore':'https://sign.game.line.me/auth/login?redirectUrl=https://gdc.game.line.me/games/main/apps'}

headers={
        'Content-Type':'application/x-www-form-urlencoded'

}
r = requests.get(url='https://sign.game.line.me/auth/login?redirectUrl=%20https://gdc.game.line.me/games/main/apps',
                  data=data,#form表单用data
                  headers=headers)
print(r.status_code)#状态码
print(r.text)