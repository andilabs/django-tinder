djtinder
========

DjangoTinder is app written for fun using Django with power of GeoDjango and PostgreSQL with PostGIS.

It aims to simulate what app like [Tinder](http://en.wikipedia.org/wiki/Tinder_%28application%29) does, that is: finding people meeting nearby, sex, age, orientation, criteria.


### how to run it



    docker-compose up -d
    

### generate random data:
this commands generates given as argument number of random users within Warsaw
see for way of picking randoms the source of: [api/management/commands/generate_random_users.py](api/management/commands/generate_random_users.py)


    docker exec -it web python manage.py generate_random_users 10000
 

### generate 1 non-random user:

this command generates user `andi` with deterministic data, see 
source code of: [api/management/commands/generate_andi_user.py](api/management/commands/generate_andi_user.py)

    docker exec -it web python manage.py generate_andi_user
    


## fetch from API endpoint tinder like proposals:

after calling two commands above; to get proposals matching distance, age, sex, etc. make 
GET call to the endpoint like this:

http://127.0.0.1:8000/api/proposals/andi/52.230/21.002/

The endpoint will return proposal for user `andi`.