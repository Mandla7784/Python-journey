import json

class Item:
    def __init__(self , title ,price) -> None:
        self.title = title
        self.price = price


class Cart:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item , quanity=1):
        
        if item.id  in self.items:
            self.items[item.id]["quzntity"] += quanity
        else:
            self.items[item.id] = {"item":item , "quantity":quanity}
    
    def remove_item(self,item_id):
        if item_id in self.items:
            del self.items[item_id]
    
    def view_cart(self):
        total_price = 0

        for _ , info  in  self.items.items():
            item = info["item"]
            quanity = info["quantity"]
            total_price+= item.price * quanity
            print(f"{item.title} (x{quanity}): ${item.price:.2f} each")
        print(f"Total Price: ${total_price:.2f}")

def main(args = None):
    dipsplay_items()

#Rendering items

def dipsplay_items():
        
    try:
        FILE_NAME  = "data.json"
        
        with open(FILE_NAME , "r", errors="ignore ",) as file:
            data = json.load(file)
            delete_item_from_cart("1",data)
           
            #getting each item from list 
            displyed_item_title = list(map(lambda item : item["title"], data))
            for product in displyed_item_title:
                print(product)
                add_to_cart(product)
            user_input  = input("Enter a product you want to add: ").lower()

            if user_input.strip() in displyed_item_title:

                new_display = list(filter(lambda item : item["id"] != user_input))
                print(f"\n These are new items  {new_display}")
            else:
                print("Not found")
       
            
    except FileNotFoundError as error:

        print(error.__traceback__)
#Add to cart //basket

def add_to_cart(item):
    CART_PATH= "cart.csv"   
    if not CART_PATH:
        raise FileNotFoundError
    else:
        with open(CART_PATH , "a") as file:
            file.writelines(item)


def delete_item_from_cart(itemID , items):

    new_items = list(filter(lambda item : item["id"]  != itemID , items))
    return new_items


def sub_total():
    subtotal = 0

    with open("cart.csv","r") as file:
        data = file.readlines()
        print(data)

sub_total()

if __name__=="__main__":
    main()
    
    item1 = Item(1,"Wireles Mouse"),29.99
    cart = Cart()
    cart.add_item(item1)
    cart.view_cart()