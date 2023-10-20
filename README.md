<h1 align="center">Bar Cart</h1>

<p align="center">
This is a Flask app that uses the Cocktail.db API to generate a random cocktail, generate a random cocktail with
a specific spirit, or search ingredients the user already has depending on the user choice.</p>



## Links

- [Repo](https://github.com/kelseychristensen/Day-95-API  "bar-cart")

## Screenshots

#### Home
![Home](/readme_images/home.gif "Home")

#### By Spirit
![Spirits](/readme_images/spirits.gif "Spirits")

#### Search your bar
![Search](/readme_images/search.gif "Search")

#### Result
![Results](/readme_images/results.PNG "Results")


### Built with

- Python
- Flask
- HTML
- CSS
- Jinja
- Bootstrap
- WTForm
- Cocktail DB API

### What went into this project

Simple Flask server with only 4 templates, but a lot of time creating the artifacts for the UI (e.g. the little shaker and liquor bottles)
as well as a LOT of time that went into the search feature. 


### What I learned

This was my first time passing a string as opposed to an integer (like an item index, for example) into a URL and then a Flask function, so there was a little bit of debugging and angst that went into that.

Also, I learned how to have an image shake on hover with CSS.

The biggest part of this project was satisfying the needs of the search function. A recipe returned from the search needed to: 
1) Return a cocktail if ALL the ingredients required were listed by the user 
2) Return a cocktail EVEN IF if didn't use an item listed by the user. 

I fussed around for a while making sure this worked and added some improvements (e.g. assuming that the user likely has ice and water, and that if they have lemons or limes they have lemon juice and lime juice as well. Probably a hundred more improvements like this could be added with more testing.)

I also added some exception handling: you get a JSON error if you filter results by an ingredient which no cocktails use and the function filters by the user's first ingredient. If this happens, the user gets feedback that there are no cocktails with their first listed ingredient which I think works pretty well.


### Continued development

Probably needs more testing to identify possible other exceptions. 


```python
            matched_ingreds = []

            for item in drink_result_list:
                if item and item.lower() not in ingredients_list  not in ingredients_list and item.title() not in ingredients_list:
                    pass
                else:
                    matched_ingreds.append(item)

                if len(matched_ingreds) == len(drink_result_list):
                    drink = [drink_name, drink_ingredients, drink_instructions]
                    return drink

        drink = ["Sorry! There were no results for the ingredients you specified. Try again!", "", ""]
        return drink
```

```html
<div class="row">

        <div id="returned_ingredients" class="col-6">
        {% for item in drink[1] %}
            {% if item[0]  == None or item[1] == None %}
                    <p></p>
                {% else %}
                    <p class="item">{{ item[0] }} {{item[1]}}</p>
                {% endif %}

        {% endfor %}

                </div>

        <div class="col-6">

                <p>{{drink[2]}}</p>

                </div>

</div>
```

```css
@keyframes shake {
  0% {  transform: translate(-10px, -10px) rotate(5deg); }
  10% { transform: translate(-10px, -10px) rotate(-5deg); }
  20% { transform: translate(-10px, -10px) rotate(5deg); }
  30% { transform: translate(-10px, -10px) rotate(-5deg); }
  40% { transform: translate(-10px, -10px) rotate(5deg); }
  50% { transform: translate(-10px, -10px) rotate(-5deg); }
  60% { transform: translate(-10px, -10px) rotate(5deg); }
  70% { transform: translate(-10px, -10px) rotate(-5deg); }
  80% { transform: translate(-10px, -10px) rotate(5deg); }
  90% { transform: translate(-10px, -10px) rotate(-5deg); }
  100%{ transform: translate(-10px, -10px) rotate(5deg); }
}
```

## Acknowledgements

Could not have done this without [Cocktail DB](https://www.thecocktaildb.com/ "Cocktail DB").

[This](https://www.w3schools.com/howto/howto_css_shake_image.asp "W3 Schools") also helped, although I customized it to achieve the effect I wanted through trial and error. 

## Author

Kelsey Christensen

- [Profile](https://github.com/kelseychristensen "Kelsey Christensen")
- [Email](mailto:kelsey.c.christensen@gmail.com?subject=Hi "Hi!")
- [Dribble](https://dribbble.com/kelseychristensen "Hi!")
- [Website](http://kelseychristensen.com/ "Welcome")
