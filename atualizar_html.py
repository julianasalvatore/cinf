import requests
from bs4 import BeautifulSoup
import re

# Função para capturar dados climáticos
def obter_dados_climaticos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    dados_climaticos = {
        'temperatura': 'Não disponível',
        'estado_tempo': 'Não disponível',
        'vento': 'Não disponível',
        'rajadas': 'Não disponível',
        'hora_atual': 'Não disponível'
    }

    # Temperatura Atual
    temp_div = soup.find('lib-display-unit', {'type': 'temperature'})
    if temp_div:
        temp_f = float(temp_div.find('span', class_='wu-value-to').text.strip())
        temp_c = (temp_f - 32) * 5 / 9
        dados_climaticos['temperatura'] = f"{temp_c:.1f}°C"

    # Estado do Tempo
    condition_div = soup.find('div', class_='condition-icon')
    if condition_div:
        estado_tempo = condition_div.find('p').text.strip()
        dados_climaticos['estado_tempo'] = estado_tempo

    # Vento
    wind_div = soup.find('div', class_='condition-wind')
    if wind_div:
        wind_speed = wind_div.find('header', class_='wind-speed').text.strip()
        gusts_div = wind_div.find('p')
        if gusts_div:
            wind_gusts = gusts_div.find('lib-display-unit').find('span', class_='wu-value-to').text.strip()
            dados_climaticos['vento'] = f"{wind_speed} km/h"
            dados_climaticos['rajadas'] = f"{wind_gusts} km/h"

    # Hora Atual
    timestamp_div = soup.find('p', class_='timestamp')
    if timestamp_div:
        hora_atual_match = re.search(r'(\d{1,2}:\d{2} [APM]{2}) GMT-03:00', timestamp_div.text)
        if hora_atual_match:
            dados_climaticos['hora_atual'] = hora_atual_match.group(1)

    return dados_climaticos

# Função para atualizar o HTML
def atualizar_html(dados_climaticos):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dados Climáticos</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .container {{ max-width: 800px; margin: auto; padding: 20px; }}
            h1 {{ text-align: center; }}
            .dados {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Dados Climáticos</h1>
            <div class="dados">
                <p><strong>Temperatura Atual:</strong> {dados_climaticos['temperatura']}</p>
                <p><strong>Estado do Tempo:</strong> {dados_climaticos['estado_tempo']}</p>
                <p><strong>Vento:</strong> {dados_climaticos['vento']}</p>
                <p><strong>Rajadas:</strong> {dados_climaticos['rajadas']}</p>
                <p><strong>Hora Atual:</strong> {dados_climaticos['hora_atual']}</p>
            </div>
        </div>
    </body>
    </html>
    """

    with open('0_est_mey.html', 'w') as file:
        file.write(html_template)

# URL das estações meteorológicas
url_conego = 'https://www.wunderground.com/weather/br/nova-friburgo/INOVAF28'
url_caledonia = 'https://www.wunderground.com/weather/br/nova-friburgo/INOVAF18'

# Obter dados
dados_conego = obter_dados_climaticos(url_conego)
dados_caledonia = obter_dados_climaticos(url_caledonia)

# Atualizar o HTML
atualizar_html(dados_conego)  # Atualiza com dados da estação Cônego
