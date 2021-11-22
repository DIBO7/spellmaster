# SPELLMASTER PROJECT

The spellmaster project is an open source python project (built with python and django) to create a bot on the web that reads through documents and webpages to find (and ofcourse, report) __mispelled words__. It will also have the capability to rewrite (in a downloadable copy) the document (or webpage) with the right spelling. This Project is hosted [here on heroku](https://spellmaster.herokuapp.com). It currently finds spelling errors in `*.txt` files for now and development is still in progress. 

**NOTE: The 'main' branch automatically deploys to heroku (and heroku collects static i.e runs `python manage.py collectstatic` on every deploy)** So working and testing within a new/another branch is adviced.


## Languages
1. Python
2. Javascript
3. HTML5
4. CSS3

## FRAMEWORKS AND LIBRARIES (for local development)
* Django
* Python Decouple 
	* _(A `sample_env.env` file has been included in the project's root to help developers who aren't familiar with python decouple. All you have to do to get this project to run locally is create a similar file named `.env` with contents similar to what is in `sample_env.env`)_
* 

__NOTE: This project requires no database. So ignore all django's message regarding database migrations__

### Files to work with includes:
* HTML files
* .txt files
* .doc(x) files
* .md files (parhaps)
* .pdf files (yes, thats right!)


---
Here is the mockup of the main page (open to changes though!)

![SpellMaster Prototyped Main Page](/screen.png)