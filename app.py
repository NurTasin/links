#!/usr/bin/python3

#Copyright 2021 Nur Mahmud Ul Alam Tasin
#mlwbd link leaker
#for educational perposes only.

import requests
import re
import html
import json
def main():
    with open("./movies.json","r") as handle:
        items=json.load(handle)
    count=0
    for i in range(1,45000):
        try:
            res=requests.get("https://songslyric.site/links/"+str(i),
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
            })
            if res.status_code==200:
                count+=1
                reobj=re.search(r"([ ]*)?<h1 class=\"entry-title\">(.*)</h1>",res.text)
                print(f"[{count}]  {html.unescape(reobj.group(2))} -> https://songslyric.site/links/{i}")
                items[html.unescape(reobj.group(2))]=f"https://songslyric.site/links/{i}"
        except KeyboardInterrupt:
            print("Saving Progress....")
            with open("./movies.json","w+") as handle:
                json.dump(items,handle,indent=2)
            print("Saved Successfully....")
            print("Exiting...")
            exit(0)
        except AttributeError:
            pass
    print("Saving Progress....")
    with open("./movies.json","w+") as handle:
        json.dump(items,handle,indent=2)
    print("Saved Successfully....")
    print("Exiting...")
    exit(0)

if __name__=="__main__":
    main()
    
