water = 400
milk = 540
grams_of_coffee = 120
number_of_cups = 9
money = 500

def make_coffee():
    global water
    water = int(input("Write how many ml of water the coffee machine has:"))
    global milk
    milk = int(input("Write how many ml of milk the coffee machine has:"))
    global grams_of_coffee
    grams_of_coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
    global number_of_cups
    number_of_cups = int(input("Write how many cups of coffee you will need: "))

    print("For " + str(number_of_cups) + "cups of coffee you will need: ")
    print(str(200 * number_of_cups) + " ml of water")
    print(str(50 * number_of_cups) + " ml of milk")
    print(str(15 * number_of_cups) + " gr of coffee beans")
    

    max_water = water / 200
    max_milk = milk / 50
    max_coffee = grams_of_coffee / 15

    max_number_of_cups = min(max_water, max_milk, max_coffee)

    if number_of_cups > max_number_of_cups:
        print("No, I can make only" + str(int(max_number_of_cups)) + "cups of coffee")
    elif number_of_cups < max_number_of_cups:
        print("Yes, I can make that amount of coffee (and even "+ str(int(max_number_of_cups - number_of_cups)) +" more than that)")
    else:
        print("Yes, I can make that amount of coffee")

    print("Starting to make a coffee")
    print("Grinding coffee beans")
    print("Boiling water")
    print("Mixing boiled water with crushed coffee beans")
    print("Pouring coffee into the cup")
    print("Pouring some milk into the cup")
    print("Coffee is ready!")

def log_state():
    global water
    global milk
    global grams_of_coffee
    global number_of_cups
    global money
    print("-" * 26)
    print("| The coffee machine has: ")
    print(f"| {water} of water ")
    print(f"| {milk} of milk ")
    print(f"| {grams_of_coffee} of coffee ")
    print(f"| {number_of_cups} of cups ")
    print(f"| amount of money:{money}$")
    print("-" * 26)

def check_if_possible(w,m,gr,cups,cash):
    global water
    global milk
    global grams_of_coffee
    global number_of_cups
    global money

    result_list = {"water": water-w ,"milk": milk-m, "coffee":grams_of_coffee - gr, "cups":number_of_cups - cups}

    if((water - w < 0) or (milk - m < 0) or (grams_of_coffee - gr < 0) or (number_of_cups - cups < 0)):
        
        for key in result_list:
            if result_list[key] < 0:
                print(f"I dont have enough ingredients for your coffee. Not enough {key}!")
    else:
        print("I have enough ingredients. Your cup of coffee will be ready in a second!")
        water -= w
        milk -= m
        grams_of_coffee -= gr
        number_of_cups -= cups
        money += cash
        log_state()

def buy_coffee():
    global water
    global milk
    global grams_of_coffee
    global number_of_cups
    global money

    print("Please pick a type of coffee: \nEspresso (250ml water, 16g coffee beans) 4$\nLatte (350ml water, 75ml milk, 20gr coffee beans) 7$\nCappuccino (200ml water, 100ml milk, 12gr coffee beans) 6$")
    coffee_decision = int(input("What do you want to buy? 1 - Espresso | 2 - Latte | 3 - Cappuccino | 4 - to go back to main menu\n"))

    while coffee_decision not in [1, 2, 3, 4]:
        print("Wrong input!")
        coffee_decision = int(input("What do you want to buy? 1 - Espresso | 2 - Latte | 3 - Cappuccino | 4 - to go back to main menu\n"))

    if coffee_decision == 1:
        check_if_possible(250, 0, 16, 1, 4)
            
    elif coffee_decision == 2:
        check_if_possible(350, 75, 20, 1, 7)
        
    elif coffee_decision == 3:
        check_if_possible(200,100,12,1, 6)

    #going back to main menu
    elif coffee_decision == 4:
        make_transaction(True)

def fill_machine():
    global water
    global milk
    global grams_of_coffee
    global number_of_cups

    water_to_add = int(input("How much water you want to add?\n"))
    water += water_to_add
    milk_to_add = int(input("How much milk you want to add?\n"))
    milk += milk_to_add
    grams_of_coffee_to_add = int(input("How many grams of coffee you want to add?\n"))
    grams_of_coffee += grams_of_coffee_to_add
    cups_to_add = int(input("How many cups you want to add?\n"))
    number_of_cups += cups_to_add

    log_state()

def take_money():
    global money

    print(f"You get {money}$")
    money = 0

    log_state()

def make_transaction(back):
    BUY = "buy"
    FILL = "fill"
    TAKE = "take"
    CHECK_STATE = "check"
    EXIT = "exit"
    
    end_transcation = False
    
    while end_transcation == False:
        user_action = input("Please make a decision (buy,fill,take,check,exit): ")

        while user_action not in [BUY,FILL,TAKE,CHECK_STATE,EXIT]:
            user_action = input("Decision is not recognized by the machine! Try again:\n")
        
        if user_action == BUY:
            buy_coffee()
        elif user_action == FILL:
            fill_machine()
        elif user_action == CHECK_STATE:
            log_state()
        elif user_action == TAKE:
            take_money()
        elif user_action == EXIT:
            print("Main menu closed!")
            print("Machine is turining off...")
            break

        if(back == False):
            user_decision = input("Want to make another transaction?\n")
            if user_decision not in ["y","yes","YES","Y"]:
                end_transcation = True
                print("Main menu closed!")
                print("Machine is turining off...")
        else:
            end_transcation = True




if __name__ == "__main__":
    make_transaction(False)

    
    