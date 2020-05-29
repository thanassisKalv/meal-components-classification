import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

f = open("foodsOntology.txt", "r")
ofoods = f.read().split()[1:]
f = open("cookingStyle.txt", "r")
cook_style = f.read().split()[1:]
onto_foods = []
for fo in ofoods:
    onto_foods.append(" ".join(fo.split("_")))
print(cook_style)


with open('template.json', "rb") as f:
    classified = json.load(f)
#pp.pprint(classified)

with open('meal-combinations-data.json', "rb") as f:
    meals = json.load(f)


meal_plans = meals["meal_plans"]
# Note that all meals["meal_plan_versions"] have length == 1 ...
# pp.pprint(meals[["meal_plan_versions"][0]["meals"][0]["meal_components"])

check_lens = []
#f = open("foodlist.txt", "w")
print(len(meal_plans))

for mlplan in meal_plans:
    mealPlan = mlplan["meal_plan_versions"][0]
    # check_lens.append( len (mealPlan["meals"]))
    for meal in mealPlan["meals"]:
        for component in meal["meal_components"]:
            for choice in component["meal_component_choices"]:
                #f.write(choice["food"]["name"]+"\n")
                if choice["food_id"] in classified["existing"]:
                    continue
                newFood = {}
                newFood["food_id"] = choice["food_id"]
                newFood["food_name"] = choice["food"]["name"]
                newFood["onto_foods"] = []
                newFood["onto_cooking_style"] = ""
                
                # some dummy string processing, food is search with a following comma or a plural "s" 
                # of course there are expeptions --> todo: some better NLP
                for ofood in onto_foods:
                    if (" "+ofood.lower()+"," in newFood["food_name"].lower() or \
                        " "+ofood.lower()+" " in newFood["food_name"].lower() or \
                        " "+ofood.lower()+"s" in newFood["food_name"].lower() or \
                        ofood.capitalize()+" " in newFood["food_name"] or \
                        ofood.capitalize()+"," in newFood["food_name"] or \
                        ofood.capitalize()+"s" in newFood["food_name"]) and \
                        "without "+ofood.lower() not in newFood["food_name"].lower():
                        newFood["onto_foods"].append(ofood)

                for cookstyle in cook_style:
                    if " "+cookstyle.lower() in newFood["food_name"].lower() or\
                        "-"+cookstyle.lower() in newFood["food_name"].lower():
                        newFood["onto_cooking_style"] = cookstyle
                if newFood["onto_cooking_style"]=="":
                    newFood["onto_cooking_style"] = "raw"

                classified["existing"].append(newFood["food_id"])
                classified["correspondences"].append(newFood)

del classified["existing"]
del classified["correspondences"][0]
print( len(classified["correspondences"]))

with open('foods-from-mealPlans.json', 'w', encoding='utf-8') as f:
    json.dump(classified, f, ensure_ascii=False, indent=4)