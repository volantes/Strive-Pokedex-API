# Strive Backend Coding Challenge - Pokedex!
Wecome to the code repository for Strive's backend coding challenge in creating a pokedex api. 

# To Get Started
Follow the steps below to get started.

### Environment Setup
* Make sure you have the latest version of python installed (To download: https://www.python.org/downloads/)
    * To test your python version type `py --version` (for Windows) in the command shell. You should see `Python 3.10.7`
* Clone this git repo to your computer at your desired filesystem location
* At the root of git repo, creat your virtual environment, activate it, and install the required packages
  * (For Windows) run the following in the command shell:
    * To create your virtual environment: `py -m venv bcc-env`
    * To activate your virtual environment: `bcc-env\Scripts\activate.bat`. You should now see `(bcc-env)` before your command shell location.
      * For example `(bcc-env) c:\project-locations\this-cloned-repo\>`
    * To install the required packages: `py -m pip install -r requirements.txt`
* Test if everything is working so far:
  * (For Windows) run in the command shell: `py -m django --version`. You should get `4.1.1` in response. 

### Initial Project Setup
Now that we have the environement set up, lets set up the project.
* To test if the project starts, run the following in the command shell (for Windows):
  *  To start the test server for the project: `py manage.py runserver`
  *  To test that the server started (after a few moments), to to http://127.0.0.1:8000 in the browser.
     *  You should see a welcome message: `Welcome to the Strive Backend Coding Challenge index page. Visit /api/ for more fun.`
* Populating Data: If all is working so far, continue by running the following in the command shell (for Windows):
  * To set up the project's database structure: `py manage.py migrate`
  * To populate the database with data run: 
    * `py manage.py loaddata pokemon_types.json`
    * `py manage.py loaddata pokemon.json`
* Lets test the api. Run `py manage.py runserver` and visit this url in a browser: http://127.0.0.1:8000/api/pokemon/. You should see a list of Pokemon. 

### Bonus: Admin Interface
Lets view the user interface for editing our projects entities. 

* Creating an admin user: Run the following in the command shell (for Windows):
  * To create your super user: `py manage.py createsuperuser`
  * Follow the prompts and enter a username, email address, and password. 
    * For example: 
      * Username: `admin`
      * Email address: `test@email.com`
      * Password: `abc456@#$`
* Admin Interface
  * Lets visit the admin interface at http://127.0.0.1:8000/admin/. 
  * Login with the credentials you just used to setup the admin user. 
  * You should now be able to see and manipulate the data for both system users and pokemon data. Neat-o!
* Taking this futher:
  * This opens the door to easily add authentication on top of our api layer. For easy testing, we currently have no authentication restrictions for interacting with the API. That being said, I can implemented authentication for the api if you'd like to see that. 

# API Usage Examples
The following shows a few ways to use the API

* **Query a pokemon by id:** 
  * http://127.0.0.1:8000/api/pokemon/1/
  * http://127.0.0.1:8000/api/pokemon/?id=1

* **Retrieve a list of Pokemon with the following filter options:**
  * Name
    * http://127.0.0.1:8000/api/pokemon/?name=Pikachu
  * Type
    * http://127.0.0.1:8000/api/pokemon/?types=1
  * Caught or not
    * http://127.0.0.1:8000/api/pokemon/?is_caught=false

* **Retrieve a list of pokemon types:**
  * http://127.0.0.1:8000/api/types/

* **Update if a pokemon is caught:**
  * Is caught:
    * curl "http://127.0.0.1:8000/api/pokemon/1/" -X PUT -H "Content-Type: application/json" -d '{"id": 1, "name": "Bulbasaur", "is_caught": true}'
  * Is not caught:
    * curl "http://127.0.0.1:8000/api/pokemon/1/" -X PUT -H "Content-Type: application/json" -d '{"id": 1, "name": "Bulbasaur", "is_caught": false}'

* **Different Language / internationalization supported responses:**
  * Response in english:
    * curl "http://127.0.0.1:8000/api/pokemon/1/" -H "Accept-Language: en-es" -H "Accept: application/xml"
  * Response in spanish:
    * curl "http://127.0.0.1:8000/api/pokemon/1/" -H "Accept-Language: es-es" -H "Accept: application/xml"
  * Response in german:
    * curl "http://127.0.0.1:8000/api/pokemon/1/" -H "Accept-Language: de-es" -H "Accept: application/xml"

