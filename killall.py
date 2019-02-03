import psutil
import requests
r = requests.get("https://gist.githubusercontent.com/ledinhhuy/2acd143b6ee5bcdf87b78b23a77a2c51/raw/3571008c7d4983b3271e2cca3c37916c9d6b76d1/kill_ignore.txt")
kill_ignore = set(r.content.splitlines())
print kill_ignore
for p in psutil.process_iter():
    try:
        if p.name() not in kill_ignore:
            print "killing", p.name(), p.cwd()
            # p.terminate()
    except Exception as ex:
        print ex
