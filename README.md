# Creating Virtual Environment
## ● What is Virtual Environment ?<br/>
![This is an image](https://github.com/enessoztrk/Creating_Virtual_Environment/blob/main/img.jpg)<br/><br/>
## Introduction<br/>
• A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.<br/><br/>
## Why do we need a virtual environment?<br/>
• Imagine a scenario where you are working on two web based python projects and one of them uses a Django 1.9 and the other uses Django 1.10 and so on. In such situations virtual environment can be really useful to maintain dependencies of both the projects.<br/><br/>
## When and where to use a virtual environment?<br/>
• By default, every project on your system will use these same directories to store and retrieve site packages (third party libraries). How does this matter? Now, in the above example of two projects, you have two versions of Django. This is a real problem for Python since it can’t differentiate between versions in the “site-packages” directory. So both v1.9 and v1.10 would reside in the same directory with the same name. This is where virtual environments come into play. To solve this problem, we just need to create two separate virtual environments for both the projects.The great thing about this is that there are no limits to the number of environments you can have since they’re just directories containing a few scripts. Virtual Environment should be used whenever you work on any Python based project. It is generally good to have one new virtual environment for every Python based project you work on. So the dependencies of every project are isolated from the system and each other.<br/><br/>
## How does a virtual environment work?<br/>
• We use a module named virtualenv which is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.<br/><br/>
