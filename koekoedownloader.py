def koedownload(code):
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup

    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url = 'https://koe-koe.com/detail.php?n=' + code
    html  = urllib.request.urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    title = str(soup.title.string) +'.mp3'
    mp3 = 'https://file.koe-koe.com/sound/upload/' + code + '.mp3'
    urllib.request.urlretrieve(mp3,title)
    print('finished, file name is ' + title)

code = input("Enter the koekoe code: ")
print('downloading...')
try:
    koedownload(code)
except:
    print('Cannot find koekoe file!')

