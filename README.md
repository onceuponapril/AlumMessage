# AlumMessage
## Envrionment
step 1: Create a virtual environment: virtualenv ven. Then install all the required package by `pip install ...`.
step 2: Run migration: `python manage.py migrate`, which will help you build the database. 

## Features
1. On the home page, you can log in if you are a member of admin, otherwise click the 'sigh up' button which will lead you to create the account. It is a default  built-in feature, and you need to follow its requirements i.e. 'Your password can't be entirely numeric.' If it cannot be processed, remember to check if you meet the requirments or not. Alternatively, you can create your account by 'createsuperuser'. 
2. Only the super user can acess the administration site, where you can read all the message in the database.
3. Once log in, the user will be led to the send message page, where you can send message using uniqname.
4. Only the authorized user can check the message, where you can input any uniqname to read the message sent to it. If you did not see any inputbox, just check if you are log in or not.
5.
