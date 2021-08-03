#! python3

import requests,pyperclip,sys,time
import pandas as pd

url = sys.argv[1]


path_prefix = r'C:\Users\John\Desktop\Python Downloads'

if len(sys.argv)>2:
    filename = ' '.join(sys.argv[2:])
else:
    filename = int(round(time.time() * 1000))

types = pd.read_csv(r'C:\Users\John\AppData\Local\Programs\Python\Python39\Programs\types.csv')

r = requests.head(url, allow_redirects = True)
strType = r.headers.get('content-type')
filetype = '.file'

if strType != None:
    filetype = types[types["MIME Type"]==strType.split(';')[0]].Extension.iloc[0]

filename = path_prefix + '\\' + str(filename) + filetype

r = requests.get(url, allow_redirects = True)

open(filename, mode = 'wb').write(r.content)

