def linear_search_product(products, target):
      for product in products:
          if product == target:
              return True
      return False
products = ["Rice","Sugar","Milk","Oil","Soap"]
target = Milk
result = linear_search_product(products, target)
  
if result :
      print("Product found")
else:
      print("Product not found")
  
