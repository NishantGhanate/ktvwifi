## Ktv Website 


### Things to work on

- [ ] Website
    - [x] Home
    - [x] Pricing
    - [x] Contactus
    - [x] Faq
    - [x] User login / Signup
- [ ] Admin dashboard
    - [x] Customers 
    - [ ] Recharges
    - [x] Complaints 
    - [x] Contacs Email shoot
    - [x] Internet Plans CRUD
    - [x] FAQ 
- [x] User dashboard
    - [x] Home view Rechagers and Complaints Count 
    - [] Recharges
    - [x] Complaints
- [ ] Gpay UPI Payment gateway
    - [ ] Setup merchant account gpay India
    - [ ] Roller coster
    - [ ] Demo test


----
### Demo hosted :-

| Website       | URL                  |
| ------------- | ------------------------------ |
| `Heroku`      | https://ktvwifi.herokuapp.com/ |
| `Pythonanywhere`   | https://nishantghanate.pythonanywhere.com/ |

<br/>

### Run this Django app on local server?

Create an empty folder :
```sh
git clone https://github.com/NishantGhanate/ktvwifi.git.
```

In Cli : 1.Create virtual env , 2. Install requirements 
```sh
 virtualenv venv

 pip install -r requirements.txt
```

### Generate Django secret key :

> from django.core.management.utils import get_random_secret_key
> get_random_secret_key()

>'[GENERATED KEY]'

<br/>

### Env file
Simply create a .env text file on your repository’s root directory in the form & paste secertkey :

```sh
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SECRET_KEY=SECRETKEY
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
DATABASE_URL=
```

### Run :
> python manage.py runserver


&nbsp;

&nbsp;

### Easy guide to host on python anywhere
> https://tutorial.djangogirls.org/en/deploy/