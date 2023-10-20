import requests
import random

class Drink():

    def __init__(self):
    # BASE ENDPOINT
        self.endpoint = "https://www.thecocktaildb.com/api/json/v1/1/"

    def get_random(self):
        # RETURN RANDOM COCKTAIL
        url = f"{self.endpoint}random.php"
        response = requests.get(url)
        data = response.json()
        drinks = data["drinks"]

        # SELECT RANDOM DRINK FROM SEARCH RESULTS
        choice = random.choice(drinks)
        id = choice["idDrink"]

        # SEARCH RANDOM SELECTION BY ID
        drink_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}"
        drink_response = requests.get(drink_url)
        drink_json = drink_response.json()
        drink_data = drink_json["drinks"][0]

        # FORMAT RECIPE
        drink_name = drink_data["strDrink"]
        drink_ingredients = [[drink_data["strMeasure1"], drink_data["strIngredient1"]],
                             [drink_data["strMeasure2"], drink_data["strIngredient2"]],
                             [drink_data["strMeasure3"], drink_data["strIngredient3"]],
                             [drink_data["strMeasure4"], drink_data["strIngredient4"]],
                             [drink_data["strMeasure5"], drink_data["strIngredient5"]],
                             [drink_data["strMeasure6"], drink_data["strIngredient6"]],
                             [drink_data["strMeasure7"], drink_data["strIngredient7"]],
                             [drink_data["strMeasure8"], drink_data["strIngredient8"]],
                             [drink_data["strMeasure9"], drink_data["strIngredient9"]],
                             [drink_data["strMeasure10"], drink_data["strIngredient10"]],
                             [drink_data["strMeasure11"], drink_data["strIngredient11"]],
                             [drink_data["strMeasure12"], drink_data["strIngredient12"]],
                             [drink_data["strMeasure13"], drink_data["strIngredient13"]],
                             [drink_data["strMeasure14"], drink_data["strIngredient14"]],
                             [drink_data["strMeasure15"], drink_data["strIngredient15"]],
                             ]

        drink_instructions = drink_data["strInstructions"]

        drink = [drink_name, drink_ingredients, drink_instructions]

        return drink


    def get_by_spirit(self, spirit):
        # SEARCH BY LIQUOR
        spirit = spirit
        url = f"{self.endpoint}filter.php?i={spirit}"
        response = requests.get(url)
        data = response.json()
        drinks = data["drinks"]

        # SELECT RANDOM DRINK FROM SEARCH RESULTS
        choice = random.choice(drinks)
        id = choice["idDrink"]

        # SEARCH RANDOM SELECTION BY ID
        drink_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}"
        drink_response = requests.get(drink_url)
        drink_json = drink_response.json()
        drink_data = drink_json["drinks"][0]

        # FORMAT RECIPE
        drink_name = drink_data["strDrink"]
        drink_ingredients = [[drink_data["strMeasure1"], drink_data["strIngredient1"]],
                                  [drink_data["strMeasure2"], drink_data["strIngredient2"]],
                                  [drink_data["strMeasure3"], drink_data["strIngredient3"]],
                                  [drink_data["strMeasure4"], drink_data["strIngredient4"]],
                                  [drink_data["strMeasure5"], drink_data["strIngredient5"]],
                                  [drink_data["strMeasure6"], drink_data["strIngredient6"]],
                                  [drink_data["strMeasure7"], drink_data["strIngredient7"]],
                                  [drink_data["strMeasure8"], drink_data["strIngredient8"]],
                                  [drink_data["strMeasure9"], drink_data["strIngredient9"]],
                                  [drink_data["strMeasure10"], drink_data["strIngredient10"]],
                                  [drink_data["strMeasure11"], drink_data["strIngredient11"]],
                                  [drink_data["strMeasure12"], drink_data["strIngredient12"]],
                                  [drink_data["strMeasure13"], drink_data["strIngredient13"]],
                                  [drink_data["strMeasure14"], drink_data["strIngredient14"]],
                                  [drink_data["strMeasure15"], drink_data["strIngredient15"]],
                                  ]
        drink_instructions = drink_data["strInstructions"]

        drink = [drink_name, drink_ingredients, drink_instructions]

        return drink

    def search(self, ingredients):

        # IMPROVING USER'S LIST FOR MAXIMUM RESULTS
        ingredients_list = ingredients
        ingredients_list.append('water')
        ingredients_list.append('ice')
        if 'lime' in ingredients_list:
            ingredients_list.append('lime juice')
        if 'lemon' in ingredients_list:
            ingredients_list.append('lemon juice')

        # SEARCH BY FIRST INGREDIENT IN LIST
        url = f"{self.endpoint}filter.php?i={ingredients_list[0]}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            drinks = data["drinks"]

        except:
            drink = [f"Sorry! There were no results with {ingredients_list[0]}. Try again!", "", ""]
            return drink


        # CHECK IF ALL REQUESTED INGREDIENTS ARE IN LIST
        for result in drinks:

            id = result["idDrink"]

            current_drink_url = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}'
            drink_response = requests.get(current_drink_url)
            drink_json = drink_response.json()
            drink_data = drink_json["drinks"][0]

            drink_name = drink_data["strDrink"]
            drink_ingredients = [[drink_data["strMeasure1"], drink_data["strIngredient1"]],
                                  [drink_data["strMeasure2"], drink_data["strIngredient2"]],
                                  [drink_data["strMeasure3"], drink_data["strIngredient3"]],
                                  [drink_data["strMeasure4"], drink_data["strIngredient4"]],
                                  [drink_data["strMeasure5"], drink_data["strIngredient5"]],
                                  [drink_data["strMeasure6"], drink_data["strIngredient6"]],
                                  [drink_data["strMeasure7"], drink_data["strIngredient7"]],
                                  [drink_data["strMeasure8"], drink_data["strIngredient8"]],
                                  [drink_data["strMeasure9"], drink_data["strIngredient9"]],
                                  [drink_data["strMeasure10"], drink_data["strIngredient10"]],
                                  [drink_data["strMeasure11"], drink_data["strIngredient11"]],
                                  [drink_data["strMeasure12"], drink_data["strIngredient12"]],
                                  [drink_data["strMeasure13"], drink_data["strIngredient13"]],
                                  [drink_data["strMeasure14"], drink_data["strIngredient14"]],
                                  [drink_data["strMeasure15"], drink_data["strIngredient15"]],
                                  ]
            drink_instructions = drink_data["strInstructions"]

            drink_result_list = [item[1] for item in drink_ingredients if item[1] is not None]

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
