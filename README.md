# SPELLMASTER PROJECT

The spell master project is an open source project (built with python and django) to create a bot that quickly read through documents and webpages to find (and ofcourse, report) __mispelled words__. It will also have the capability to quicly rewrite (in a downloadable copy) the document (or webpage) with the right spelling. This Project is hosted [here on heroku](https://spellmaster.herokuapp.com). It is also currently under development. 

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

**NOTE: The 'main' branch automatically deploys to heroku. So developing within a new/another branch is adviced.**

---
Here is the mockup of the main page (open to changes though!)

![SpellMaster Prototyped Main Page](/screen.png)