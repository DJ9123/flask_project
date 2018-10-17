from flask import Flask, render_template, abort, request

app = Flask(__name__)

@app.route("/")
def index():
    # http://localhost:5000/?pizza=beef&drink=sprite
    pizza = request.args.get("pizza")
    drink = request.args.get("drink")
    
    # my_dictionary = {"pizza": pizza, "drink": drink}

    pizzas = ["pepperoni", "beef", "chicken", "veggie"]
    if pizza in pizzas:
        return render_template("index.html", pizza=pizza, drink=drink)
    else:
        return abort(404)

# @app.route("/<string:pizza>")
# def index(pizza):
#     pizzas = ["pepperoni", "beef", "chicken", "veggie"]
#     if pizza in pizzas:
#         return f"You ordered a {pizza} pizza"
#     else:
#         return abort(404)
#     # return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)