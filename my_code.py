#geeksforgeeks.org  

def make_dict():

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    currency = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}         # complete this line

    return currency

def add_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}

    added_value = foods.add(4, 'dairy', 'yogurt')

    return foods

def remove_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}
    # remove 'veggie': 'carrot' from the dictionary
    removed_value = foods.pop('veggie', 'carrot')

    return foods

def merge_dict():
    # Merge these two dictionaries together so the contents are in numerical order:
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    # add code here
    dict3 = {**dict1, **dict2}
    return dict3     # return new dictionary

def access_key():
    # return the value of the key 'Twenty'
    currency = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

    val = currency.get("Twenty")            # add code to assign the desired value to 'val'
    return val





if __name__ == '__main__':
    # Test your code with this first
    # Change the function to test different sections
    print(make_dict())

