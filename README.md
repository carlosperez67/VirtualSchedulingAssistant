# VirtualSchedulingAssistant

** What will this application be capable of?**

### Basic Functionality
- Creating events (set start time and end time) as identified by the user
- Adding events to Google Calendar automatically
- Take in user preferences for automatically scheduling like: 
  - how long of work blocks are preferred
  - check user google calendar to see when they are available
  - take into account blackout hours (aka when the user wants free time)
- Create tasks to be done (with a deadline and estimated hours needed to finish task)


### ML Functionality
- Automatically add work periods corresponding to tasks to Google Calendar
- - Give the user the ability to edit the work period details (time and length) and note each work period (and corresponding details) as vectors
- Use linear regression (or similar ML algorithm) (perhaps NumPy?) to compute dot product and create prediction model
- Keep improving model by using the edits created by the user as training data.
