
# Offsite Test Q1 - SQL

## 1. Tools Used

* Postgre Version 2.1.3

## 2. Environment Setup

* Run db_test.sql in command line <br>
    1. Create new DB db_test
    2. Create new table piwik_track
    3. Insert sample data for testing

psql postgres -f db_test.sql

## 3. Create the SQL script

* Approach</br>
    1. The first step is to get those users who installed the app (with FIRST_INSTALL event) on 2017-04-01, and join this table with itself
    2.	Then, count each user who selected in step 1 has at least 1 event between 2017-04-02 and 2017-04-08
    3.	Count the no.of user satisfy the condition in step 2.


SELECT COUNT(*)  FROM
    (SELECT a.uid, COUNT(b.event_name) AS event_count
        FROM piwik_track a ,piwik_track b
        WHERE a.event_name='FIRST_INSTALL'
        AND a.time::date = date '2017-04-01'
        AND a.uid = b.uid
        AND b.time between '2017-04-02' AND '2017-04-08'
        GROUP BY a.uid
        HAVING COUNT(b.event_name)>=1) as t1;

## 4. Testing

* Run ans_script.sql in command line

psql db_test -f ans_script.sql

* Test Cases

No | Description | Expected | Result  
---|---------------------------------------|---
1 | All users install the app on 2017-04-01 and use app at least one between 2017-04-02 and 2017-04-08 (F75DA5D1)| Y | Y 
2 | User does not install the app on 2017-04-01 but have event between 2017-04-02 and 2017-04-08 (F75DA5D6) | N | N
3 | User install the app on 2017-04-01 but does not have any events between 2017-04-02 and 2017-04-08 (F75DA5D4)| N | N

* Sample Data

INSERT INTO piwik_track (time , uid, event_name) VALUES
    ('2017-04-01 10:00:00','F75DA5D1','FIRST_INSTALL'),
    ('2017-04-05 11:11:11','F75DA5D1','EVENT1'),
    ('2017-04-05 11:15:11','F75DA5D1','EVENT2'),
    ('2017-04-01 10:00:00','F75DA5D2','FIRST_INSTALL'),
    ('2017-04-05 11:50:11','F75DA5D2','EVENT1'),
    ('2017-04-05 12:50:11','F75DA5D2','EVENT2'),
    ('2017-04-01 10:00:00','F75DA5D3','FIRST_INSTALL'),
    ('2017-04-06 11:40:11','F75DA5D3','EVENT1'),
    ('2017-04-01 10:00:00','F75DA5D4','FIRST_INSTALL'),
    ('2017-04-10 11:40:11','F75DA5D4','EVENT1'),
    ('2017-04-01 10:00:00','F75DA5D5','FIRST_INSTALL'),
    ('2017-04-02 11:00:10','F75DA5D6','FIRST_INSTALL'),
    ('2017-04-05 11:40:11','F75DA5D6','EVENT1');

* Result

MacBook-Pro:Q1 sincheng$ psql db_test -f ans_script.sql
   
---
 3
(1 row)

* Users satisified conditions
    * F75DA5D1
    * F75DA5D2
    * F75DA5D3


```python

```
