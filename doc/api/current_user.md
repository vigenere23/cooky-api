[← BACK](./README.md)

# API Documentation

## Current User

- ### `GET /user`
  Get current user.

  **Response**

  ```ts
  {
    id: int,
    username: string
  }
  ```

- ### `GET /user/account`
  Get current user account.

  **Response**

  ```ts
  {
    id: int,
    id_User: int,
    id_Address: int,
    firstName: string,
    lastName: string,
    email: string,
    address: {
      id: int,
      number: int,
      street: string,
      city: string,
      country: string,
      apartment?: int
    }
  }
  ```

- ### `PATCH /user/account`
  Modify current user account.

  **Request**

  ```ts
  {
    email?: string,
    password?: string
  }
  ```

  **Response**

  ```ts
  {
    id: int,
    id_User: int,
    id_Address: int,
    firstName: string,
    lastName: string,
    email: string,
    address: {
      id: int,
      number: int,
      street: string,
      city: string,
      country: string,
      apartment?: int
    }
  }
  ```

- ### `GET /user/account/address`
  Get current user address.

  **Response**

  ```ts
  {
    id: int,
    number: int,
    street: string,
    city: string,
    country: string,
    apartment?: int
  }
  ```

- ### `PATCH /user/account/address`
  Modify current user address.

  **Request**

  ```ts
  {
    number?: int,
    street?: string,
    city?: string,
    country?: string,
    apartment?: int
  }
  ```

  **Response**

  ```ts
  {
    id: int,
    number: int,
    street: string,
    city: string,
    country: string,
    apartment?: int
  }
  ```

- ### `GET /user/cart`
  Get current user cart.

- ### `GET /user/cart/items`
  Get current user cart items.

- ### `POST /user/cart/items`
  Add item to current user cart.

- ### `DELETE /user/cart/items/<ingredient_id>`
  Delete item from current user cart.

- ### `PUT /user/cart/items/<ingredient_id>`
  Modify item from current user cart.

  **Request**
  
  ```ts
  {
    multiplier: int
  }
  ```

- ### `GET /user/commands`
  Get current user commands.

- ### `POST /user/commands`
  Create a command for current user.
