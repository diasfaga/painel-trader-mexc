from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Aplicação Flask mínima no Railway funcionando!'

if __name__ == '__main__':
    app.run()
