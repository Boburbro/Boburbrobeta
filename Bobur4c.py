def tgddos(a):
	import telethon
	import time
	import sys
	from os import system
	import os, sys, time, socket, random, requests
	from telethon import TelegramClient, sync, utils
	os.system("termux-open-url https://t.me/Boburbro_tg")
	time.sleep(0.5)
	os.system("clear")
	telegramspam_banner ='''\033[91m  
	 ____        _                _      
	 |  _ \      | |              | |    
	 | |_) | ___ | |__  _   _ _ __| |__  _ __ ___    
	 |  _ < / _ \| '_ \| | | | '__| '_ \| '__/ _ \    
	 | |_) | (_) | |_) | |_| | |  | |_) | | | (_) |    
	 |____/ \___/|_.__/ \__,_|_|  |_.__/|_|  \___/     
	'''
	def clearscreen():
	        if sys.platform == "linux2":
	                os.system("clear")
	        elif sys.platform == "win32":
	                os.system("cls")
	        else:
	                os.system("clear")
	
	def restart_program():
	        python = sys.executable
	        os.execl(python, python, * sys.argv)
	        curdir = os.getcwd()
	
	def backtomenu_option():
	        print(backtomenu_banner)
	        backtomenu = input("boshlash:  ")
	
	        if backtomenu == "99":
	                restart_program()
	        elif backtomenu == "00":
	                sys.exit()
	        else:
	                print("\nERROR: Wrong input")
	                time.sleep(2)
	                restart_program()
	
	
	__banner__ ='''\033[91m   
	 ____        _                _      
	 |  _ \      | |              | |    
	 | |_) | ___ | |__  _   _ _ __| |__  _ __ ___    
	 |  _ < / _ \| '_ \| | | | '__| '_ \| '__/ _ \    
	 | |_) | (_) | |_) | |_| | |  | |_) | | | (_) |    
	 |____/ \___/|_.__/ \__,_|_|  |_.__/|_|  \___/     
	'''
	
	
	clearscreen()
	print(__banner__)
	os.system("clear")
	
	print("""\033[1;34m
	  Menu:
	 [1] Tgddos
	 [0] chiqish
	""")
	
	
	while True:
	        try:
	                santet = input("\t\t->")
	
	                if santet == "01" or santet == "1":
	                        os.system("clear")
	                        print(telegramspam_banner)
	                        api_id = 1148490
	                        api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
	                        client = TelegramClient('client',api_id,api_hash).start()
	                        target = input("Enter: habar yubormoqchi bolgan odamingizning useri yoki ID sini yozing: ")
	                        try: count = int(input("boshlash: necha marta yuborilsin:"))
	                        except(ValueError): count = 100
	                        urmsg = input("Enter: yubormoqchi bo'lgan habaringiz: ")
	                        for x in range(count):
	                                client.send_message(target, urmsg)
	                                sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, target))
	                                sys.stdout.flush()
	                        print("\n[!] muvafaqiyatli amalga oshirildi ... !!\n")
	                        backtomenu_option()
	                elif santet == "00" or santet == "0":
	                        sys.exit()
	                        print("Telegram: @Boburbro_tg")
	                elif santet.lower() == "Script":
	                        print("ushbu script orqali telegram guruhlarga har bir sozni 2000 marotabadan koproq yubora olasiz.")
	                elif santet.lower() == "version":
	                        print("Version 1.0")
	                elif santet.lower() == "exit":
	                        sys.exit()
	                else:
	                        pass
	        except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
	                print("Bunday raqam topilmadi")
	                print("Nimadur xato keti\n")
	        except(KeyboardInterrupt):
	                print("\n[!] Thank you for using")
	                break
	        except(EOFError):
	                print("\n[!] Thank you for using")
	                break
	        except Exception as e:
	                print("\n[!] Error: "+e)
	