from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument('--disable-dev-shm-usage')

# Use o caminho para o ChromeDriver manualmente
service = Service('/diretorio/para/o/drive/do/chrome//chromedriver_134')

browser = webdriver.Chrome(service=service, options=options)

#Para corrigir bug de desconexão do site
#alterna entre o portal CIPM e outro portal
browser.get('http://www.google.com')

#Loga no CIPM
url = "https://user:senha@cipm.fcsh.unl.pt/login"
browser.get(url)

#Acessa página principal do CIPM Corpus
url = "https://cipm.fcsh.unl.pt/corpus/"

browser.get(url)

#Coleta título para nomear a pasta
#dir_name = "default"
#h1 = browser.find_elements(By.TAG_NAME, "h1")
#if h1:
#    dir_name = h1[0].text

# Encontrar todas as células da tabela (<td>)
td_elements = browser.find_elements(By.TAG_NAME, "td")

# Armazenar os links extraídos
links_pais = []
titles_pais = []

#Mapeando sujeiras para remover
links_to_remove = ['https://cipm.fcsh.unl.pt/', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=2', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=3', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=4', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=5', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=6', 'https://cipm.fcsh.unl.pt/gencontent.jsp?id=17', 'https://cipm.fcsh.unl.pt/passwd.jsp', 'https://cipm.fcsh.unl.pt/logout', 'http://www.fct.mct.pt/']


# Iterar pelas células e buscar links dentro delas
for td in td_elements:
    a_tags = td.find_elements(By.TAG_NAME, "a")  # Encontrar <a> dentro do <td>
    for a in a_tags:
        href = a.get_attribute("href")
        if href and href not in links_to_remove:  # Evita None
            titles_pais.append(a.text)
            links_pais.append(href)


#Calcula percentual de conclusao
#total = len(links)
#counter = 1
#del links_pais[0:62]

for i in range(len(links_pais)):

    print(f"Coletando {titles_pais[i]}")

    #Login again
    browser.get('http://www.google.com')


    url = "https://danielms:32249095@cipm.fcsh.unl.pt/login"
    browser.get(url)
    
    #Get the new link
    #print(link)
    browser.get(links_pais[i])
    
    td_elements = browser.find_elements(By.TAG_NAME, "td")

    # Armazenar os links extraídos
    links_filhos = []
    titles_filhos = []
    
    for td in td_elements:
        a_child_tags = td.find_elements(By.TAG_NAME, "a")  # Encontrar <a> dentro do <td>
        for a in a_child_tags:
            href = a.get_attribute("href")
            if href and href not in links_to_remove:  # Evita None
                titles_filhos.append(a.text)
                links_filhos.append(href)

    total = len(links_filhos)
    counter = 1

    for j in range(len(links_filhos)):

        #Login again
        browser.get('http://www.google.com')

        url = "https://danielms:32249095@cipm.fcsh.unl.pt/login"
        browser.get(url)
    
        #Get the new link
        browser.get(links_filhos[j])      
        html_content = browser.page_source

        # Usando BeautifulSoup para extrair apenas o texto
        #Get text
        soup = BeautifulSoup(html_content, 'html.parser')
        texto = soup.get_text()

        #Valida se o texto foi coletado por inteiro
        verifica = texto.strip()
        if verifica.endswith("Projecto financiado por FCT-MCES.") is False:
            print(f"Verifique o arquivo {nome_arquivo}")
        else:
            print("Texto coletado com sucesso.")

        # Salvando o texto em um arquivo de texto
        nome_arquivo = f'./{titles_pais[i]}/{titles_filhos[j]}.txt'
        os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)  # Cria o diretório, se não existir

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)

        #Informa o percentual de conclusao
        concluido = round((counter / total) * 100,2)
        print(f"{concluido}% concluido")
        counter += 1

        time.sleep(1)  # Tempo de espera entre as requisições


browser.quit()
