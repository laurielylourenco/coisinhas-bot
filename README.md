# coisinhas-bot
Aprendendo fazer um bot para Instagram que usa de web scraping em Python, fazendo uso do ChromeDriver para automação do navegador Google Chrome.

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados antes de executar o bot:

1. Python: Versão 3.x
2. Selenium: Uma biblioteca para automação de navegador. Pode ser instalado com o comando:
   ```bash
   pip install selenium
   ```
3. ChromeDriver: Um WebDriver para o navegador Google Chrome. Baixe e instale a versão compatível com o seu navegador a partir do [site oficial](https://sites.google.com/a/chromium.org/chromedriver/).

## Configuração

Antes de executar o bot, você precisa configurar algumas informações no arquivo `.env`. Preencha as variáveis com as suas credenciais e configurações:

```python
# config.py

# Configurações do Instagram
SENHA_INSTAGRAM = 'seu_usuario'
USER_INSTAGRAM = 'sua_senha'

## Executando o Bot

Para executar o bot , utilize o script `bot.py`:

```bash
python3 bot.py
```

O bot irá abrir o navegador Google Chrome, fazer login na conta especificada.

## Aviso Legal

Este projeto é apenas para fins educacionais e não deve ser usado para violar os Termos de Serviço do Instagram. O uso inadequado deste bot pode resultar na suspensão ou encerramento da sua conta do Instagram. Use-o por sua própria responsabilidade.
