import psutil
import requests
r = requests.get("https://pastebin.com/raw/h7KiWPtq")
kill_ignore = set(r.content.splitlines())
print "ignore", kill_ignore
for p in psutil.process_iter():
    try:
        if p.name() not in kill_ignore:
            print "killing", p.name(), p.cwd()
            # p.terminate()
    except Exception as ex:
        print ex
