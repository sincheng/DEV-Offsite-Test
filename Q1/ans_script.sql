SELECT COUNT(*)  FROM
	(SELECT a.uid, COUNT(b.event_name) AS event_count
		FROM piwik_track a ,piwik_track b
		WHERE a.event_name='FIRST_INSTALL'
		AND a.time::date = date '2017-04-01'
		AND a.uid = b.uid
		AND b.time between '2017-04-02' AND '2017-04-08'
		GROUP BY a.uid
		HAVING COUNT(b.event_name)>=1) as t1;
