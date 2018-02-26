import urllib.request
import urllib, time

def read(site_url):
    with urllib.request.urlopen(site_url) as url:
        start=time.time()
        s = url.read()
        page=url.read()
        end=time.time()
        url.close()
        return end - start
