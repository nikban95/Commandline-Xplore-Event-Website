# commandLine-Xplore-Event-Website

This website was used to host commandline xplore event. It is website which can be used to host any question-answer type event. 
You just need to edit the questions in a file and the information about the registered users and their answers will be recorded as files in a folder.
So it can be used by some less technical person also.
It is developed in Django using HTML and CSS.

Dependency:

1. Django 1.8
2. python 2.7

Pre Steps: 

1. Create a file named "ques" on the Desktop. It will be containing all the questions. Each question must be written in 1 line i.e. line 1 contains first question.
2. Create a folder named "submit" on the Desktop. The information of registered users and the answers submitted by them will be recorded in the form of files in this folder.

Run Server:

1. Open project directory in the terminal.
2. Run the below written commands:
  1. python manage.py makemigrations
  2. python manage.py migrate
  3. python manage.py runserver
3. Now the Server starts running.
4. The website will be live at 127.0.0.1:8000/home/1/
