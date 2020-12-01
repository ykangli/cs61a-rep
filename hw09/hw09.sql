CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name AS name, s.size AS size FROM dogs AS d, sizes AS s
  WHERE d.height > s.min AND d.height <= s.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child FROM parents AS p, dogs AS d
    WHERE p.parent = d.name
      ORDER BY d.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
SELECT a.child AS sibling01, b.child AS sibling02, c.height AS sibling01_height, d.height AS sibling02_height 
    FROM parents AS a, parents AS b, dogs AS c, dogs AS d
      WHERE a.child < b.child AND a.parent = b.parent AND a.child = c.name AND b.child = d.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || sibling01 || " plus " || sibling02 || " have the same size: " || size
  FROM siblings, sizes AS s 
    WHERE sibling01_height > s.min AND sibling01_height <= s.max 
    AND sibling02_height <= s.max AND sibling02_height > s.min;

