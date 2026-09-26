from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    a = 0
    b = 0
    cong = 0
    tru = 0
    nhan = 0
    chia = 0

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])

        cong = a + b
        tru = a - b
        nhan = a * b
        chia = a / b

    return render_template(
        "math.html",
        a=a,
        b=b,
        cong=cong,
        tru=tru,
        nhan=nhan,
        chia=chia
    )

if __name__ == "__main__":
    app.run(debug=True)