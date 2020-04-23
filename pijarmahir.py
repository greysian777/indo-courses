from bs4 import BeautifulSoup

html = ' '.join(open('./Pijar Mahir.html').read().splitlines())
soup = BeautifulSoup(html, 'lxml')
seluruh_p = soup.find_all('p')
with open('pijarmahir.txt', 'w') as f:
    for p in seluruh_p:
        p = p.text
        if len(p.split())>2:
            f.writelines(f'{p}\n')

