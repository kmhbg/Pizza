import pizza
import easygui




number_of_pizzas = easygui.enterbox("Hur många pizzor vill du göra?")
yeast_type = easygui.buttonbox("Vilken jäst bakar du med?",
                           choices = ['Färskjäst', 'Torrjäst'] )

if yeast_type == "Färskjäst":
    yeast_type = 0
else:
    yeast_type = 1

myPizza = pizza.Make_pizza(int(number_of_pizzas),yeast_type)
#print(myPizza.get_recepie())
easygui.msgbox (myPizza.get_formated_recepie())