
print("\n---Challenge 1: Letter Index Dictionary---")
word = input("Enter a word: ")

char_indices = {}

for index, char in enumerate(word):
    if char in char_indices:
        char_indices[char].append(index)
    else:
        char_indices[char] = [index]

print(char_indices)

print("\n---Challenge 2: Affordable Items---")

def affordable_items(items_purchase, wallet):
    wallet_amount = int(wallet.replace('$', '').replace(',', ''))

    affordable = []

    for item, price_str in items_purchase.items():
        price = int(price_str.replace('$', '').replace(',', ''))

        if price <= wallet_amount:
            affordable.append(item)

    affordable.sort()

    return affordable if affordable else "Nothing"


# Example tests
items_purchase1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet1 = "$300"
print(affordable_items(items_purchase1, wallet1))  

items_purchase2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet2 = "$100"
print(affordable_items(items_purchase2, wallet2))  


items_purchase3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet3 = "$1"
print(affordable_items(items_purchase3, wallet3))  
