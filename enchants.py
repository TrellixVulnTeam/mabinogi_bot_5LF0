import requests
from bs4 import BeautifulSoup

def spoon(url):
    enchant_info = ''
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    if soup.find_all('table', {"class": "mabitable"}):
        for data in soup.find_all('td'):
            enchant_info += data.get_text(separator=" ")
            enchant_info += '\n'
        return enchant_info
    else:
        return False

def keyword_strip(user_message):
    user_message = user_message[9:]
    return user_message


def send_link(result_links, search_words):
    send_link = set()
    search_words = search_words.lower()
    for link in result_links:
        text = link.text.lower()
        if search_words in text and ("rank" in text or "enchant" in text):
            send_link.add(link.get('href'))
    return send_link

class EnchantSearcher:
    def __init__(self):
        self.base_url = 'https://wiki.mabinogiworld.com/view/'

    def base_url(self, url):
        if spoon(self.base_url + url):
            return spoon(self.base_url + url)
        else:
            return False

    def base_case(self, base_key):
        path_key = base_key[9:]
        path_key_split = path_key.split(" ")
        capitalized = [x.capitalize() for x in path_key_split]
        if len(path_key_split) == 3:
            new_pathway = f'https://wiki.mabinogiworld.com/view/{capitalized[0]}_({capitalized[1]}_{capitalized[2]})'
            return spoon(new_pathway)
        else:
            new_pathway = "_".join(capitalized)
            if spoon(self.base_url + new_pathway + "_(Enchant)"):
                return spoon(self.base_url + new_pathway+"_(Enchant)")
            else:
                return False

    def send_link(self, result_links, search_words):
        send_link = set()
        search_words = search_words.lower()
        for link in result_links:
            text = link.text.lower()
            if search_words in text and "rank" in text:
                send_link.add(link.get('href'))
        return send_link

    def searcher(self, keyword):
        keywords = keyword.split()
        capitalized_keyword = [x.capitalize() for x in keywords]
        whole_keyword = "_".join(capitalized_keyword)
        whole_keywords = whole_keyword + "_(Enchant)"
        url = self.base_url + whole_keywords
        if spoon(url):
            print('searcher')
            return spoon(url)
        else:
            es2 = EnchantSearcher()
            return es2.searcherparttwo(whole_keyword)


    def searcherparttwo(self, keyword):
        url = self.base_url + keyword
        if spoon(url):
            return spoon(url)
        else:
            es3 = EnchantSearcher()
            return es3.searcher_part_three(keyword)

    def searcher_part_three(self, keyword):
        url = f'https://wiki.mabinogiworld.com/index.php?search={keyword}+enchant&title=Special%3ASearch&go=Go'
        response = requests.get(url, "html.parser")
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('a')
        return send_link(result_links, keyword)



