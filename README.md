# Star Wars Planets

![Darth Vader looking Tatooine sunset](https://64.media.tumblr.com/9dc2e9cc2805063596f0153f3296df4e/tumblr_pp8bteVjQb1w4t7wqo2_540.gifv)

## Summary
- [Overview](#overview)
- [Goals](#goals)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [License](#license)

## Overview <a name="overview"></a>
This project implements a CRUD (Create, Read, Update, Delete) RESTful API in Django to interact with data retrieved from an external GraphQL endpoint. The goal is to fetch data from the Star Wars API GraphQL endpoint, store it in a local database, and provide endpoints to manage this data. The project uses Docker for development, JWT for authentication, and Django's testing framework.

## Goals <a name="goals"></a>

1. Retrieve Data: Fetch data from the Star Wars GraphQL endpoint.
   
2. Database Integration: Store fetched data into the Django database with appropriate models.
   
3. API Endpoints: Implement RESTful endpoints for:
   * Creating new entries
   * Reading existing entries
   * Updating existing entries
   * Deleting entries
   * JWT Authentication: Secure API endpoints with JWT (JSON Web Tokens) authentication.

## Technologies Used <a name="technologies-used"></a>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)


## Requirements <a name="requirements"></a>
* Docker and Docker Compose
* Python 3.8+
* Django 3.2+
* PostgreSQL

## Setup Instructions <a name="setup-instructions"></a>
To run this project locally, follow these steps:
1. Clone the repository:  
```
git clone https://github.com/LucasNoliveira/sw-planets-api.git  
cd sw-planets-api
```

2. Create and configure environment variables:  
```
cp .env.example .env
 # Update the .env file with your configurations
```

3. Build and run the Docker containers:  
```
docker compose up --build
```
4. Populate the PostgreSQL Database:
```
docker compose run web python manage.py fetch_planets 
```

## Running the Project <a name="running-the-project"></a>
Once the Docker containers are up and running, the Django server will be accessible at http://localhost:8000.

#### Authentication
To use the API, you need to obtain a JWT token. Register a new user and log in to get the token.

1. Register a new user:
```
POST /api/register/
{
    "username": "yourusername",
    "password": "yourpassword"
}
```
2. Log in to get the token:
```
POST /api/token/
{
    "username": "yourusername",
    "password": "yourpassword"
}
```
3. Use the token in the Authorization header for subsequent requests:
```
Authorization: Bearer <your_token>
```

## API Endpoints <a name="api-endpoints"></a>

### CRUD Operations:
1. Create a new planet:

```
   POST /api/planets/
{
    "name": "Tatooine",
    "population": "200000",
    "terrains": ["desert"],
    "climates": ["arid"]
}
```
2. Retrieve all planets:
```
GET /api/planets/
```

3. Retrieve a specific planet:
```
GET /api/planets/{id}/
```

4. Update a planet:

```
   PUT /api/planets/{id}/
{
    "name": "Tatooine",
    "population": "200000",
    "terrains": ["desert"],
    "climates": ["arid"]
}
```
5. Delete a planet:
```
   DELETE /api/planets/{id}/
```

## Running Tests <a name="running-tests"></a>
```
docker-compose exec web python manage.py test
```

## Deployment <a name="deployment"></a>
This project is deployed on an AWS EC2 instance. You can access the live deployment of this project at Star Wars Planets API through the following address: http://3.130.205.160 .

## License <a name="license"></a>
This project is licensed under the MIT License. See the LICENSE file for details.

Made with love by Lucas Oliveira ❤️  

![Darth Vader looking Tatooine sunset](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzI5ZGZzZzczbGQwbGphaWk2YW80Z2M5Z3JsNmdlNG8zb3lxeG9nNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0K4k1O7RJSghST3a/giphy.webp)

