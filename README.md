# DjangoHotelBookingApp

This is an online hotel booking web application build with python's Django Framework
*NOTE:* This application is hosted live at 
<a href="http://believeohiozua.pythonanywhere.com" target="_blank" >believeohiozua.pythonanywhere.com</a>
      
 ![alt text](https://raw.githubusercontent.com/believeohiozua/DjangoHotelBookingApp/master/media/flowchart.jpg)

    
## WEB PAGES
    

*Home Page*
This is the very first you see when you lunch the site url.
it contains list of all hotel categories, links to profile page, gallery, 
contact form and a reservation search form which takes you to the hotel list page        
     
*Hotel List Page*                      
The hotel list page, page is reached based on search result
from either the search page or the home pageand it shows
the list of avalible rooms based on the search parameters and
it takes the user to the hotel detail page where payment is made
for the selected room

*Hotel/Room Booking Page*
The room booking page is where the user pays for the seletected
avalible room.
transaction test parameters are :

``` 
card no. :4242 4242 4242 
Date :12/20  (or any date of your choice)
CVC :123 (or any code of your choice)
zip :00000 (or any zip of your choice)
    
```
    if payment is successful, it takes the user to profile page           

*Profile Page*
This page contains the users current hotel bookings informations 
if the check in date is in the future , the status = payment confirmed
if check in  date is today or passed, status = checked in
and if check out date is reached, the status = checked out
The booking and informations are automatically deleted
a day after the checkout date and the booked room 
becomes available again.
The user can update or delete his / her profile.
from the profile page
If there are no current bookings, the user can click on the.
search page botton from the profile to search for available reservations.

*Search Page*
This page contains a form for searching available reservations
and it takes users to the avalible hotel list page 

*Gallary Page*
This page dispalys the hotel media and it takes the user
to the reservation search page
        


       
## Running the Application locally


This application was built in *python 3.6* so be sure you have it installed, up and running
open your terminals 
Create a virtual env ( optional)
Navigate to the app root folder ( where you have the manage.py file)
And run the `pip install -r requirements.txt` file to install the dependencies 
Add a.env file in the Chappsolutions folder 
and add tbe following parameters: 

```
SECRET_KEY=your uniquely generated secret key
EMAIL_HOST_USER=youremail@something.com
EMAIL_HOST_PASSWORD=your_password
STRIPE_PUBLISHABLE_KEY=your stripe publishable key
STRIPE_SECRET_KEY=your stripe secret key
```

With All Set and Done. run the Command
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Open the host in your browser http://127.0.0.1:8000
        

     


