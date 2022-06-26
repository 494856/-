from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '╔═╗┌─┐┌┬┐┬ ┬┌─┐',
    '╚═╗├┤  │ │ │├─┘',
    '╚═╝└─┘ ┴ └─┘┴'
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF SAIF==============')
    print(f' Version: 2.0 |  Telegram:@HackerAttack_BOT{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] 添加新账户'+n)
    print(lg+'[2] 过滤所有被禁账号'+n)
    print(lg+'[3] 删除特定账号'+n)
    print(lg+'[5] 显示所有账户'+n)
    print(lg+'[6] 退出'+n)
    a = int(input('\n输入您的选择： '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] 输入要添加的帐户数量: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] 输入电话号码: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Saved all accounts in vars.txt')
            clr()
            print(f'\n{lg} [*] 从新帐户登录\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Login successful')
                c.disconnect()
            input(f'\n 按回车键进入主菜单...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] 没有账户！ 请添加一些并重试')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\n按回车键进入主菜单...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\n按回车键进入主菜单...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] 选择要删除的帐户\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] 输入一个选项: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] 帐户已删除{n}')
        input(f'\n按回车键进入主菜单...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Checking for updates...')
        try:
            # https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/manager.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('按回车键进入主菜单...')
        else:
            print(f'{lg}[i] Your Telegram-Members-Adder is already up to date')
            input('按回车键进入主菜单...')
    elif a == 5:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        print(f'\n{cy}')
        print(f'\t电话号码列表是')
        print(f'==========================================================')
        i = 0
        for z in accs:
            print(f'\t{z[0]}')
            i += 1
        print(f'==========================================================')
        input('\n按回车键进入主菜单')
    elif a == 6:
        clr()
        banner()
        exit()
