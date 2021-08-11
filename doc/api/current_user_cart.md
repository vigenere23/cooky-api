[← BACK](./current_user.md)

# API Documentation

## Current User - Cart

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
