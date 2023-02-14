import requests
from bs4 import BeautifulSoup
import itertools
import json



#git pull
#git status
#git add
#git commit -m " "
#git commit 
#git push 
#git log 
#git push

# This is a Web Scraper Python script.

#Gets the link from the wepage and finds other links
def get_link(link,domain,linklist):
    try:

        request = requests.get(link)
        soup = BeautifulSoup(request.text, 'html.parser')
        for link in soup.find_all('a'):
            fullLink=link.get('href')
            if(fullLink != None) and fullLink != '#':
                domain_check(domain, fullLink,linklist)
        #This is the list of links from the website chosen
        request.close()
    except:
        print("URL didnt work")
    #print(LL)
    #print(len(LL))


#goes through and scans for all the links
def depthcounter(count):
    depthlist=set()
    if count == depth:
        LL.update(depthlist)
        print("This shows the final count of all the links found", len(LL))
        return LL
    else:
        for i in LL:
            get_link(i,domain,depthlist)
        count=count+1
        LL.update(depthlist)
        depthcounter(count)

        


#checks to see if the link is in the right domain
def domain_check(domain, link,linklist):
    if link.find(domain) >0:
        #print(link)
        linklist.add(link)

if __name__ == '__main__':
    #Defines the 3 inputs needed domain,url, and depth
    domain = input("Enter the domain to be searched (Ex: www.rit.edu): ")
    url = input("Enter the URL that is needed to search (Ex: https://www.rit.edu): ")
    depth = int(input("Enter a depth wanted: (Ex: 0, 1, 2 ..): "))
    #this is a counter to check what depth is at. 
    count = 0
    depthlist=0
    #ensures no duplicates and order doesnt really matter for this
    LL= set()
    btL = []
    get_link(url,domain,LL)
    depthcounter(count)
    #Can not add a set to a json file for some reason so converter back into a list
    btL = list(LL)
    #This puts the list into a json file at current working directory
    with open('test.json', 'w') as outputfile:
        output = json.dump(btL,outputfile)
