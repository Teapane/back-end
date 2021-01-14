# Matrimania Backend

## Introduction

Matrimania was a Capstone project completed by members of Turing's Frontend Engineering and Backend Engineering programs.

The purpose of Matrimania is to provide wedding photographers an organized way to gather wedding attendees/guests for specific wedding photos.

This repo serves as the backend API for the frontend application.

Links for both applications can be found below:
- [Matrimania API](https://matrimania-backend.herokuapp.com/) (pending)
- [Matrimania Application](https://matrimania-client.herokuapp.com/)

## Tech Stack
  * Python 3.7
  * Django 3.1.1
  * PostgreSQL
  * TravisCI
  * Docker

## Learning Goals

## Contributors

### Backend Team
* Tyler Fields
  * [GitHub](https://github.com/fieldstyler)
  * [LinkedIn](https://www.linkedin.com/in/tylerfields93/)
* Norma Lopez
  * [GitHub](https://github.com/IamNorma)
  * [LinkedIn](https://www.linkedin.com/in/norma-lopez/)

### Frontend Team
* Eric Berglund
  * [GitHub](https://github.com/ericberglund117)
  * [LinkedIn](https://www.linkedin.com/in/eric-berglund117/)
* Hanna Kim
  * [GitHub](https://github.com/hannakim91)
  * [LinkedIn](https://www.linkedin.com/in/kimhanna/)
* Kristi Miller
  * [GitHub](https://github.com/Kristiannmiller)
  * [LinkedIn](https://www.linkedin.com/in/kristiannmiller/)

## Endpoints

### Retrieve all weddings

Example Request: `GET /api/v1/weddings/weddings`

Example Response:
```
[
    {
        "id": 1,
        "name": "Simpsons",
        "email": "simpsons@email.com",
        "date": "06/18/2022",
        "image": "https://images.unsplash.com/reserve/xd45Y326SvKzSR3Nanc8_MRJ_8125-1.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80"
    },
    {
        "id": 2,
        "name": "Smith",
        "email": "smith@email.com",
        "date": "08/03/2022",
        "image": "https://images.unsplash.com/reserve/xd45Y326SvKzSR3Nanc8_MRJ_8125-1.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80"
    },
    {
        "id": 3,
        "name": "Sanchez",
        "email": "sanchez@email.com",
        "date": "04/22/2022",
        "image": "https://images.unsplash.com/reserve/xd45Y326SvKzSR3Nanc8_MRJ_8125-1.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80"
    }
]
```

### Create a wedding

Example Request:
```
POST /api/v1/weddings/create/
Content-Type: application/json
Accept: application/json

{
  "name": "Williams",
  "email": "williams@email.com",
  "date": "06/10/2022",
  "image": "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80"
}
```

Example Response:

```
{
    "id": 4,
    "name": "Williams",
    "email": "williams@email.com",
    "date": "06/10/2022",
    "image": "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80"
}
```
### Create guest

Example Request:
```
POST /api/v1/weddings/guest/create/
Content-Type: application/json
Accept: application/json

{
    "name": "Homer",
    "phoneNumber": "5554127893",
    "wedding": 1
}
```

Example Response:

```
{
    "id": 1,
    "name": "Homer",
    "phoneNumber": "5554127893",
    "wedding": 1
}
```

### Retrieve all guests for specific wedding

Example Request:
```
GET /api/v1/weddings/guests/?wedding=1
```

Example Response:

```
[
    {
        "id": 2,
        "name": "Bart",
        "phoneNumber": "5559631594",
        "wedding": 1
    },
    {
        "id": 1,
        "name": "Homer",
        "phoneNumber": "5554127893",
        "wedding": 1
    }
]
```

### Create a photo

Example Request:
```
POST /api/v1/weddings/photo/create/
Content-Type: application/json
Accept: application/json

{
    "number": 2,
    "description": "Groom alone",
    "guest": [1],
    "weddingId": 1
}
```

Example Response:

```
{
    "id": 1,
    "number": 2,
    "description": "Groom alone",
    "guest": [
        1
    ],
    "weddingId": 1
}
```

### Retrieve all photos for specific wedding

Example Request:
```
GET /api/v1/weddings/photos/?weddingId=1
```

Example Response:

```
[
    {
        "id": 3,
        "number": 6,
        "description": "Groom and son",
        "guest": [
            1,
            2
        ],
        "weddingId": 1
    },
    {
        "id": 2,
        "number": 5,
        "description": "Groom's son",
        "guest": [
            2
        ],
        "weddingId": 1
    },
    {
        "id": 1,
        "number": 2,
        "description": "Groom alone",
        "guest": [
            1
        ],
        "weddingId": 1
    }
]
```

## Future Iterations

  * Consume Twilio API to send SMS notifications to guests to inform them of which photo numbers they are in
  * Allow updating for wedding, photo, and guest
  * Create vendor table which will represent the users/photographers who will sign in to use the app

## Local Development Setup

1. Download Docker desktop
2. Clone down this repository on your local machine
3. Execute the following commands one by one in this order:
  * `docker-compose build`
