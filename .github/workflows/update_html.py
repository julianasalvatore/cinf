import requests
from bs4 import BeautifulSoup

# Supondo que você já tem funções para obter os dados climáticos
def obter_dados_climaticos():
    # Seu código para obter e processar dados climáticos
    pass

# Atualizar o arquivo HTML
def atualizar_html():
    dados_climaticos = obter_dados_climaticos()
    with open('0_est_mey.html', 'w') as file:
        file.write('<html><body>\n')
        for chave, valor in dados_climaticos.items():
            file.write(f'<p><strong>{chave}</strong>: {valor}</p>\n')
        file.write('</body></html>\n')

if __name__ == "__main__":
    atualizar_html()
