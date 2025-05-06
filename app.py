from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Painel Trader MEXC está funcionando!</h1><p>Deploy via Railway ok.</p>"
