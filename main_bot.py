import requests
import base64
import mail
import time,os
import random
import string
import base64

logo = f"""
> Devoloper  :  Saifur Rahman Siam
> Github     :  github.com/nbprg
> YouTube    :  Crypto Hub
\033[1;34m------------------------------------------\033[0m"""
os.system('clear')
print(logo)
base_url = input('> Input base url : ')
refcode = input('> Reffar code : ')
print('\033[1;34m------------------------------------------\033[0m')
def gtpas(length=8):
    if length < 8:
        length = 8
    
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("@#$&")
    
    remaining = ''.join(random.choices(string.ascii_letters + string.digits + "@#$&", k=length - 4))
    
    password = upper + lower + digit + special + remaining
    
    encoded_password = base64.b64encode(password.encode()).decode()
    return encoded_password

used = []
def random_proxy():
   global used
   proxy = open('proxy.txt','r').read()
   total = int(len(proxy.splitlines()))
   if int(len(used)) >= total:
       return str('All proxy used form `proxy.txt`  ')
   else:
       while True:
            prox = random.choice(proxy.splitlines())
            if not prox in used:
                used.append(prox)
                return {'http': prox, 'https': prox}

def create_account(captcha_token, password, email, returned_proxy):
    headers = {
    'Host': 'gw.sosovalue.com',
    'sec-ch-ua-platform': 'Android',
    'user-device': 'Chrome/131.0.6778.260#Android/15',
    'accept-language': 'en',
    'sec-ch-ua': 'Android',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; 23129RAA4G Build/AQ3A.240829.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://m.sosovalue.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://m.sosovalue.com/',
    'priority': 'u=1, i'
    }
    json_data = {'password': password,'rePassword': password,'username': 'NEW_USER_NAME_02','email': email}
    params = {
    'cf-turnstile-response': captcha_token,
    }
    response = requests.post(
    'https://gw.sosovalue.com/usercenter/email/anno/sendRegisterVerifyCode/V2',
    params=params,
    headers=headers,
    json=json_data,
    proxies=returned_proxy
    ).json()
 #   print(response)
#    print(params)
    return response

def verify_email(password, mail, code, refcode, returned_proxy):
    headers = {
    'Host': 'gw.sosovalue.com',
    'sec-ch-ua-platform': 'Android',
    'user-device': 'Chrome/131.0.6778.260#Android/15',
    'accept-language': 'en',
    'sec-ch-ua': 'Android',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; 23129RAA4G Build/AQ3A.240829.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.260 Mobile Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://m.sosovalue.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://m.sosovalue.com/',
    'priority': 'u=1, i',
    }
    json_data = {'password': password,'rePassword': password,'username': 'NEW_USER_NAME_02','email': email,'verifyCode': code,'invitationCode': refcode,'invitationFrom':'null'}
    response = requests.post('https://gw.sosovalue.com/usercenter/user/anno/v3/register', headers=headers, json=json_data, proxies = returned_proxy).json()
#    print(response)
    return response

def console(mail, password, code):
    return 'ok'
    # str(x).replace("b'",'').replace("'",'')


def get_captcha():
  global base_url
  while True:
    token = requests.get(f'{base_url}/get').text
    if not token == "No tokens available":
       return token
    else:
       time.sleep(0.3)

while True:
 try:
   email = mail.getmails()
   print('> \033[1;32mNew email :', email)
   password = gtpas()
   decpass = str(base64.b64decode(password.encode())).replace("b'",'').replace("'",'')
   print('\033[0m> \033[1;32mPassword :',decpass)
   captcha_token = get_captcha()
   returned_proxy = random_proxy()
   if 'All proxy used form' in returned_proxy:
       print('\033[1;31mAll proxy used now! end.')
       break
   get_msg = create_account(captcha_token, password, email, returned_proxy)
   if get_msg['code'] == 0:
        print(f'\033[0m>\033[1;32m Email send successfully \033[0m')
   username, domain = email.split('@')
   code = mail.get_verification_link(email, domain)
   value = verify_email(password, email, code, refcode, returned_proxy)
   open('accounts.txt','a').write(f"Email : {email} \nPassword : {decpass} \nToken : {value['data']['token']}\nRefresh Token : {value['data']['refreshToken']}\n--------------------------------\n")
   if value['code'] == 0:
        print(f'>\033[1;32m Email verify successfull \033[0m')
   print(f"\033[1;34m{'-' * 42}\033[0m")
 except Exception as e:print('\033[0m> \033[1;31mError :',str(e) + '\033[1;34m------------------------------------------\033[0m')
