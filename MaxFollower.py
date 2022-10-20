try:
	import requests,random,os
except ImportError:
	import os
	os.system('pip install requests')
	os.system('pip install random')
class whisper():
	def igg(user):
		he = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar',
	'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'x-asbd-id': '198387',
	'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	}
		urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
		try:
			re =requests.get(urlg,headers=he).json()
			name = re["data"]["user"]["full_name"]
			id = re["data"]["user"]["id"]
			fbid =re["data"]["user"]["fbid"]
			return name,id,fbid,user
		except requests.exceptions.RequestException as e:
			return "Error User"
	def login(name,id,fbid,user):
		url="http://maxfolwer.ir/appapi/v1/account.php"
		h={"X-Access": "cafegram",
"X-Version": "1",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-J610F Build/PPR1.180610.011)",
"Host": "maxfolwer.ir",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"Content-Length": "115",

}
		d=f'full_name={name}&user_pk={id}&fbid={fbid}&x_version=1&login=&username={user}&'
		req = requests.post(url,headers=h,data=d)
		try:
			return req.json()['data']['user_token']
		except:
			return 'Error'
	def order(token,id):
		u0='http://maxfolwer.ir/appapi/v1/orders.php'
		h0={"X-Access": "cafegram",
"X-Version": "1",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-J610F Build/PPR1.180610.011)",
"Host": "maxfolwer.ir",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"Content-Length": "90",}
		d0=f'user_pk={id}&x_version=1&action=follow&user_token={token}&'
		req = requests.post(u0,headers=h0,data=d0)
		return req.json()
	def coin(id,token,order_pk,order_id):
		u1='http://maxfolwer.ir/appapi/v1/coin.php'
		h1={"X-Access": "cafegram",
"X-Version": "1",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-J610F Build/PPR1.180610.011)",
"Host": "maxfolwer.ir",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"Content-Length": "118",}
		d1=f'user_pk={id}&x_version=1&action=follow&user_token={token}&pk={order_pk}&order_id={order_id}&'
		req = requests.post(u1,headers=h1,data=d1)
		return req.json()
	def gecoin(userredem,id,token):
		u2='http://maxfolwer.ir/appapi/v1/transCoin.php'
		h2={"X-Access": "cafegram",
"X-Version": "1",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-J610F Build/PPR1.180610.011)",
"Host": "maxfolwer.ir",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"Content-Length": "116",}
		d2=f'to_user={userredem}&user_pk={id}&x_version=1&action=follow&user_token={token}&coin=150&'
		req = requests.post(u2,headers=h2,data=d2)
		return req.text
	def genuser():
		user=['mosalah','ahmed','ali','khaled','marshal','jones','hydra','amr','whisper','zenib','mostafa','abanoub','Sherif']
		user1='0192837465'
		users=str(''.join((random.choice(user) for i in range(1))))+str(''.join((random.choice(user1) for i in range(3))))
		return users
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}==============================
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
userredem=input(f'{S}[+] UserName To Send Coins ==> {B}')
print(f'{E}==============================')
cs = whisper
userig=cs.genuser()
info=cs.igg(userig)
name=info[0]
id=info[1]
fbid=info[2]
user=info[3]
token=cs.login(name,id,fbid,user)
send=0
while True:
	order=cs.order(token,id)
	for i in order['data']:
		order_id=(i['id'])
		order_pk=(i['user_pk'])
		co = cs.coin(id,token,order_pk,order_id)['data']['coin']
		print(f'{S}[+] Coins ==> {B}{co}')
		if co > int(160):
			fm=cs.gecoin(userredem,id,token)
			if 'success' in fm:
			 send+=150
			 print(f'{G}[✓] Done Send {B}{send} {G}Coins')
			else:
				print(f'{E}[×] Error Send')
		else:
			pass