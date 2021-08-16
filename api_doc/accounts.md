[← BACK](./README.md)

# API Documentation

## Accounts

- ### `POST /accounts`
  Create new account.

  **Request**

  ```ts
  {
    user: {
      username: string
    },
    account: {
      firstName: string,
      lastName: string,
      email: string,
      password: string
    },
    address: {
      number: int,
      street: string,
      city: string,
      country: string,
      apartment?: int
    }
  }
  ```

  **Response**

  ```ts
  {
    id: int,
    username: string
  }
  ```

- ### `POST /login`
  Login.
