from fileinput import filename


class RecipeSearch:
    import pandas as pd
    import random as rd

    recipeIndexList = []
    foodDf = 0
    meals = []


    def __init__(self):
        self.foodDf = self.pd.read_csv('RAW_recipes.csv')
        self.foodDf.head()

# returns a list of recipe indices w/ right tags and ingredients
    def searchIngredients(self,myIngredients,myTags):
        
        recipeIngsIndexList = []
        tagsIndexList = self.searchTag(myTags)

        for recipe in tagsIndexList: # recipe is an index
            counter = 0 # matching ingredients
            ingList = eval(self.foodDf.loc[recipe,'ingredients'])
            

            for ing in ingList:
                for myIng in myIngredients:
                    if (myIng == ing or myIng in ing):
                        counter += 1
            if (counter == len(ingList)):
                recipeIngsIndexList.append(recipe)
            

        return recipeIngsIndexList

    # searches recipes based on ingredients + cals
    def searchTag(self,myTags):
        recipeTagsIndexList = []
        recipeCounter = 0

        for recipeTagString in self.foodDf.tags:  # recipeTagString is an string
            
            recipeCounter += 1
            counter = 0
            recipeTags = eval(recipeTagString)

            for tag in myTags:  # in input tags list, z = tag
                if (tag in recipeTags):
                    counter += 1
            if (counter == len(myTags)):
                recipeTagsIndexList.append(recipeCounter)
                
        return recipeTagsIndexList

    def toFile(self, fileName, meals):
        with open(fileName, "a") as o:
             for m in meals:
                print(self.foodDf.loc[m,'name'],file=o)
                print('Index:', m,file=o)
                print('\n',file=o)
                print(self.foodDf.loc[m,'description'],file=o)

                # Nutrition info
                print('\n', "NUTRITION:",file=o)
                nutList = eval(self.foodDf.loc[m,'nutrition'])
                del nutList[5]
                del nutList[3]
                del nutList[2]
                nameNuts = ['Calories: ','Protein(g): ','Carbs(g): ', 'Fats(g): ']
                for k in range(len(nutList)):
                    print(nameNuts[k],2 * nutList[k],file=o)

                
                # prints ingredients as a bullet point list
                print('\n', "INGREDIENTS:",file=o)
                ingrList = eval(self.foodDf.loc[m,'ingredients'])
                for ingr in ingrList:
                    print('-', ingr,file=o)
                
                # prints steps as a numbered list
                print('\n', "STEPS:",file=o)
                stepNum = 1
                stepsList = eval(self.foodDf.loc[m,'steps'])
                for step in stepsList:
                    print(str(stepNum) + ".", step,file=o)
                    stepNum += 1
                print('\n\n',file=o)

                
    def checkFavorites(self,recipeIndicesList,favorites):

        
        length = int((len(recipeIndicesList)/3)/len(favorites))

        for x in favorites:
            for y in range(len(recipeIndicesList)):
                if recipeIndicesList[y] == x:
                    for z in range(length):
                        recipeIndicesList.append(x)
                       

    def searchNutrition(self, weight, gender, age, height, tagString, ingString, filename, favoriteString):

        # weight lbs, gender "f"/"m", age years, height inches
        bmr = 0
        meals = []
        
        tags = tagString.split(',') # easy,breakfast --> ['easy', 'breakfast']
        # easy --> ['easy']
        
        ings = ingString.split(',')
        
        favorites = favoriteString.split(',')

        recipeIndicesList = self.searchIngredients(ings,tags)

        if (len(favorites) > 0):
            self.checkFavorites(recipeIndicesList,favorites)

        if gender == "m":
            bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.75 * age)
        if gender == "f":
            bmr = 65.51 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

        bmr = 2200

        protein = 0.2 * bmr
        carb = 0.55 * bmr
        fat = 0.3 * bmr

    # take 3 random recipes, check if nutrition info matches w/i 100 cal buffer
        # recipesList = recipeIndexList

        

        caloriesMatch = False
        while (caloriesMatch == False):
            meals = []
            for i in range(3):
                randRecipeIn = recipeIndicesList[self.rd.randint(0,len(recipeIndicesList)-1)]
                meals.append(randRecipeIn)
                
            if (self.checkCals(meals, bmr, protein, carb, fat)):
                caloriesMatch = True
        
        self.toFile(filename,meals)


    # check if given recipes in list meals have matching nutrition count
    # return T or F

    def printRecipeInfo(self, meals):
        for m in meals:
            print(self.foodDf.loc[m,'name'])
            print('Index:', m)
            print('\n')
            print(self.foodDf.loc[m,'description'])

            # Nutrition info
            print('\n', "NUTRITION:")
            nutList = eval(self.foodDf.loc[m,'nutrition'])
            del nutList[5]
            del nutList[3]
            del nutList[2]
            nameNuts = ['Calories: ','Protein(g): ','Carbs(g): ', 'Fats(g): ']
            for k in range(len(nutList)):
                print(nameNuts[k],2 * nutList[k])

            
            # prints ingredients as a bullet point list
            print('\n', "INGREDIENTS:")
            ingrList = eval(self.foodDf.loc[m,'ingredients'])
            for ingr in ingrList:
                print('-', ingr)
            
            # prints steps as a numbered list
            print('\n', "STEPS:")
            stepNum = 1
            stepsList = eval(self.foodDf.loc[m,'steps'])
            for step in stepsList:
                print(str(stepNum) + ".", step)
                stepNum += 1
            print('\n\n')

    def checkCals(self, meals, bmr, protein, carb, fat):
        totalCals = 0
        totalP = 0
        totalC = 0
        totalF = 0
        
        # print (meals, bmr, protein, carb, fat, " \n\n")

        for recipe in meals:
            # converts string foodDf.nutrition into a list
            nutritionStr = self.foodDf.nutrition[recipe]
            nutritionStr = nutritionStr.strip('[]')
            nutrition = nutritionStr.split(", ")

            totalCals += float(nutrition[0]) * 2
            totalP += float(nutrition[4]) * 2
            totalC += float(nutrition[6]) * 2
            totalF += float(nutrition[1]) * 2
            
        # print('Protein: ', totalP, ' Carbs: ', totalC, ' Fats: ', totalF)
        # print('Calories: ',totalCals)
        # print('\n\n')
        
        if totalCals <= bmr + 100 and totalCals >= bmr - 100:
            return True
        else:
            return False
        
        


# and totalP >= protein and totalC >= carb - 100 and totalC <= carb + 100 and totalF <= fat + 100 and totalF >= fat - 100:
# ['calories','total fat (PDV)','sugar (PDV)','sodium (PDV)','protein (PDV)','saturated fat (PDV)','carbohydrates (PDV)']
# ['asian'],['cider vinegar', 'sugar', 'ketchup', 'molasses', 'garlic', 'serrano chili pepper', 'fresh ginger', 'salt'])


#     def searchNutrition(self, weight, gender, age, height, tags, ings):

