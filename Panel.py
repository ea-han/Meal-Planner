import tkinter as tk
import tkinter.font as tkFont
import RecipeSearch

class Panel:
    height = 0
    weight = 0
    age = 0
    gender = ''
    tags =''
    ings =''
    favorites =''
    mySearch = RecipeSearch.RecipeSearch()
    
    def __init__(self, root):

        self.height = tk.IntVar()
        self.weight = tk.IntVar()
        self.age = tk.IntVar()
        self.gender = tk.StringVar()
        self.tags = tk.StringVar()
        self.ings = tk.StringVar()
        self.favorites = tk.StringVar()

        #setting title
        root.title("Meal Planner")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # weight
        weight1=tk.Entry(root,textvariable=self.weight)
        weight1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        weight1["font"] = ft
        weight1["fg"] = "#333333"
        weight1["justify"] = "center"
        weight1.place(x=120,y=30,width=70,height=25)

        weightLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        weightLabel["font"] = ft
        weightLabel["fg"] = "#333333"
        weightLabel["justify"] = "center"
        weightLabel["text"] = "Weight (lbs)"
        weightLabel.place(x=20,y=30,width=90,height=30)

        # gender
        gender1=tk.Entry(root,textvariable=self.gender)
        gender1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        gender1["font"] = ft
        gender1["fg"] = "#333333"
        gender1["justify"] = "center"
        gender1.place(x=120,y=60,width=70,height=25)

        genderLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        genderLabel["font"] = ft
        genderLabel["fg"] = "#333333"
        genderLabel["justify"] = "center"
        genderLabel["text"] = "Gender (m or f)"
        genderLabel.place(x=20,y=60,width=90,height=30)

        # age
        age1=tk.Entry(root,textvariable=self.age)
        age1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        age1["font"] = ft
        age1["fg"] = "#333333"
        age1["justify"] = "center"
        age1.place(x=120,y=90,width=70,height=25)

        ageLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        ageLabel["font"] = ft
        ageLabel["fg"] = "#333333"
        ageLabel["justify"] = "center"
        ageLabel["text"] = "Age"
        ageLabel.place(x=20,y=90,width=90,height=30)

        # height
        height1=tk.Entry(root, textvariable = self.height)
        height1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        height1["font"] = ft
        height1["fg"] = "#333333"
        height1["justify"] = "center"
        height1.place(x=120,y=120,width=70,height=25)

        heightLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        heightLabel["font"] = ft
        heightLabel["fg"] = "#333333"
        heightLabel["justify"] = "center"
        heightLabel["text"] = "Height (in)"
        heightLabel.place(x=20,y=120,width=90,height=30)

        # tags
        tags1=tk.Entry(root,textvariable=self.tags)
        tags1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        tags1["font"] = ft
        tags1["fg"] = "#333333"
        tags1["justify"] = "center"
        tags1.place(x=300,y=30,width=271,height=30)

        tagsLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        tagsLabel["font"] = ft
        tagsLabel["fg"] = "#333333"
        tagsLabel["justify"] = "center"
        tagsLabel["text"] = "Tags"
        tagsLabel.place(x=220,y=30,width=70,height=25)

        # ingredients
        ings1=tk.Entry(root, textvariable = self.ings)
        ings1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ings1["font"] = ft
        ings1["fg"] = "#333333"
        ings1["justify"] = "center"
        ings1.place(x=300,y=110,width=270,height=30)

        ingsLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        ingsLabel["font"] = ft
        ingsLabel["fg"] = "#333333"
        ingsLabel["justify"] = "center"
        ingsLabel["text"] = "Ingredients"
        ingsLabel.place(x=220,y=110,width=70,height=25)
        
        # favorites
        favorites1=tk.Entry(root,textvariable=self.favorites)
        favorites1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        favorites1["font"] = ft
        favorites1["fg"] = "#333333"
        favorites1["justify"] = "center"
        favorites1.place(x=120,y=150,width=70,height=25)

        favoritesLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        favoritesLabel["font"] = ft
        favoritesLabel["fg"] = "#333333"
        favoritesLabel["justify"] = "center"
        favoritesLabel["text"] = "Favorites"
        favoritesLabel.place(x=30,y=150,width=70,height=25)

        # calculate button
        calcButton=tk.Button(root)
        calcButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        calcButton["font"] = ft
        calcButton["fg"] = "#000000"
        calcButton["justify"] = "center"
        calcButton["text"] = "Calculate!"
        calcButton.place(x=500,y=210,width=70,height=25)
        calcButton["command"] = self.calculate

 
    def calculate(self):
        
        self.mySearch.searchNutrition(self.weight.get(), self.gender.get(), self.age.get(), self.height.get(), self.tags.get(), self.ings.get(),self.favorites.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = Panel(root)
    root.mainloop()