import urllib
url = 'http://aska.ru-hoster.com:8053/autodj'

code = urllib.urlopen(url).getcode()
#if code == 200:  #Edited per @Brad's comment
if str(code).startswith('2') or str(code).startswith('3') :
    print ('Stream is working')
else:
    print ('Stream is dead')
