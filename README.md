### CommandLine Xplore Event Website

#### What this is about?
- This website was built for a Tech Event at NIT Jalandhar.
- It is website which can be used to host any question-answer type event. 
- You just need to edit the questions in a file and the information about the registered users and their answers will be recorded as files in a folder.
- So it can be used by anyone with or witout technical skills.

#### Dependency:
- Django 1.8
- python 2.7

#### Setup:
- Create a file named "ques" in the "data" folder. It will be containing all the questions. Each question must be written in 1 line i.e. line 1 contains first question.
- Create a folder named "submit" in the "data" folder. The information of registered users and the answers submitted by them will be recorded in the form of files in this folder.

- Open project directory in the terminal.
- Run the below written commands:
  ````
  pip install -r requirements.txt 
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ````
- Now the Server starts running.
- The website will be live at 127.0.0.1:8000/home/1/
