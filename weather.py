import bs4
import requests

class weather_data:
    
    def weather():
        flag = -1
        while flag == -1:
            try:
                city = input("Enter city: ")
                url = "https://www.google.com/search?q="+"weather" + city
                html = requests.get(url).content
                request_result = requests.get( url ) 
                soup = bs4.BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                # this contains sky description
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        
                # format the data
                data = str.split('\n')
                sky = data[1]
                
                # list having all div tags having particular class name
                listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        
                # particular list with required data
                strd = listdiv[5].text
        
                # formatting the string
                pos = strd.find('Wind')
                other_data = strd[pos:]
                
                print("Temperature is", temp)
                print("Sky Description: ", sky)
                print(other_data)
                flag = 0
            except:
                print("Can't find a city with that name!")

        