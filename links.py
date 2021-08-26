# This Software is under the MIT License
# Copyright (c) 2021, The Shah Jabir Taqi and Nur Mahmud-ul-Alam Tasin, All Rights Reserved.
import argparse
import json
import os
import platform
import re
import webbrowser

import requests

os_name = platform.system()
if os_name == "Windows":
    pythoncmd = "python"
    os.system("cls")
elif os_name == "Linux":
    pythoncmd = "python3"
    os.system("clear")
else:
    pythoncmd = "python3"
    os.system("clear")

if os.path.exists("./movies.json"):
    with open("./movies.json","r") as handle:
        items=json.load(handle)
        links=list(items.values())
        movies=list(items.keys())
else:
    print("No movies.json file found.\nCreating a new one. or run ",pythoncmd," ./app.py") 
        

def check_file():
    if os.path.exists("./movies.json"):
        pass
    movie_in_list = format(len(movies))
    return movie_in_list

def movie_update():
    res=requests.get("https://mlwbd.one/")
    if res.status_code==200:
        reobj=re.search(r"<span>([0-9, ]*)<a href=\"https://mlwbd.one/movie/\" class=\"see-all\">See all</a></span>",res.text)
        count=int(reobj.group(1).strip().replace(",",""))
    return count
        
if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Links | get your movie")

    parser.add_argument("Name",help="File or Movie name undar ", action="store")
    parser.add_argument("-c","--check",help="-c <file_name> Check Movie list.",action="store_true")
    parser.add_argument("-u","--update",help="-u <file_name> Update Movie list.",action="store_true")
    parser.add_argument("-l","--list",help="-l <file_name> List Movie list.",action="store_true")
    parser.add_argument("-ln","--link",help="-ln <movie_name> Movie link.",action="store_true")
    parser.add_argument("-d","--download",help="-d <movie_name> Download Movie.",action="store_true")
    parser.add_argument("-s","--search",help="-s <movie_name> Search Movie.",action="store_true")

    arguments=parser.parse_args()

    if arguments.check:
        print("Checking Movie list.....")
        if check_file() == movie_update():
            print("Movie list is up to date.")
        else:
            print("There are ",check_file()," movies in your list.")
            print("There are ",movie_update()," movies in the website.")
            print("Please update your list.")
            print("Use ",pythoncmd," -u <file_name> to update your list.")
    elif arguments.update:
        print("Updating Movie list.....")
        os.system(pythoncmd+" ./update_links.py")
        print("Movie list is updated.")
        print("Total Movie:",check_file())
    elif arguments.list:
        print("Listing Movie list.....")
        print("Total Movie:",check_file())
        for i in range(len(movies)):
            print(movies[i])
    elif arguments.link:
        i = 0
        print("Getting Movie link.....")
        movie_name=arguments.Name
        while i < len(movies):
            if movie_name.lower() in movies[i].lower() :
                print(movies[i])
                print(links[i])
                print("------------------------------------")
                print("\n")
            i=i+1
    elif arguments.search:
        print("Searching Movie.....")
        movie_name=arguments.Name
        i = 0
        while i < len(movies):
            if movie_name.lower() in movies[i].lower() :
                print(movies[i])
                print("-----------------------------------")
                print("\n")
            i = i+1
    elif arguments.download:
        i = 0
        j = 0
        count = {}
        movie_name=arguments.Name
        while i < len(movies):
            if movie_name.lower() in movies[i].lower() :
                j = j+1
                print(j)
                print("------------------------------------")
                print(movies[i])
                print(links[i])
                print("------------------------------------")
                print("\n")
                count.update({j: i})
            i=i+1
        print("There are ", j ," movies found.")
        print("Which one do you want to download?")
        print("Enter the number of the movie:")
        movie_number = int(input())
        if movie_number > j:
            print("Invalid number.")
        else:
            print("Downloading Movie.....")
            download_link = count[movie_number]
            print(movies[download_link])
            print(links[download_link])
            webbrowser.register('chrome', None)
            webbrowser.open(links[download_link])
    else:
        print("Use ",pythoncmd," -h to see help.")

