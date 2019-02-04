####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "crazy"
signature_flavors = ["vanilla","popcorn","sweety"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("our menu :")
    for item in menu :
        print("- %s (SAR %s)" %(item,menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print("- %s" % item)
    
   
    # for i in range(0, len(original_flavors)):
    # 	print (original_flavors[i])

    




def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu : 
        return True 
    elif order in original_flavors : 
        return True 
    elif order in signature_flavors : 
        return True
    else : 
        return False 
            
    
     


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    

    while True:
        order = input("please enter your order: ")
        if order == ("exit"): 
            break
        if is_valid_order(order) == True :
            order_list.append(order)
        elif is_valid_order(order) == False :
            print ("error")
            break

    else:
            print("ivalid order , please type again")

    return order_list	


    


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total > 5 : 
        return True 
    else : 
        return False	


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list : 
        if order in menu :
            total += menu[order]
        elif order in signature_flavors : 
            total += signature_price
        else:
            total += original_flavors		

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    total = get_total_price(order_list)
    for order in order_list :
        print(order)
        
    print("your total price is: %s SR" % (total))
    if accept_credit_card(total):
        print("pay by credit card or cash")
    else:
        print("you can pay by cash only")

    print("thank you for using %s as your path" %(cupcake_shop_name))