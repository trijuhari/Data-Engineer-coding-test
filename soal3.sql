/*postgreSQL*/

/* a. */
SELECT m.*
FROM 
messages AS m
WHERE m.attachments_id in (
	SELECT id
	FROM attachments
	WHERE mime_type = "video/mp4"
)
 

/* b. */

SELECT m.*
FROM 
messages AS m
WHERE  m.attachments_id in
(
select id 
FROM  attachments
WHERE mime_type = "video/mp4"
) AND m.delivered_at >= (NOW() - INTERVAL '3' HOUR)
ORDER BY  m.delivered_at DESC


/* c.*/

 messages.attachments_id   
 The reason is  this columns have high cardinality(), and 
 the other than that indexes can play an important role in query optimization and searching the results speedily from tables.   