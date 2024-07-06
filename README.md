# Star Wars Planets

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

## Setup Instructions
`git clone https://github.com/LucasNoliveira/sw-planets-panel.git`  
`cd sw-planets-panel`

## Start Containers Docker
`docker compose up --build`

## Start a new terminal and execute the following commands
`docker compose run web python manage.py fetch_planets`
