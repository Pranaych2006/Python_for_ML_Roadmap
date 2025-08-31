#Using lambda function
products = [{'name': 'Laptop', 'price': 1200}, {'name': 'Mouse', 'price': 25}, {'name': 'Keyboard', 'price': 75}]
prices = list(map(lambda x: x['price'],products)) #(list contains only prices )
print(prices)
