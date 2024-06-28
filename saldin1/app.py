from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {"name": "Beras Emas", "price": 10000, "image": "2.png"},
        {"name": "Beras Kepal Super", "price": 15000, "image": "3.png"},
        {"name": "Beras Merah Premium", "price": 20000, "image": "4.png"}
    ]
    return render_template('index.html', items=items)

@app.route('/order/<item_name>', methods=['GET', 'POST'])
def order(item_name):
    items = {
        "Beras Emas": 10000,
        "Beras Kepal Super": 15000,
        "Beras Merah Premium": 20000
    }
    price = items.get(item_name, 0)
    if request.method == 'POST':
        quantity = int(request.form['quantity'])
        total_price = price * quantity
        return render_template('thank_you.html', total_price=total_price)
    return render_template('order.html', item_name=item_name, price=price)

if __name__ == '__main__':
    app.run(debug=True)
