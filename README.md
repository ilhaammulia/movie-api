# Movie API

Simple Movie API

## API Reference - Movies

#### Get all movies

```http
  GET /api/movies
```

| Parameter  | Type     | Description                         |
| :--------- | :------- | :---------------------------------- |
| `api_key`  | `string` | **Required**. Your API key          |

**Response:**

`200 - OK`

    {
        "error": null,
        "data": [
            {
                "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f",
                "title": "The Pope's Exorcist",
                "release_date": "2023-04-05",
                "language": "English",
                "genres": ["Action", "Horror"],
                "popularity": 5089.969,
                "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
            }
        ]
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "Movie not found",
        "data": null
    }

#### Get movie

```http
  GET /api/movies/:id
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `id`      | `string` | **Required**. Id of movie to fetch |
| `api_key` | `string` | **Required**. Your API key         |

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f",
            "title": "The Pope's Exorcist",
            "release_date": "2023-04-05",
            "language": "English",
            "genres": ["Action", "Horror"],
            "popularity": 5089.969,
            "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "Movie not found",
        "data": null
    }

#### Create movie

```http
  POST /api/movies
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

**Body:**

    {
        "title": "The Pope's Exorcist",
        "release_date": "2023-04-05",
        "language": "English",
        "genres": ["Action", "Horror"],
        "popularity": 5089.969,
        "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
    }

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f",
            "title": "The Pope's Exorcist",
            "release_date": "2023-04-05",
            "language": "English",
            "genres": ["Action", "Horror"],
            "popularity": 5089.969,
            "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

#### Update movie

```http
  PUT /api/movies/:id
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `id`      | `string` | **Required**. Id of movie to update |
| `api_key` | `string` | **Required**. Your API key          |

**Body:**

    {
        "title": "The Pope's Exorcist",
        "release_date": "2023-04-05",
        "language": "English",
        "genres": ["Action", "Horror"],
        "popularity": 5089.969,
        "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
    }

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f",
            "title": "The Pope's Exorcist",
            "release_date": "2023-04-05",
            "language": "English",
            "genres": ["Action", "Horror"],
            "popularity": 5089.969,
            "synopsis": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "Movie not found",
        "data": null
    }

#### Delete movie

```http
  DELETE /api/movies/:id
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `id`      | `string` | **Required**. Id of movie to delete |
| `api_key` | `string` | **Required**. Your API key          |

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f"
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "Movie not found",
        "data": null
    }

## API Reference - Users

#### Login

```http
  POST /api/users/login
```

| Parameter  | Type     | Description                 |
| :--------- | :------- | :-------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "24da12f3-80ff-40a6-9ae4-139255e856d6",
            "api_key": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        }
    }

`404 - Not Found`

    {
        "error": "User not found",
        "data": null
    }

#### Create User

```http
  POST /api/users
```

**Body:**

    {
        "username": "newuser",
        "password": "password123"
    }

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "24da12f3-80ff-40a6-9ae4-139255e856d6"
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "User not found",
        "data": null
    }

#### Update user

```http
  PUT /api/users/:id
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `id`      | `string` | **Required**. Id of user to update |
| `api_key` | `string` | **Required**. Your API key         |

**Body:**

    {
        "username": "usernew",
        "password": "newpassword123"

    }

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "24da12f3-80ff-40a6-9ae4-139255e856d6",
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "User not found",
        "data": null
    }

#### Delete user

```http
  DELETE /api/users/:id
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `id`      | `string` | **Required**. Id of user to delete |
| `api_key` | `string` | **Required**. Your API key         |

**Response:**

`200 - OK`

    {
        "error": null,
        "data": {
            "id": "214b535b-2683-40cd-aaa2-2bb4879eec3f"
        }
    }

`401 - Unauthorized`

    {
        "error": "Unauthorized",
        "data": null
    }

`404 - Not Found`

    {
        "error": "User not found",
        "data": null
    }
