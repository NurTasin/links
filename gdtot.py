#!/usr/bin/python3

#Copyright 2021 Nur Mahmud Ul Alam Tasin
#mlwbd link leaker
#for educational perposes only.

import requests
import re
import html
import json
import datetime
def main():
    with open("./gdtot.json","r") as handle:
        items=json.load(handle)
        links=list(items.values())
        movies=list(items.keys())
    count=0
    last_index=int(links[-1].replace("https://new.gdtot.sbs/file/",""))+1
    gap=0
    for i in range(last_index,999999999):
        print(i,end="\r")
        try:
            if not "https://new.gdtot.sbs/file/"+str(i) in links:
                res=requests.get("https://new.gdtot.sbs/file/"+str(i),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
                })
                if res.status_code==200:
                    count+=1
                    reobj=re.search(r"<h5 class=\"m-0 font-weight-bold\" align=\"center\">(.*)</h5>",res.text)
                    print(f"[{count}]  {html.unescape(reobj.group(1))} -> https://new.gdtot.sbs/file/{i}")
                    items[html.unescape(reobj.group(1))]=f"https://new.gdtot.sbs/file/{i}"
                elif res.status_code==404:
                    gap+=1
                    if gap>=200:
                        break
            else:
                print("[Cached]  "+movies[links.index("https://new.gdtot.sbs/file/"+str(i))]+" -> "+"https://new.gdtot.sbs/file/"+str(i))
        except KeyboardInterrupt:
            print("Saving Progress....")
            with open("./movies.json","w+") as handle:
                json.dump(items,handle,indent=2)
            print("Saved Successfully....")
            print("Exiting...")
            return
        except AttributeError:
            pass
    print("Saving Progress....")
    with open("./movies.json","w+") as handle:
        json.dump(items,handle,indent=2)
    print("Saved Successfully....")
    print("Exiting...")

if __name__=="__main__":
    start=datetime.datetime.now()
    print(f"Process started on {str(start)}")
    main()
    end=datetime.datetime.now()
    print(f"Process ended on {str(end)}")
    print(f"Process took {str(end-start)}")
