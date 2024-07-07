# Star Wars Planets

![Darth Vader looking Tatooine sunset](https://64.media.tumblr.com/9dc2e9cc2805063596f0153f3296df4e/tumblr_pp8bteVjQb1w4t7wqo2_540.gifv)

## Overview
This project implements a CRUD (Create, Read, Update, Delete) RESTful API in Django to interact with data retrieved from an external GraphQL endpoint. The goal is to fetch data from the Star Wars API GraphQL endpoint, store it in a local database, and provide endpoints to manage this data.

## Goals

1. Retrieve Data: Fetch data from the Star Wars GraphQL endpoint.
   
2. Database Integration: Store fetched data into the Django database with appropriate models.
   
3. API Endpoints: Implement RESTful endpoints for:
   * Creating new entries
   * Reading existing entries
   * Updating existing entries
   * Deleting entries
   * JWT Authentication: Secure API endpoints with JWT (JSON Web Tokens) authentication.

## Setup Instructions
To run this project locally, follow these steps:
1. Clone the repository:  
`git clone https://github.com/LucasNoliveira/sw-planets-panel.git`  
`cd sw-planets-panel`



### Authentication
Before accessing the API endpoints, you need to generate a JSON Web Token (JWT) for authentication. Here's how you can generate a JWT:

1. **Obtain JWT**: Send a POST request to the `/api/token/` endpoint with your credentials to obtain a JWT.
   
   Example using curl:
   ```bash
   curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}' \
     http://localhost:8000/api/token/
   Replace your_username and your_password with your actual credentials.


