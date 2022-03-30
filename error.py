import os, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install futures')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    __import__('error').check_subscription()
elif bit == '32bit':
    __import__('error32').check_subscription()
    exit()
