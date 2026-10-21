from flask import abort, jsonify, make_response, redirect, request, url_for
from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

SHOP = { "name": "Cà phê sông Hương",
        "address": "12 Lê Lợi, Huế",
        "open": 7, "close": 22}

PROMOTIONS = ["Giảm 10% cho sinh viên", "Mua 2 tặng 1 vào thứ Hai"]
MENU = [{"name": "cà phê đen", "price": 20000, "available": True},
        {"name": "bạc xỉu", "price": 30000, "available": False},
        {"name": "matcha latte", "price": 36000, "available": True},
        {"name": "trà đào", "price": 15000, "available": False},
        {"name": "trà sữa trân châu", "price": 30000, "available": False}]



@app.route("/")
def dashboard():
    gio = request.args.get("gio", default=None, type=int)
    if gio is None:
        gio = datetime.now().hour
    hour = datetime.now().hour

    is_open = SHOP["open"] <= gio < int(SHOP["close"])

    return render_template("dashboard.html", shop=SHOP, promotion=PROMOTIONS, hour=hour, is_open=is_open)

@app.route("/menu")
def menu():

    return render_template("menu.html", menu=MENU)


if __name__ == "__main__":
    app.run(debug=True, port=8000)