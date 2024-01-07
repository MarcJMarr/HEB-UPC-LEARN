import random
import time

opt1 = {
    'premium bananas' : 4011,
    'small limes' : 4048,
    'small avocados' : 4046,
    'small lemons' : 4033,
    'large avocados' : 4225,
    'cucumbers' : 4062,
    'roma tomatos' : 4087,
    'organic bananas' : 94011,
    'cilantro' : 4889,
    'green onions' : 4068,
}

opt2 = {
    'green bell peppers' : 4065,
    'premium white grapes' : 3343,
    'sweet onions' : 4166,
    'garlic' : 4608,
    'russet potato' : 4072,
    'red bell peppers' : 4088,
    'green cabbage' : 4069,
    'jumbo avocados' : 4770,
    'zucchini squash' : 4067,
    'premium red grapes' : 3344,
}

opt3 = {
       'jumbo white onions' : 4663,
    'celery' : 4577,
    'jumbo yello onions' : 4093,
    'broccoli' : 4548,
    'small navel oranges' : 4013,
    'xl navel oranges' : 4012,
    'bulk tomato on vine' : 4664,
    'yello corn' : 4078,
    'iceberg lettuce' : 4061, 
}

opt4 = {
    'premium bananas' : 4011,
    'small limes' : 4048,
    'small avocados' : 4046,
    'small lemons' : 4033,
    'large avocados' : 4225,
    'cucumbers' : 4062,
    'roma tomatos' : 4087,
    'organic bananas' : 94011,
    'cilantro' : 4889,
    'green onions' : 4068,
    'green bell peppers' : 4065,
    'premium white grapes' : 3343,
    'sweet onions' : 4166,
    'garlic' : 4608,
    'russet potato' : 4072,
    'red bell peppers' : 4088,
    'green cabbage' : 4069,
    'jumbo avocados' : 4770,
    'zucchini squash' : 4067,
    'premium red grapes' : 3344,
}

opt5 = {
    'premium bananas' : 4011,
    'small limes' : 4048,
    'small avocados' : 4046,
    'small lemons' : 4033,
    'large avocados' : 4225,
    'cucumbers' : 4062,
    'roma tomatos' : 4087,
    'organic bananas' : 94011,
    'cilantro' : 4889,
    'green onions' : 4068,
    'green bell peppers' : 4065,
    'premium white grapes' : 3343,
    'sweet onions' : 4166,
    'garlic' : 4608,
    'russet potato' : 4072,
    'red bell peppers' : 4088,
    'green cabbage' : 4069,
    'jumbo avocados' : 4770,
    'zucchini squash' : 4067,
    'premium red grapes' : 3344,
    'jumbo white onions' : 4663,
    'celery' : 4577,
    'jumbo yello onions' : 4093,
    'broccoli' : 4548,
    'small navel oranges' : 4013,
    'xl navel oranges' : 4012,
    'bulk tomato on vine' : 4664,
    'yello corn' : 4078,
    'iceberg lettuce' : 4061,
}

def get_random_item(producedict):
    random_item = random.choice(list(producedict.items()))
    return random_item

def main():
    random_product, random_upc = get_random_item(producedict)

    attempts = 0
    

    while attempts < trueattmpts:

        user_input = input(f"{random_product}\nPlease type the upc: ")
    
        if user_input != str(random_upc):
            print("Error, Wrong UPC")
            attempts = 0
            
        else:
            print("Correct!")
            attempts += 1
            if trueattmpts > 1:
                print(f"correct attempts {attempts}")

def optionsgiven():
    print("You have 5 different sets to choose from:")
    print("1 = First ten codes")
    print("2 = Second ten codes")
    print("3 = Final 9 codes")
    print("4 = First twenty codes")
    print("5 = All codes")
    
def successattmpts():
    print("How many times would you like to input a code correctly?")
    print("This is just to build repitition and does not impact the amount of codes you would like to learn.")

                
            
        




while True:

    correct = 0

    optionsgiven()

    
    while True:

        try:
            print("Which set do you want to work on?")
            chosenset = int(input())
            if chosenset >= 1 and chosenset <= 5:
                break
            else:
                print("Please choose from the given options")
                continue
        except ValueError:
            print("Please choose from the given options")

    print(f"you have chosen option {chosenset}")
        
    if chosenset == 1:
        producedict = opt1

    elif chosenset == 2:
        producedict = opt2

    elif chosenset == 3:
        producedict = opt3
    
    elif chosenset == 4:
        producedict = opt4

    elif chosenset == 5:
        producedict = opt5



    while True: 
     try:
        successattmpts()
        trueattmpts = int(input())
        break
     except ValueError:
         print("Please type a number (if you don't know what to put type 1)")
    

    while True:
        try:
            print("how many codes do you want to attempt?")
            goal = int(input())
            break
        except ValueError:
            print("Enter a valid number")

        print("type the corrisponding UPC to the item given, remember to use the paper if you come across a code you are not familiar with.")

    while correct < goal: 
        get_random_item(producedict)
        main()
        correct += 1


    print(f"you have completed {goal} \n codes successfully")
    time.sleep(1)
    
    

    
    print("Do you want to learn more? y/n")
    learnmore = input()

    if learnmore.lower == 'y':
        continue

    elif learnmore.lower == 'n':
        break

print("Goodbye!")
time.sleep(2)
quit()