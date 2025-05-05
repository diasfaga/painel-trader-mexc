from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    saldo = {
        'usdt': 1000,
        'futuros': 750,
        'margem': 500
    }
    posicoes = [
        {'par': 'BTC/USDT', 'lado': 'LONG', 'quantidade': 0.01, 'pnl': '+5%'},
        {'par': 'ETH/USDT', 'lado': 'SHORT', 'quantidade': 0.5, 'pnl': '-2%'}
    ]
    logs = [
        'Análise: BTC/USDT rompeu resistência',
        'Sinal: ETH/USDT abaixo da média de 50'
    ]

    html = '''
    <h1>Painel Trader MEXC</h1>
    <h2>Saldo</h2>
    <ul>
        <li>USDT: {{ saldo.usdt }}</li>
        <li>Futuros: {{ saldo.futuros }}</li>
        <li>Margem: {{ saldo.margem }}</li>
    </ul>
    <h2>Posições Abertas</h2>
    <ul>
    {% for p in posicoes %}
        <li>{{ p.par }} - {{ p.lado }} - {{ p.quantidade }} - PnL: {{ p.pnl }}</li>
    {% endfor %}
    </ul>
    <h2>Logs / Sinais</h2>
    <ul>
    {% for log in logs %}
        <li>{{ log }}</li>
    {% endfor %}
    </ul>
    <p><em>Versão demo com dados fictícios.</em></p>
    '''
    return render_template_string(html, saldo=saldo, posicoes=posicoes, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
