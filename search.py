import wikipedia
from googlesearch import search
import random
 

class search_internet:

    def search_google(data):
        
        query = input("Enter query: ")
        print('Wait, let me search....')
        try:
            print(wikipedia.summary(query))
        except:
            print("Here are the top links to the query")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)  

    def wiki_summary(data):
        
        flag = -1
        while flag == -1:
            try:
                topic = input("Enter topic: ")
                if topic.lower()=='quit':
                    break
                print('Accessing wikipedia....')
                print(wikipedia.summary(topic))
                flag = 0
            except:
                print("Give more specifics")