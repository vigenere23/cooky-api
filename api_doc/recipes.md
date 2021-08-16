[← BACK](./README.md)

# API Documentation

## Recipes

- ### `GET /recipes?name=<search_name>`
  Get all recipes.

  **Filters**

  - name: Recipe name (inclusive).

- ### `POST /recipes`
  Create new recipe.

  **Request**

  ```ts
  {
    name: string,
    directives: string,
    ingredients: [
      {
        id_Ingredient: int,
        id_QuantityUnit: int,
        totalQuantity: float
      }
    ]
  }
  ```

  **Response**

  ```ts
  {
    id: int,
    id_User: int,
    name: string,
    directives: string,
    ingredients: [
      {
        id_Ingredient: int,
        id_QuantityUnit: int,
        totalQuantity: float
      }
    ]
  }
  ```

- ### `GET /recipes/<recipe_id>`
  Get recipe by id.

- ### `DELETE /recipes/<recipe_id>`
  Delete recipe.

- ### `PATCH /recipes/<recipe_id>`
  Modify recipe.

  **Request**

  ```ts
  {
    name?: string,
    directives?: string
  }
  ```

- ### `GET /recipes/<recipe_id>/comments`
  Get all comments of recipe.

- ### `POST /recipes/<recipe_id>/comments`
  Add comment to recipe.

  **Request**

  ```ts
  {
    text: string
  }
  ```

- ### `PUT /recipes/<recipe_id>/ingredientQuantity`
  Modify recipe ingredient quantiy.

  **Request**

  ```ts
  {
    id_Ingredient: int,
    totalQuantity: float
  }
  ```

- ### `GET /recipes/<recipe_id>/ingredients`
  Get all ingredients of recipe.

- ### `POST /recipes/<recipe_id>/likes`
  Like recipe.

- ### `DELETE /recipes/<recipe_id>/likes`
  Unlike recipe.

- ### `POST /recipes/<recipe_id>/ratings`
  Add rating to recipe.

  **Request**

  ```ts
  {
    value: int
  }
  ```

- ### `PUT /recipes/<recipe_id>/ratings`
  Modify recipe rating.

  **Request**

  ```ts
  {
    value: int
  }
  ```
