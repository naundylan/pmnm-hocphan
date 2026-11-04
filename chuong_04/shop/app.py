from flask import Flask, render_template, request, abort
from datetime import datetime
from math import ceil

app = Flask(__name__)

SHOP = {
    "name": "Cà phê sông Hương",
    "address": "12 Lê Lợi, Huế",
    "open": 7,
    "close": 22
}

PROMOTIONS = [
    "Giảm 10% cho sinh viên",
    "Mua 2 tặng 1 vào thứ Hai"
]

MENU = [
    {"name": "Cà phê đen", "price": 20000, "available": True},
    {"name": "Cà phê sữa", "price": 25000, "available": True},
    {"name": "Bạc xỉu", "price": 30000, "available": True},
    {"name": "Trà đào", "price": 35000, "available": True},
    {"name": "Trà vải", "price": 35000, "available": False},
    {"name": "Sinh tố bơ", "price": 40000, "available": True},
    {"name": "Nước ép cam", "price": 30000, "available": True}
]

ITEMS_PER_PAGE = 3


@app.route("/")
def dashboard():
    now = datetime.now()
    hour = now.hour

    is_open = SHOP["open"] <= hour < SHOP["close"]

    return render_template(
        "dashboard.html",
        shop=SHOP,
        promotions=PROMOTIONS,
        hour=hour,
        is_open=is_open
    )


@app.route("/menu")
def menu():
    # Không có page thì mặc định là trang 1
    page_str = request.args.get("page", "1")

    # Kiểm tra page có phải số nguyên không
    try:
        page = int(page_str)
    except (ValueError, TypeError):
        abort(404)

    # Trang phải lớn hơn hoặc bằng 1
    if page < 1:
        abort(404)

    total_pages = ceil(len(MENU) / ITEMS_PER_PAGE)

    # Không cho truy cập trang vượt quá tổng số trang
    if page > total_pages:
        abort(404)

    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    menu_items = MENU[start:end]

    return render_template(
        "menu.html",
        menu=menu_items,
        page=page,
        total_pages=total_pages
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        shop=SHOP
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)