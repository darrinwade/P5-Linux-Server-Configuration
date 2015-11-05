# Wade's Category results application (Modified to run on a new server installation configured by me)

 version 1.0 11/05/2015


- This application is the same used in the "P3 Item Catalog" project but with as needed modifications,
(described below), to run on a PostgreSQL database and a Ubuntu Linux server built from scratch
and served up via an Apache webserver.

- The IP address is 52.89.49.213 and the port the application is running on is 2200

- The application itself can be reached at either of the following two URLs:
    http://ec2-52-89-49-213.us.west-2.compute.amazonaws.com
                  or
    http://52.89.49.213

- Software and/or applications installed and/or configured in order to have the Catalog appliction
  run include:

  (1) Apache
  (2) Git
  (3) PostgreSQL database
  (4) Finger
  (5) mod-wsgi
  (6) Psycopg2
  (7) SqlAlchemy
  (8) ufw

  See the "Modifications Needed" section for configuration changes made to have the application run.

- Third-party resources used to complete the project:

  (1) Stackoverflow.com
  (2) Youtube
  (3) www.digitalocean.com
  (4) developers.google.com
  (5) www.ubuntu.com

- Contents of my ~/.ssh/udacity_key.rsa file

MIIEowIBAAKCAQEAuzDNN1wXpqXecyLoISI+uNTnZckW3JedP9L6Kqo3QNtR2Yv5
8qcCSQe3ARno3yJ60z1/YNN1i87vZrBKm4INhhbIAiGk0bV/EoU8t5WUMsjfljeG
DDJhzrEvrOsgeU5vhptuaVBYN739Bd0DFs7AKEBb3BFucxNzVOXkJEAebkv7Q9G0
wNfZcpemtA2hyM9KZhTNGSyqqqRtYFK299cMp9nmJvaXZFgCQOqg7ea+Q/bag5Ky
Me2No3GhOatdigyKoGazaXUVhEOJiLxLVGk5lv5BjHEHle9JHtafeNJ71vbWdbcD
ZGMtu5QYSplfK+lmrdw5pVdsJJMCxYsHEncjLwIDAQABAoIBAFGfkQx/sqxvDVXF
NdUk2pa7936xta9QyTfIZl9uQ5ObTtB+sem2G0/+9jSbuKh7n3U3DrEI4+unu0pa
ut2eUwlSK7qKMxVif9tyj6w5pBqU7rHQ2jm9SlrXdkN/b3SV2Bmo8vcnGqCLzqXc
3nj2hGHI1oVacH/rTlIJwHZyIxLSfHJIx0U0DQuNAOePpj07b3Bx1dChhPefBjuw
4sSDZFnaZTCbC4OxCk7aTKbipVHZlYAc6E5pT4Lc9yi1qQmGG2K23XEuFn9QNmyR
k4ujZVPot6H1LMtHUoTQzGcd6aovtTh3526YzNde0QlkNu0xuUmps5Hz7TOyl9ai
P3DaI8ECgYEA+Kw2PEhz7j2mKpa15AW+LAn0WtuxoGHHv3zQfLUrLNRGtZeQI0l8
FbHBL3E9onEo13yJaJPELyFO1jpyp9VY2nFXPy8Kg9ewLd6LcWg37iDL7M1qx+PT
1ehrnZAMLjLvqGiIMhX6WBj2yMw/VzybI7s8BeXQ8Vzp95NUtrw7wE8CgYEAwLTR
crOJ7SnMfftZpGb4UO4nG96VNfkGsdwZYpGp8MhBBjJSZRoqESC1y/RnI2XPfun0
QkBTy9C9hQt8q1uA14xJYrkuBemutcA+/IIuXaBV+Jh1+nZYfk+EJHGwkpCMqcW4
xo1JEIsMY6OI/wtm5HPgJOFrPHXx6hEFZGJv1yECgYEA07z3FU9v/yzZHyxixjyp
mCAFw5OLZI+9oGvrrjQpBivd5WOfZJx+no5Te00F+Ro3d3xgF/6yLptC4KC13fiI
hr+5VWB9qJNwPS5gN3lRHl8opIKoaHmyd1JGx8vOw0u1ywTu6w7Rsk/XWlSnnmVJ
iBw2WKM9zTabNaZqnIocqnsCgYBJRzjyDfWf2qopKeAvlPxOAhGbFmvU50o1bgW1
JsDhj7SyP4Z3bZibhL28vcZOfpOFpj88xitXMJwwsGqK2rPGw1DQmqw2kWLfOCh7
aqFo9uRaMNeEE2aZOXF9TkIfqZnjoQ0fa3BiOw3OAczBdzt8GdgdDh7yEcOZBznu
r0PqIQKBgALGauOH5GZ9HgR0kuVcjIC8hnz9CpmysbMFwAESPgtZy/7Nr7/12Dhp
PUbHa68BasvN+n+4qplayu03TvUKY8V87vZvmR8MOk+t1Z19UJyDXjcs9ZvnDocs
er1sqo2zZELUh12/xlWNr4KQAAFfjp+bMTRutYtxBB2dAuw+Gv+L

####################  Modifications Needed  ####################

Server Side Configuration Changes Made
---------------------------------------
(01) Root access login disabled once a new user was created. This change was made
     in /etc/ssh/sshd_config
(02) grader user created with associated file added to the /etc/sudoers.d structure
     to enable "sudo" access for the user
(03) As needed package upgrades applied, (See list above for specifics)
(04) sudo dpkg-reconfigure tzdata run to change the serve time format to UTC
(05) Default ssh port changed from 22 to 220 in /etc/ssh/sshd_config
(06) ufw setup and enabled allowing incoming access only on ports 80, 123, and 2200
(07) Apache installed and setup to inable serving of application
(08) /etc/host and /etc/hostname modifications made to enable serving of the application


Application Structure (Modifications denoted as **New)
---------------------------------------

The checked in Category.zip file contains the following files:

(01) application.py - Python file containing the bulk of the processing code for the category
             application project.  Basic "CRUD" database processing, functionality needed for
             routing to the various UI components, as well as that needed to authenticate
             a user is stored here.

      **New  Change to specify the absolute path location of the
             client_secrets.json file within the application structure.

             Change made to have the appliction run on a PostgreSql database


(02) application_dbsetup.py - Python file containing the configuration and setup code needed to
             define and build out the category database.  Execution of this script results in
             the creation of three tables, (Owner, Category, and Item), defined in an sqlite
             database for this application.

      **New  Change made to have the appliction run on a PostgreSql database

(03) application_LoadAndSetupCode.py - Python file used in the mid to late stateges of the
             category application's development to ensure the correct setup of the database
             tables, for the insertion/removal of data for the appropriate level of testing,
             and other misc uses.  Depending on the final state of testing, the contents of
             the script may or may not have "relevent" value.

(04) client_secrets.json - Credentials file downloaded from Google's developer sight used in
             the authentication and authorization portion of the application.

(05) static\main.css - Cascading style sheet for the application.

(06) templates\categoriesAll.html - UI component used for displaying the category list information.
             It is the "home page" of the application, handles the primary routing for adding,
             changing, and deleting categories, shows both individual and "group" JSON category
             information, and handles the routing for category's items.

(07) templates\categoryCreate.html - UI component used in the creation of a category element

(08) templates\categoryDelete.html - UI component used in the deletion of a category element

(09) templates\categoryEdit.html - UI component used in the editing of a category element

(10) templates\categoryItemAll.html - UI component used for the display of all item entries for a
             given category element.  It also handles the primary routing for adding, changing,
             and deleting category items in addition to showing both individual and "group"
             JSON category item information.

(11) templates\categoryItemAllLastCreated.html - UI component used for the display the last 
             20 catogory items regardles of the individual category it belongs to.

(12) templates\categoryItemCreate.html - UI component used in the creation of a category item element

(13) templates\categoryItemDelete.html - UI component used in the deletion of a category item element

(14) templates\categoryItemEdit.html - UI component used in the editing of a category item element

(15) templates\categoryItemView.html - UI component used in the viewing of a category item element

(16) templates\categoryView.html - UI component used in the viewing of a category element

(17) templates\login.html - UI component used for processing user logins

      **New  New client_secrets.json information provided

_____________________________________________________________________________________________


In order test/run the category application, perform the following steps:

(01) Using a standard browser, you should be able to access the application "home page"
     by typing http://ec2-52-89-49-213.us.west-2.compute.amazonaws.com <Enter> on the URL.
     
 From there you can begin viewing any existing category and associated item entries or you can
 look to add your own category entries once you've logged into the application.  Authourization
 is granted through Google so a valid Google account id is required.



Copyright 2015 Wade Corporation.  All rights reserved.
Wade's Tournament Results Application and its use are subject to a license agreement and are
also subject to copyright, trademark, patent and/or other laws.
