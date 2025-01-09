_Copy this recipe template to design and create a database table from a specification._
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)


```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
```

```
Nouns:

album, title, release year, artist, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year , artist_id|
|
Name of the table (always plural): `albums`

Column names: `title`, `release_year` , `artist_id`, `id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```

# {{ record store }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
  title: string
  release_year: number (string)
  artist_id: number (string)

GET /albums
```


## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# Post /albums
#  title: 'DooMore'
#   release_year: 1999
#   artist_id: 1
#Expected Response (200 OK)

# GET /albums
# Expected Response (200 OK)

```
Album(1,'Doolittle', 1989, 1)
Album(2,'DooMore', 1999, 1)
```

# Post /albums
#Expected Response (400 Bad Request)

You need to submit a title, release_year, and artist_id

# GET /albums
# Expected Response (200 O)

```
Album(1,'Doolittle', 1989, 1)
```

