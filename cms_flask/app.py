from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    orders = [
        {"Pedido": "#130520220434", "Data": "06/06/2017", "Itens": "2", "Valor Total": "R$68,30", "Situação": "Confirmado"},
        {"Pedido": "#130520220433", "Data": "06/06/2017", "Itens": "1", "Valor Total": "R$38,71", "Situação": "Confirmado"},
        {"Pedido": "#130520220432", "Data": "06/06/2017", "Itens": "1", "Valor Total": "R$28,61", "Situação": "Pendente"},
        {"Pedido": "#130520220430", "Data": "30/03/2017", "Itens": "3", "Valor Total": "R$56,43", "Situação": "Confirmado"},
        {"Pedido": "#130520220428", "Data": "21/03/2017", "Itens": "10", "Valor Total": "R$79,46", "Situação": "Confirmado"},
    ]
    return render_template('index.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
