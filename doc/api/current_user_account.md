[← BACK](./current_user.md)

# API Documentation

## Current User - Account

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
