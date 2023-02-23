# ecommerce-django
E-commerce platform using DRF

## Features
- [x] User Registration
- [x] User login
- [x] Products table in admin panel only
- [x] All users could add to the cart
- [x] All users could make orders with the products in the cart

### Roadmap

1. Create simple Rest APIs endpoints for:
    - [x] Registration
    - [x] Login
    - [x] Add Product model and show it in admin (product fields are: name, price)
    - [x] Get products and the query should:
        - [x] Order by price
        - [x] Search by name
    - [x] add to cart
    - [x] get user cart
    - [x] create an order with products in the cart
    - [x] get user orders

2. [x] Use linter for your code (ex: flake8).

3. [x] Add a Readme file containing instructions to run your code


### Extras
- [x] Adding simple test cases for your code using pytest or another test framework you are familiar with is a plus.
- [ ] Adding nginx configuration and supervisor is a plus.
- [ ] deploying the task on the server is a plus.
- [ ] Using docker and docker-compose with your application is also a plus.


### Project Design (mostly assumptions)
- Used Token Authentication (Storing it in the db, less scalable but simpler to implement)


### Setup Instructions:
1. Create python virtual environment using conda on virtualenv and activate it
2. Install package requirements using pip command within env
3. Setup new postgres user and DB and grant him all privileges on it 
4. Setup sercrets file with the settings.py file accordingly (db_name, host, user, password, port...)
5. run `python manage.py makemigrations`
6. run `python manage.py migrate`
7. run `python manage.py runserver` to start testing the endpoints locally on 127.0.0.1:8000
