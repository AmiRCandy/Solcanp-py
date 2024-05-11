import requests , json , string , random
class Solcan :
    def __init__(self):
        self.headers = {
            'authority': 'api.solscan.io',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'origin': 'https://solscan.io',
            'referer': 'https://solscan.io/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.get('https://solscan.io/')
        newheader = {'sol-aut': self.generate_random_string()}
        self.session.headers.update(newheader)
        self.session.options('https://api.solscan.io/v2/publicize/all')
        newheader = self.session.get('https://api.solscan.io/v2/publicize/all').headers['Etag']
        self.session.headers.update({'if-none-match':newheader})
    def generate_random_string(self):
        e = string.ascii_letters + string.digits + "==--"
        t = ''.join(random.choice(e) for _ in range(16))
        r = ''.join(random.choice(e) for _ in range(16))
        n = random.randint(0, 30)
        o = t + r
        i = o[:n] + "B9dls0fK" + o[n:]
        return i
    def getSPL(self,addr) :
        self.session.options('https://api.solscan.io/v2/account?address='+str(addr))
        self.session.get('https://api.solscan.io/v2/account?address='+str(addr))
        self.session.options(f'https://api.solscan.io/v2/account/token/txs?address={addr}&limit=40&offset=0&account_type=account_main')
        response = self.session.get(f'https://api.solscan.io/v2/account/token/txs?address={addr}&limit=10&offset=0&account_type=account_main')
        return json.loads(response.text)
    def getAccountTokens(self,addr) :
        self.session.options('https://api.solscan.io/v2/account/v2/tokens?address='+str(addr))
        response = self.seesion.get('https://api.solscan.io/v2/account/v2/tokens?address='+str(addr))
        return json.loads(response.text)
    def getAccountTransction(self,addr,limit=10) :
        self.session.options(f'https://api.solscan.io/v2/account/transaction?address={addr}&limit={limit}')
        response = self.session.get(f'https://api.solscan.io/v2/account/transaction?address={addr}&limit={limit}')
        return json.loads(response.text)
    def getSolTransfers(self,addr,limit=0,offset=0) :
        self.session.options(f'https://api.solscan.io/v2/account/soltransfer/txs?address={addr}&limit={limit}&offset={offset}')
        response = self.session.get(f'https://api.solscan.io/v2/account/soltransfer/txs?address={addr}&limit={limit}&offset={offset}')
        return json.loads(response.text)
