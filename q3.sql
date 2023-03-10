SELECT o.owner_id, o.owner_name, COUNT(DISTINCT(cam.category_id))
FROM owner o 
INNER JOIN article a
on a.owner_id = o.owner_id
INNER JOIN category_article_mapping cam
on a.article_id = cam.article_id
GROUP BY o.owner_id
ORDER BY 3 DESC