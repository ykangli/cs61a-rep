.read data.sql


CREATE TABLE average_prices AS
  SELECT category, SUM(MSRP) / COUNT(category) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store AS store, item AS item, price AS price FROM inventory GROUP BY item HAVING MIN(price);


CREATE TABLE shopping_list AS
  SELECT name, store FROM lowest_prices AS l, products AS p 
    WHERE l.item = p.name GROUP BY category HAVING MIN(MSRP / rating);

CREATE TABLE total_bandwidth AS
  SELECT SUM(a.MBs) FROM stores AS a, shopping_list AS b 
    WHERE a.store = b.store;

