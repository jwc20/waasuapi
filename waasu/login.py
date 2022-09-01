import requests
from bs4 import BeautifulSoup


class LogIn(object):
    def __init__(self):
        pass

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    @staticmethod
    def _load_page():
        # login_url = "https://account.ycombinator.com/"

        # s = Session()
        # # s.headers.update({
        # #     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
        # # })

        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # }

        # headers = {
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
        # }

        # req = Request("POST", url, data=data, headers=headers)
        # prepped = req.prepare()

        # r = s.get(login_url, headers=headers)
        # html = r.text
        # soup = BeautifulSoup(html, "lxml")

        cookies = {
            '_bf_session_exists': 'BAhU--aa46bb667960b8fed5cd9d1cd8c1716513cb2768',
            '_bf_session_key': 'ZHN5RC9raWV3MzRSajY2aHpHcmdURGo3Y3ZlNmNQU0VqMGViWWw1b2dvZWo3VW1iV0dNNE1ZVWx6cjdRb1BCMnNrK1hsUGVkUnFJaGpOdXJzbFdzREVzQmU3UVZVRk1ZdTM4OGlOb1dVL1RqVUYxczBlWHhUZTlqRDBhK2lwbkFJZlZ1ZEd1WVJUSHJRNDNuTGdkcVJ6QzVyRFNHQ2hMOFc3U3FsR1paRHZUWHJxaW8remEwUjVreG5hRWVJQk9aLS0yM1NyeHVrMzlPYnNKckJtb0NYcldBPT0%3D--08c4b3eafe6160d467822c722716a79b989c0d10',
        }

        headers = {
            'authority': 'account.ycombinator.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_bf_session_exists=BAhU--aa46bb667960b8fed5cd9d1cd8c1716513cb2768; _bf_session_key=ZHN5RC9raWV3MzRSajY2aHpHcmdURGo3Y3ZlNmNQU0VqMGViWWw1b2dvZWo3VW1iV0dNNE1ZVWx6cjdRb1BCMnNrK1hsUGVkUnFJaGpOdXJzbFdzREVzQmU3UVZVRk1ZdTM4OGlOb1dVL1RqVUYxczBlWHhUZTlqRDBhK2lwbkFJZlZ1ZEd1WVJUSHJRNDNuTGdkcVJ6QzVyRFNHQ2hMOFc3U3FsR1paRHZUWHJxaW8remEwUjVreG5hRWVJQk9aLS0yM1NyeHVrMzlPYnNKckJtb0NYcldBPT0%3D--08c4b3eafe6160d467822c722716a79b989c0d10',
            'if-none-match': 'W/"5e61048e6f0046cc6bb84fafef4540cc"',
            'referer': 'https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        
        response = requests.get('https://account.ycombinator.com/', cookies=cookies, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        return soup

    @staticmethod
    def _pick_form(soup_data):
        login_container = soup_data.find_all("input")
        return login_container

    def log_in(self):
        # self._load_page()
        print(self._get_login(self._load_page()))


if __name__ == "__main__":
    LogIn().log_in()
