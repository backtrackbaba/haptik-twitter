# Haptik - Twitter

## Problem Statement:
Twitter is a micro blogging platform where users post “tweets” which are ristricted to 140
characters. In this question we want you to build twitter as a platform. Below are the
functionalities of twitter that we want to build out

- A user should be able to sign up / login
- Users should be able to follow each other
- User should be able to tweet about anything they like
- When a user comes on their homepage, they should see all the tweets of people they
are following sorted by latest tweet on top

## Features:

- Users can sign up and login to the platform and logout
- A logged in user can see a list of all users on the platform and follow or unfollow anybody
- A logged in user can view the profile page of any user and glance over the User's tweets without needing to follow them
- Following/Unfollowing of users implemented via Ajax calls
- Tweets are limited to 140 characters
- Profile pic is shown as per the profile set for the entered email ID on Gravatar
- Once the user logs in, they are taken to the feed page which is the equivalent of Twitter's home page
- Tweets from all the following users as well as user's own tweets are shown in reverse chronological order of the time of posting the Tweet


## Tech Stack

- Python
- Flask
- PostgreSQL
- Redis
- SQLAlchemy
- Bootstrap
- jQuery

## Design Decisions


### Technology / Web Framework

If the requirement is not yet stable, I would ideally start of with a Monolithic approach keeping in hindsight the possibility of a rewrite in the future.

The reason to go with Monolith would also depend of the team, timeline and resources available, but yeah, instead of over-engineering right from the start I might choose a Monolithic approach possible with Django.

For microservices, I would go with Flask as the de-facto choice but also evaluate FastAPI, a up and coming alternative to Flask with similar interface.


### Database

Usually, for most of the problem statements requiring RDBMS, I prefer PSQL over MySQL mainly due to the flexibility of PSQL with a wide variety of data types and the ability to add custom data types.

However, In this problem statement, it is inherently clear that a service like Twitter would be more read intensive than write intensive. MySQL is better than PSQL in read-heavy use cases. Upto some extent, personally, I feel the difference between the two could be improved with strategic caching of resources 

Both offer good support for scalability, high availability as per our configuration

A lot of social networking sites user Graph Databases like Neo4j or RedisGraph which I would explore to see the feasibility to have in our application.


### Caching

For now, I have chosen Redis. It gives consistent, blazing fast performance under almost all circumstances. I would mainly implement it as a read through cache. As the users grow, Redis could scale well and could work as a cluster as well.


### Deployment

I usually go with a combination of Gunicorn with Nginx which performs well. Twisted could also be explored as an alternate to Gunicorn.

### Possible Bottleneck

A point of failure that I see for now is the Database. Careful considerations would have to be taken to ensure the queries are efficient, entities are properly indexed and caches are maintained well.
Depending on the use case, Python, the language selected could itself become a bottleneck due to it's supposed inability to handle the needs of real-time applications unlike Node or Go.


## Local Setup

### Create a Virtual Environment using the following command:
`virtualenv -p python3 path/to/env/haptik`

## Clone this repo
`git clone https://github.com/backtrackbaba/haptik-twitter`
then `cd` into the project

### Source the env and install dependencies
`source path/to/env/haptik/bin/activate`
`pip install -r requirements.txt`

### Create .env file using the sample.env

