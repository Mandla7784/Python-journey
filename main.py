import json


def main(args = None):
    dipsla_items()

#Rendering items

def dipsla_items():
        
    try:
        FILE_NAME  = "data.json"
        
        with open(FILE_NAME , "r", errors="ignore ",) as file:
            data = json.load(file)
            #getting each item from list 
            displyed_item_title = list(map(lambda item : item["title"], data))
            for product in displyed_item_title:
                print(product)

            else:
                print("Not found")
    except FileNotFoundError as error:
        print(error.__traceback__)


        
def add_to_cart(item):
    pass

if __name__=="__main__":
    main(0)