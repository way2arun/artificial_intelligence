

def check_sugar(sugar_grams:str):
    sugar_value = sugar_grams[:2]
    if (sugar_value > "24" ):
        print("This is a higher value of Sugar Consumption for a men and for Women")
    else:
        print("Good to Exercise and control the intake, no processed sugar intake")

def check_carbs(carbs_grams:str):
    carbs_value = carbs_grams[:2]
    if (carbs_value > "100"):
        print("This is more of a moderate carbohydrate intake. It is very appropriate for people who are lean, active and are simply trying to stay healthy and maintain their weight.")
    else:
        print("Proper Exercise and healthy life style is required, go for portion control")
def check_proteins(protein_grams:str):
    proteins_value = protein_grams[:2]
    if (proteins_value > "46"):
        print("Exercise is very important if you are consuming more than the amount of protein")
    else:
        print("Portion Control and good exercise is good for better living")

def check_sodium(sodium_grams:str):
    sodium_value = sodium_grams[:2]
    if (sodium_value > "20"):
        print("Less the intake of Sodium, Sodium attracts water, increase the blood pressure and causes hypertension")
    else:
        print("Always be limited, dont cross the limit")

def check_fat(fat_grams:str):
    fat_value = fat_grams[:2]
    if (fat_value > "22"):
        print("Portion Control is must, this is higher")
    else:
        print("No fat in the food, that does not mean its good, there might be some other Nutrions in the same will go bad")

def check_calorie(calories:str):
    if (calories > "2500"):
        print("High Calorie food intake, not good for long run")
    else:
        print("Should take minimum calorie, for energy boosting,")