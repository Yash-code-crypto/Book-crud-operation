Project Name: Book Management System using CRUD operations.

Project Prerequisites:

HTML5
CSS3
Bootstrap
Django
Javascript
Python
MySql Database 

Project Features:

For admin
Admin can add new books
View the whole list of books and delete any book
Admin can update the information of existing book

For Other Users
Can view the whole list of books 
Can read the all information of that book.


Project File Structure:

1) Models.py

Genre model:
It storing the categorys of books.

Language model:
It storing the languages of books. 

Book model:
It saves all the data of each book added to the system.

2) Urls.py

 It's where you define the mapping between URLs and views. 
 A mapping is a tuple in URL patterns like − from django. conf. urls import patterns, include, url from django.

3) Views.py:

1) signup_user()->Function based view

New User can register through it.
template_name='library/login.html'

2) signin()->Function based view

User can logged in into dashboard.
template_name='library/register.html

3)  HomeView()
template_name='library/main.html'

4) BookView()
tempalte_name='library/main.html'
As we have saved all the details of the book inside the book model, then from the book model we fetch all the data of the books and display it in the form of a table

5) BookCreate()
After the admin login, the admin can add new books or delete a book. Admin just have to give the details of the book in a form and add that book.

6) BookDetail()
template_name='library/book.html'
After login,user can see the books detail that added by admin.

7) BookUpdate()
template_name='library/book_list.html'
On clicking on the update button on the book page, admin can update some of the details of book.

8) BookDelete()
template_name='library/book_list.html'

On clicking on the delete button on the book page, admin can delete that particular book.


Connection of database with MySql:

Write a code in settings.py

DATABASES = {
     'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'bookman',  
        'USER':'root',  
        'PASSWORD':'Yash@123',  
        'OPTIONS': {
          'autocommit': True,
        },  
    }  
   
}


to connect with mysql server.



Summary
With this project in Django, we have successfully developed an Books Management Project. We have used front-end (html5, css3, bootstrap) to design the pages and also back-end databases MySql for storing and fetching data. 
We Use Python,Django to built a backend part.

