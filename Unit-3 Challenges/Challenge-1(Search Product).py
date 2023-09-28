def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices
product_list = ["apple", "cherry", "orange", "apple", "banana", "apple"]
target_product = "apple"
result = linear_search_product(product_list, target_product)
print(result)  
