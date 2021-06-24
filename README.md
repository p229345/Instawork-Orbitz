# Instawork take home assignment
##Project
Using selenium with any programming language and test framework of your choice, implement
the following:
- Visit www.orbitz.com website.
- Select Flights
- Select “Roundtrip”.
- Enter “Leaving from” : San Francisco and “Going to”: New York.
- Select “Departing” date to be 2 weeks from today and “Returning” date to be 3 weeks
from today.
- Click on Search.
- Assert that the search results are rendered correctly (Ex: Departure/Arrival location and
dates match the input data).
- Select “Nonstop” flights.
- Select the most expensive flight from the list.
- Click on “Select” and then click on “Select this fare” to book.
- Assert the flight details & price on the flight review page

##Instructions on how to run the test
1. Install Python 3.6 or higher on your PC 
2. Install Chrome and Firefox browser on your PC
3. Install Git and Clone repository
4. In project folder, in CMD/Terminal/Bash run "pip install -Ur requirements.txt"
5. In project folder, in CMD/Terminal/Bash run "pytest -v"

##Additional information 
- The test is running in Chrome and Firefox local and remote(Travis CI on Github)
- CI implemented On Github through TravisCI+Selenium Grid+Docker
- Every pull request will trigger Travis CI to run a test with Selenium Grid  in Chrome and Firefox