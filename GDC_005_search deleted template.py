#! usr/bin/env python
#  -*- coding: UTF-8 -*-
#author: panxintong
import requests


headers={
	'Cookie':'SESSION=ebd678dd-9089-4619-9f34-7b8a14c3d46b; userGdcLanguage=zh_CN; _trmccid=1ca5c6a150aa8699; _ga=GA1.2.1790544946.1468403163; _gid=GA1.2.1426293822.1547537996; X-Linegame-UserToken=WZgYqnKM5aozjoYqLFhWXn2IvasM5tnv9xvJRwm7LONjuihd%2FCXF3KdjeVdxXBLuHzpOu7sJLMgsEoY737pJZw%3D%3D; lgac=GDC.X8pFvSxzGZ0p23taEGB6E28X2gzTqCNmMLTcoQ4KUcvlYe0lLxQ3fn2NGN9rq-tj3gIZgaG1GVOwtShNVtUk3FS9ouszFCwp-WPUFp2KVhRWD25Hk6G7g81-Tq3aihEg'
}
r=requests.get(url='https://gdc.game.line.me/games/channels/1367581746/linemarketing/linemessage?index=1&keyword=realnotuse6th&_=1547606394200')
print(r.status_code)
