#!/usr/bin/python3

#Copyright 2021 Nur Mahmud Ul Alam Tasin
#mlwbd link leaker
#for educational perposes only.

from sys import argv
import requests
import re
import html
import json
import datetime
def main():
    argv_val=int(argv[-1])
    with open("./movies.json","r") as handle:
        items=json.load(handle)
        links=list(items.values())
        movies=list(items.keys())
        links__=links[len(links)-argv_val:-1]
        print(movies)
    count=0
    for link in links__:
        try:
            res=requests.get(link,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
            })
            if res.status_code==200:
                count+=1
                reobj=re.search(r"([ ]*)?<h1 class=\"entry-title\">(.*)</h1>",res.text)
                print(f"[{count}]  {html.unescape(reobj.group(2))} -> {link}")
                movies[links.index(link)]=html.unescape(reobj.group(2))
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
        json.dump(dict(zip(movies,links)),handle,indent=2)
    print("Saved Successfully....")
    print("Exiting...")

if __name__=="__main__":
    start=datetime.datetime.now()
    print(f"Process started on {str(start)}")
    main()
    end=datetime.datetime.now()
    print(f"Process ended on {str(end)}")
    print(f"Process took {str(end-start)}")
