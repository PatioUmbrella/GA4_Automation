Project Goal:
This project aims to further automate the google analytics web and mobile analytics reporting process. 
This will help to save time and provide easier, more consistent analytics reporting for desktop and 
mobile websites.

Overview of the process:
  Gather necessary information:
    Report type
    Google property_id
    api credentials json file
    start date = 20xx-xx-xx
    end date = 20xx-xx-xx
  Set up a virtual environment
  Run Python GUI code
  Fill in info and press buttons
  Wait for csv file to output
  Run Python Graph code
  Validate with csv file (only on the 1st implementation)
  Analyze the results!

About:
By taking advantage of the Google Data API, we can pull data programmatically from the api. 
On top of this we can use PyQt5 to input those credentials, thereby skipping two processes: 
1 - making the graphs in the Google Analytics environment and 2 - manually adjusting our code. 
Simply put, the major benefit is that we can automate the creation of multiple reports by 
pressing just a few buttons. 

In addition, this in theory could all be run in the background or ideally on a timer (weekly, monthly), 
and afterwards the program would forward the complete and branded graphs to the analyst and optionally 
the project stakeholders as well.
