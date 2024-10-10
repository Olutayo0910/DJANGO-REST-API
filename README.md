# Product API

This project provides a simple REST API for managing products, allowing users to list, create, retrieve, update, and delete products. The API is built using Django and Django REST Framework.

## Features

- **List all products**: Retrieve a list of all available products.
- **Create a new product**: Add a new product to the database.
- **Retrieve a product**: Get detailed information on a specific product by ID.
- **Update a product**: Modify an existing product.
- **Delete a product**: Remove a product or delete all products.

## Prerequisites

Before running this project, ensure that you have the following installed on your machine:

- Python 3.x
- Django
- Django REST Framework

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/product-api.git
   cd product-api

2. **Create and activate a virtual environment**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Set up the database**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Run the development server**
    ```bash
    python manage.py runserver

## API Endpoints

### List All Products
- **URL**: `/products/`
- **Method**: `GET`
- **Description**: Fetches all products from the database.

### Create a New Product
- **URL**: `/products/`
- **Method**: `POST`
- **Description**: Creates a new product.

#### Request Body (example):
```bash
{
  "name": "Product Name",
  "description": "Product Description",
  "price": 100.00
}

### Retrieve a Product
- **URL**: `/products/<pk>/`
- **Method**: `GET`
- **Description**: Retrieves a product by its primary key (pk).

### Update a Product
- **URL**: `/products/<pk>/`
- **Method**: `PUT`
- **Description**: Updates the details of a product.

### Delete a Product
- **URL**: `/products/<pk>/`
- **Method**: `DELETE`
- **Description**: Deletes a product by its primary key.

### Delete All Products
- **URL**: `/products/`
- **Method**: `DELETE`
- **Description**: Deletes all products from the database.

## Views

### ProductListCreate
- **Endpoint**: `/products/`
- **Methods**: `GET`, `POST`, `DELETE`
- **Description**: Handles listing all products, creating a new product, and deleting all products.

### ProductRetrieveUpdateDestroy
- **Endpoint**: `/products/<pk>/`
- **Methods**: `GET`, `PUT`, `PATCH`, `DELETE`
- **Description**: Handles retrieving, updating, and deleting a single product by its pk.

### ProductListView
- **Endpoint**: `/products/`
- **Methods**: `GET`
- **Description**: Handles listing all products (can be used for more customized list views).

## Running Tests
To run tests for this project:

```bash
python manage.py test

## Author
[Olutayo Ogunlade](https://github.com/Olutayo0910)
