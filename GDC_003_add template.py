#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong
import requests

data={
'templateImages[0].title':'test123',
'templateImages[0].text':'test123',
'templateImages[0].imageUrl':'https://obs.line-scdn.net/0hlhEKr9y4M0d4Mhke7URMEEJvNSgBVCRNEEo5fUNkOCU7AnAUQlN9Jlw3ZXRRAXQZEVV7J18wKHZdBCRCE1R8',
'templateImages[0].buttonLabel':'test123',
'ttemplateImages[0].appstoreUrl':'https://itunes.apple.com/app/id888615473',
'templateImages[0].iphoneLinkUri':'line3rdp.com.linecorp.LGSDKTEST://',
'templateImages[0].googleplayUrl':'https://play.google.com/store/apps/details?id=com.linecorp.LGPKPK',
'templateImages[0].androidLinkUri':'LGSDKTEST://',
'templateId':'test1231234',
'templateType':'game_buttons',
}

headers={
'cookie':'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg; _gat=1'
}

r=requests.get( url='https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage/template/form?method=add',
				data=data,
				headers=headers)

print(r.status_code)
print(r.text)