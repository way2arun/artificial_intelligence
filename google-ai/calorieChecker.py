
import io
import os
from google.cloud import vision
from utils.vision_utils import init_vision, detect_image
from facts import check_sugar, check_carbs, check_proteins, check_sodium, check_fat,check_calorie

def calorie_checker(path, file_name):
    """Captures the text contents in the jpg"""
    #Initialize the vision API
    client  = init_vision()
    #Get the path and jpg
    file_name = os.path.join(path,file_name)
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    nutrition_facts = response.text_annotations
    print('Nutrition Check:')
    
    sugar_found = False
    carbs_found = False
    calorie_found = False
    fat_found = False
    sodium_found = False
    protein_found = False
   

    for nutrition in nutrition_facts:
        #text_msg = format(text.description)
        if ("sugars"  in nutrition.description.lower() or sugar_found == True):
            sugar_found = True
            if (nutrition.description.lower()[-1:] == "g"):
                sugar_grams = nutrition.description
                sugar_found = False
            
        if ("carbohydrate" in nutrition.description.lower() or carbs_found == True):
            carbs_found = True
            if (carbs_found):
                if (nutrition.description.lower()[-1:] == "g"):
                    carbs_grams = nutrition.description
                    carbs_found = False

        if ("protein" in nutrition.description.lower() or protein_found == True):
            protein_found = True
            if(nutrition.description.lower()[-1:] == "g"):
                protein_grams = nutrition.description
                protein_found = False

        if (calorie_found):
            calorie_found = False
            calories = nutrition.description
            
        if ("Calories" in nutrition.description):
            calorie_found = True
        
        if ("sodium" in nutrition.description.lower() or sodium_found == True):
            sodium_found = True
            if (nutrition.description.lower()[-2:] == "mg" or nutrition.description.lower()[-1:] == "g"):
                sodium_grams = nutrition.description
                sodium_found = False

        if ("fat" in nutrition.description.lower() or fat_found == True):
            fat_found = True
            if (nutrition.description.lower()[-1:] == "g"):
                fat_grams = nutrition.description
                fat_found = False
       
    print("Total Sugars :%s"%sugar_grams)
    check_sugar(sugar_grams)
    print("Total Carbohydrates :%s" %carbs_grams)
    check_carbs(carbs_grams)
    print("Total Proteins :%s"%protein_grams)
    check_proteins(protein_grams)
    print("Total Calories :%s"%calories)
    check_calorie(calories)
    print("Total Sodium :%s"%sodium_grams)
    check_sodium(sodium_grams)
    print("Total Fat :%s"%fat_grams)
    check_fat(fat_grams)

    
    
    
if __name__ == '__main__':
    path = os.path.dirname(__file__)
    file_name = 'resources/cocacola.jpg'
    calorie_checker(path, file_name)