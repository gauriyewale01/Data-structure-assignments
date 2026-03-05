## Task 1 
products=["wheat", "rice", "sugar", "salt" ,"oil", "chips"]
categories={"grocery", "grocery", "grocery", "grocery", "grocery", "snacks"}
sample_product=("chips", 20, "snacks")

print("second product is ", products[1], "and last product is ", products[5])

products.extend(["tea", "coffee"])

print(products)



## Task 2
categories_set=set(categories)
categories.add("beverages")
print(categories)
print("beverages" in categories)




##Task 3
price_dict={"wheat": 30, "rice": 40, "sugar": 50, "salt": 20, "oil": 100, "chips": 60}
price_dict["tea"]= 40
price_dict["sugar"]=60
price_dict.pop("oil")

avg_price= sum(price_dict.values())/len(price_dict)
print("average price of products is ", avg_price)




##Task 4
catalog=[("wheat", 30, "grocery"), ("rice", 40, "grocery"), ("sugar", 50, "grocery"), ("salt", 20, "grocery"), ("oil", 100, "grocery"), ("chips", 60, "snacks")]
category_to_products={"grocery": ["wheat", "rice", "sugar", "salt", "oil"], "snacks": ["chips"]}
print(category_to_products["grocery"])
