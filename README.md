📝 Descrição
Script de Web Scraping em Python para automação de coleta de textos no portal CIPM (Corpus Informatizado do Português Medieval). O script acessa páginas protegidas por login, navega por links de categorias e subcategorias, extrai o conteúdo textual das páginas e salva localmente em arquivos .txt organizados em pastas.

🚀 Tecnologias utilizadas
Python 3

Selenium – automação de navegação web

BeautifulSoup – extração de conteúdo HTML

ChromeDriver – driver do navegador Chrome

📡 API
❌ Este projeto não possui API.
É um script de automação de navegação web (web scraping) usando Selenium.

💻 Requisitos para rodar
Python instalado (versão 3.x)

Instalar as bibliotecas necessárias:
```
bash
pip install selenium
pip install beautifulsoup4
```

Chrome instalado na máquina

ChromeDriver compatível com a sua versão do Chrome
Baixe em: https://sites.google.com/chromium.org/driver/

Configurar o caminho do ChromeDriver no código:

```
python
service = Service('/caminho/para/o/chromedriver')
```

Alterar o trecho do login no código para suas credenciais:

```
url = "https://usuario:senha@cipm.fcsh.unl.pt/login"
```

⚙️ Como executar
Clone o repositório:

```
bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Instale as dependências:

```
bash
pip install selenium beautifulsoup4
```

Edite o caminho do ChromeDriver e as credenciais no código.

Execute o script:

```
bash
python robo_coleta_textos.py
```

Os arquivos .txt serão salvos em pastas organizadas pelo nome das categorias e subcategorias.
