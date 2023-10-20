from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from get_drink import Drink
from search_form import SearchForm

app = Flask(__name__)
Bootstrap(app)

drink = Drink()
app.config['SECRET_KEY'] = "fdasfgfsdfisdhjnk;glbm75derfw4afsd54f"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/spirits")
def spirits():
    return render_template("spirits.html")


@app.route("/random")
def random():
    drink_to_gen = drink.get_random()
    print(drink_to_gen)
    return render_template("result.html", drink=drink_to_gen)


@app.route("/<spirit>", methods=['GET'])
def by_spirit(spirit):
    spirit_to_search = spirit
    drink_to_show = drink.get_by_spirit(spirit_to_search)
    return render_template("result.html", drink=drink_to_show)

@app.route("/search-your-bar", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "POST":
        ingredients = form.ingredients.data
        list_of_ingredients = ingredients.split(', ')
        drink_to_show = drink.search(list_of_ingredients)
        return render_template("result.html", drink=drink_to_show)
    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
