def bro(bobur):
	prin= ('''\033[91m   
 ____        _                _      
 |  _ \      | |              | |    
 | |_) | ___ | |__  _   _ _ __| |__  _ __ ___    
 |  _ < / _ \| '_ \| | | | '__| '_ \| '__/ _ \    
 | |_) | (_) | |_) | |_| | |  | |_) | | | (_) |    
 |____/ \___/|_.__/ \__,_|_|  |_.__/|_|  \___/     
''')







	import requests,re,os
	import time
	import sys
	from os import system
	from platform import platform
	from time import sleep
	import os
	puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
	delet = 'clear'
	os.system(delet)
	print(prin)
	print("Please select country for hack :")
	print("""
1. Russian Federation\n2. United States\n3. Japan\n4. Canada\n5. New Zealand\n6. Ukraine\n7. Germany\n8. Austria\n9. Spain\n10. Turkey \n11. Hong Kong\n12. Greece\n13. Portugal\n14. Singapure\n15. Columbia
	""")
	num = int(input("country : "))
	if num == 1:
	        print("\n")		
	        os.system(delet)
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,82):
				
	                url = ("http://www.insecam.org/en/bycountry/RU/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	
	                     count += 1
	        except:
	            print ("") 
	if num == 2:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,720):
				
	                url = ("http://www.insecam.org/en/bycountry/US/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")
	if num == 3:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,232):
				
	                url = ("http://www.insecam.org/en/bycountry/JP/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")
	if num == 4:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,38):
				
	                url = ("http://www.insecam.org/en/bycountry/CA/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")             
	if num == 5:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,5):
				
	                url = ("http://www.insecam.org/en/bycountry/NZ/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")             
	if num == 6:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,2):
				
	                url = ("http://www.insecam.org/en/bycountry/UK/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;37m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ") 
	if num == 7:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,107):
				
	                url = ("http://www.insecam.org/en/bycountry/DE/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")
	if num == 8:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,48):
				
	                url = ("http://www.insecam.org/en/bycountry/AT/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                     count += 1
	        except:
	            print (" ")           
	if num == 9:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,39):
				
	                url = ("http://www.insecam.org/en/bycountry/ES/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")  
	if num == 10:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,54):
				
	                url = ("http://www.insecam.org/en/bycountry/TR/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")             
	if num == 11:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,7):
				
	                url = ("http://www.insecam.org/en/bycountry/HK/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")  
	if num == 12:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,8):
				
	                url = ("http://www.insecam.org/en/bycountry/GR/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")           
	if num == 13:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,7):
				
	                url = ("http://www.insecam.org/en/bycountry/PT/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ")        
	if num == 14:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,7):
				
	                url = ("http://www.insecam.org/en/bycountry/SG/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	
	                     count += 1
	        except:
	            print (" ")      
	if num == 15:
	        print("\n")		
	        try:
	            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
	            for page in range (0,6):
				
	                url = ("http://www.insecam.org/en/bycountry/CO/?page="+str(page))
	            
	                res = requests.get(url, headers=headers)
	                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
	                count = 0
	                                
	                for _ in findip:
	                     hasil = findip[count]
	
	                     print ("\033[1;31m",hasil)
	                     f = open('logs.txt' , 'a')
	                     f.write(f'{findip}' + '\n')
	                     f.close()
	                 
	                     count += 1
	        except:
	            print (" ") 
	
	
	print("Готово! Все логи были сохранены в файл logs.txt")