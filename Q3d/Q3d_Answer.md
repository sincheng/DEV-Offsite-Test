
# Q3d - Product KPI setting

## 1. Key Questions regarding the performance of the application

From data analytics perspective, I have designed three questions to analyze user behavior, user satisfaction and revenue.

i. Session Time in each page <br>
ii. No. of crush or error in each page <br>
iii. User Purchase Report

## 2. Tracking Plan

### i. Session Time

#### * Why
    - Understanding the time user spent in each page
    - Detect fruad users
    - Improve the efficency of the flow

#### * Field
     - User_id
     - Session_id
     - Page
     - Time

#### * Location
     - Each steps in ticket module

### ii. No. of crash or error 

 #### * Why
    - Crash or error is the most important issue in event ticketing application
    - Understand how and when app crash
    - Improve user satisfaction
    - Improve application performance

#### * Field
    - User_id
    - Session_id
    - Crash or error type
    - Crash or error page
    - Platform
    - App Version
    - Crash Time

#### * Location
     - Retrieve from Server log

### iii. User Purchase Report

#### * Why
    - Revenue are from transaction fee of purchase
    - Category User type depends on purchase frequency
        - Type 1: Registered but no purchase
        - Type 2: Registered and purchase only once in a given period
        - Type 3: Purchased more than 1 time
    - Customized marketing plan for different user type
        - Type 1: Analyze crash report and session time report
        - Type 2: Send out promotion or win-back customer email campign
        - Type 3: Provide update events or recommendations on events

#### * Field
    - User_id 
    - Session_id
    - Event_id
    - Price
    - Payment Method

#### * Location
    - Server Payment Record

## 3.  Data Visualization

### * Tools
    - Tableau Public

### *  Dataset
    -Created three datasets for dashboard visualization
       * user_session_time
            - Record user time spent in every pages   
       * app_crash_report
            - Record every crashes by login session
       * user_purchase_report
            - Record every purchases by login session

### * Dashboard Overview

The KPI dashboard consists of 5 parts.

Public Link
https://public.tableau.com/profile/cathy.cheng8698#!/vizhome/q3d_dashboard_0/KPIDashboard

![Dashboard Overview](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/kpi_dashboard2.png)

#### * Crash Rate
    - Visualization Type: Donut pie chart with crash rate percentage
    - Calculated by count of session_id in app crash report / count of all session id in user_session_time
    - Can quickly alert if the crash rate exceed a given value

![Crash Rate](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/1_crash_rate3.png)
 * Example
  - No. of session_id in app crash report = 11
  - No. of session_id in user session time = 17
  - crash rate = 11/37 = 64.71%

####  * Session Time Overview
    - Visualization Type: Bar Chart 
    - Show average session time user spent on each page
    - Understand which page user spent most of the time
    - The label above the bar show no. of time access the page

![Session Time Overview](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/2_session_time_overview.png)
* Example
    - Users average spent 150 seconds on page 5 which is perform payment
    - Users spent less time on page 1 and 6 (event summary and purchase confirmation)
    - Most of the user access page 3(seat selection)

#### * Crash Overview
    - Visualization Type: Text Table
    - Display percentage of crash occured in each platform and app version

![Crash Overview](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/3_crash_overview.png)
* Example
   - Over 30% of crash from Android with App version 1.3

#### * Event Overview
    - Visualization Type: Text Table
    - Display no.of purchase, no.of user and total price transaction in each event
    - Sort descending by no.of of purchase
    - Identify user favorite events
![Event Overview](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/4_event_overview.png)
* Example
    - ABC Concert has greatest no. of purchase, no.of user purchase and highest price

#### * Crash Count in 7 days

    - Visualization Type: Line 
    - Show no.of crash in last 7days
    - Easy to track app performance
![Crash Count](https://github.com/sincheng/DEV-Offsite-Test/blob/master/Q3d/img/5_crash_count.png)
* Example
    - The no.of crash has greatly reduced from 1 Jan 2018
