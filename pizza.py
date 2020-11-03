class Make_pizza():
    def __init__(self,number_of_pizzas=1,yeast_type=0):
        self.number_of_pizzas = number_of_pizzas
        self.yeast_type = yeast_type
        self.flour = self.number_of_pizzas * 250
        self.water = self.number_of_pizzas * 175
        self.yeast = self.number_of_pizzas * 4
        if self.yeast_type != 0:
            self.yeast = self.number_of_pizzas * (0.24*4)
        self.salt = self.number_of_pizzas * 8

    def get_recepie(self):
        return ("""\n
                ###############################\n
                Här är ditt recept för %s pizza/pizzor \n
                ###############################\n               
                Mjöl %s gram\n
                Vatten %s gram\n
                Jäst %s gram\n
                Salt %s gram\n
                ###############################\n
                Instruktioner:\n
                ###############################\n
                1. Blanda ingredieserna\n
                2. Knåda minst 15 minuter\n
                3. Jäs degen i 30 minuter\n
                4. Skapa små bullar på x gram\n
                styck och lägg i ett bleck\n
                5. Jäs i ytterliggare 30 minuter\n
                6. Lägg in blecket i kylen i 24 timmar\n
                ###############################\n

                """% (str(self.number_of_pizzas),str(round(self.flour)),str(round(self.water)),str(round(self.yeast)),str(round(self.salt))))
    def get_formated_recepie(self):
        return ("""\n
                Här är ditt recept för %s pizza/pizzor \n
                \n               
                Mjöl %s gram\n
                Vatten %s gram\n
                Jäst %s gram\n
                Salt %s gram\n
                \n
                Instruktioner:\n
                \n
                1. Blanda ingredieserna\n
                2. Knåda minst 15 minuter\n
                3. Vila degen i 5 minuter\n
                4. Jäs degen i en plastbunke i 20 min \n
                5. Skapa små bullar på 260-280 gram\n
                styck och lägg i ett bleck\n
                6. Lägg in blecket i kylen i 24 timmar\n
                \n

                """% (str(self.number_of_pizzas),str(round(self.flour)),str(round(self.water)),str(round(self.yeast)),str(round(self.salt))))
        
