# coding: utf-8

    
shoes = {'name': 'Nike Shoes', 'price': 600}
# discount = 0.25
discount = 2

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

print(apply_discount(shoes, discount))