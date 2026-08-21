## Sari-Sari Store Inventory system

### 1. Encapsulation
Encapsulation can be applied by grouping a product's data, such as its name, price, and quantity, together inside a Product() class. Methods such as add_stock(), sell_product(), or update_price() can control how the product's data is changed. This improved organization and prevents the product information from being changed directly or incorrectly.

### 2. Abstraction
Abstraction can be used to show only the important features needed to manage a product while hiding unnecessary implementation details. For example, the user can call a method like sell_produt() without needing to know exactly how the program subtracts the quantity from the available stock. This makes the system easier to use, understand, and maintain.

### 3. Inheritance
Inheritance can be applied by creating a general Product class containing commo properties such as name, price, and quantity. More specific classes, such as FoodProduct or NonFoodProduct, can inherit these properties and methods while adding their on features. This improves the design by reducing repeated codes and allowing related product types to be organized clearly.

### 4. Polymorphism
Polymorphism can allow different types of products to use the same method in different ways. For example, a get_price() method may work differently for regular products and discounted products, even though both belong to the Product class. This makes the program more flexible because one method name can handle different product behaviors.

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful in improving the sari-sari store inventory system. It keeps each product's information and related methods together in one object, making the program more organized. It can also protect important data, such as quantity and price, from being changed incorrectly. As the stores adds more products, encapsulation can make the system easier to manage and maintain.
