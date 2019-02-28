

import requests
from lxml import etree



def exractcharacter():
    try:
        #opening male and female files seperately 
        with open("malecharacter.txt","w") as maleFile, open('femalecharacter.txt', 'w') as femaleFile:   
            for i in range(0,50):
                    res = requests.get("https://theyfightcrime.org/") 
                    root= etree.HTML(res.content)
                    words = root.xpath("//p//text()")
                    if(len(words)> 1):
                        characters = words[1]    
                    gender = characters.split('She')                  
                    if(len(gender)>1):
                        male =gender[0]
                        maleFile.writelines(male+'\n')
                        female = 'she'+gender[1] 
                        femaleFile.writelines(female+'\n')
                    elif len(gender) == 0:
                        male =gender[0] 
                        maleFile.writelines(male+'\n')
    except IOError as e:
        print ('Operation failed: %s' % estrerror)
  
#function call                  
exractcharacter()
