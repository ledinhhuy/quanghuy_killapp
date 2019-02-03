import psutil
import requests
r = requests.get("https://pastebin.com/raw/h7KiWPtq")
kill_ignore = set()
for p in r.content.splitlines():
    kill_ignore.add(p.lower())
print "ignore", kill_ignore
for p in psutil.process_iter():
    try:
        if p.name().lower() not in kill_ignore:
            print "killing", p.name(), p.cwd()
            p.terminate()
    except Exception as ex:
        print "gap loi", ex