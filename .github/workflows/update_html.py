name: Atualizar HTML

on:
  schedule:
    - cron: '*/10 * * * *'  # Executa a cada 10 minutos
  workflow_dispatch:

jobs:
  update_html:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v2

    - name: Configurar Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4 deep-translator pytz

    - name: Executar script de atualização do HTML
      run: python atualizar_html.py

    - name: Commit das mudanças
      run: |
        git config --local user.email "you@example.com"
        git config --local user.name "GitHub Actions"
        git add 0_est_mey.html
        git commit -m "Atualização automática do HTML com dados meteorológicos"
        git push
