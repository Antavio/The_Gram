# The_Insta_Gram Application

## Author
[Anthony Njuguna Kiarie](https://github.com/Antavio)

## Description
This a django application that mimics the Instagram application. It allows a user to register an account the logs them into the main page from where they can view all the images uploaded by all users. A registered user can upload a photo, comment on a photo, like a photo & follow other users.
They can also click on the profile button from where they can view all their info i.e All their photos, username, edit profile, number of posts,followers and following.

## Behaviour Driven Development(BDD)
| Behaviour                                                | Input                                   | Output                                                                                       |
|----------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------|
| The Page loads the homepage                              | On application load                     | User views the sign up/login page                                                            |
| User is redirected to the index page                     | User successfully registers and logs in | Images of all users are displayed with the profile name,like & comment                       |
| A modal with the image details is displayed              | User clicks on a specific image         | User can view a specific image with all its details                                          |
| User is redirected to the specific profile page          | User clicks on profile icon             | A page with all the details about a specific user is displayed including all their posts     |
| User redirected to a page with a form to enable the post | User clicks on create post button       | A template with a form is rendered. The user fills in all the details including image upload |
| User redirected to the edit profile page|User Clicks on the Edit Profile Button|User fills in the appropriate fields and saves that information and is redirected to the homepage|

### Project Setup instructions
Use the following commands to use this project.
- git clone `https://github.com/Antavio/The_Gram.git`
- install `python 3.6`
- Install [Postgresql](https://www.postgresql.org/download/)
- cd The_Gram
- Navigate to the virtual environment using `source virtual/bin/activate`
- `atom .`  //For those using atom text editor.
- `code .`  //For those using Visual Studio editor.


### Install dependancies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`

### Create the Database
```
psql
CREATE DATABASE <preferred name>;
```
- Run `python3.6 manage.py runserver`
- Access the application on this localhost address `http://127.0.0.1:8000`

### Technologies used
The different technologies that were used to develop this program include:
```
1. Python 3.6 
2. Bootstrap
3. HTML
4. CSS
5. Postgresql
6. MDBootstrap
7. Django Framework
```

### Link to live site
Here is a link to the live site 
### Contact Me
If you have any suggestions, additions or modifications on this project you can reach me via my email: njuguna13@gmail.com

### License  & Copyright information
Copyright (c) 2019 Anthony Njuguna

[MIT License](./LICENSE)