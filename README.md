# Boutique Ado
B2C E-Commerce Django-based Web Application. It is a fully functional online store with a shopping cart, checkout, and payment capabilities, as well as the admin interface to manage the store.

Live Demo: https://boutique-ado-b2c.herokuapp.com/

Repo: https://github.com/FlashDrag/boutique-ado


## User Stories
#### Epic: Viewing and Navigation
- As a Shopper, I want to be able to view a list of products so that I can select some to purchase
- As a Shopper, I want to be able to view the details of a product so that I can identify the price, description, product rating, image and available sizes
- As a Shopper, I want to be able quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase
- As a Shopper, I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much
#### Epic: Registration and User Accounts
- As a Shopper, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile
- As a Shopper, I want to be able to easily login or logout so that I can access my personal account information
- As a Shopper, I want to be able to easily recover my password in case I forget it so that I can recover access to my account
- As a Shopper, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful
- As a Shopper, I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information
#### Epic: Sorting and Searching
- As a Site User, I want to be able to sort the list of available products so that I can easily identify the best-rated, best-priced and categorically sorted products
- As a Shopper, I want to be able to sort a specific category of products so that I can find the best-priced or best-rated product in a specific category or sort the products in that category by name
- As a Shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best-priced or best-rated product across broad categories, such as "clothing" or "homeware"
- As a Shopper, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase
- As a Shopper, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available
#### Epic: Purchasing and Checkout
- As a Shopper, I want to be able easily select the size and quantity of a product when purchasing it, so that I can ensure I don't accidentally select the wrong product, size or quantity
- As a Shopper, I want to be able to view items in my bag to be purchased, so that I can identify the total cost of my purchase and all items I will receive
- As a Shopper, I want to be able to adjust the quantity of individual items in my bag, so that I can easily make changes to my purchase before checkout
- As a Shopper, I want to be able to easily enter my payment information so that I can check out quickly and with no hassles
- As a Shopper, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
- As a Shopper, I want to be able to view an order confirmation after checkout, so that I can verify I haven't made any mistakes
- As a Shopper, I want to be able to receive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records
#### Epic: Admin and Store Management
-  As a Store Owner, I want to be able to add a product to the store, so that I can sell it to customers.
-  As a Store Owner, I want to be able to edit/update a product, so that I can change the price, description, image or any other attribute of the product.
-  As a Store Owner, I want to be able to delete a product, so that I can remove it from the store.


## Features
#### User Authentication and Authorization
- [x] User registration
- [x] User login with email confirmation(temporary disabled)
- [x] User logout

#### User Profile
- [x] Order history
- [x] Order email confirmation
- [x] Save delivery information

#### List of Products
- [x] All products
- [x] Clothing products
- [x] Homeware products
- [x] Special offers

#### Product Details
- [x] Product category(clickable)
- [x] Product price
- [x] Product rating
- [x] Product image
- [x] Product Description
- [x] Product sizes
- [x] Product Quantity
- [x] Add to bag button

#### Search
- [x] Search by keywords in the product name and description

#### Sorting
- [x] Sort by price (ascending and descending)
- [x] Sort by rating (ascending and descending)
- [x] Sort by name (ascending and descending)
- [x] Sort by category (ascending and descending)

#### Shopping Bag
- [x] Add product to bag
- [x] Remove a product from the bag
- [x] View bag
- [x] View and adjust the number of each product in the bag
- [x] View a subtotal cost of each product in the bag
- [x] Delivery calculation
- [x] Grand total

#### Checkout (Stripe)
- [x] Checkout form with delivery information
- [x] Card payment

## Technologies Used
- [Python 3.11](https://www.python.org/)
- [Django 3.2](https://docs.djangoproject.com/en/3.2/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
- [jQuery 3.4](https://jquery.com/)

## Payment (Stripe)
Python Django - Build a user, payment and order management system
https://www.youtube.com/watch?v=ncsCnC3Ynlw&t=11263s

#### Test card numbers for Stripe
https://stripe.com/docs/testing?testing-method=card-numbers

- ##### Successful payment
`4242424242424242`

- ##### Declined payments
`4000000000000002` - card declined
`4000000000009995` - insufficient funds
`4000000000009987` - lost card
`4000000000009979` - stolen card

- ##### 3D Secure
`4000002500003155` - 3D Secure authentication required
