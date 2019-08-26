# SparkifyDB

## Summary

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The song data resides in JSON logs on user activity, as well as JSON metadata on the songs in their app.

Sparkify needs a better data model to analyse their data. They need a Postgres database with a focus on . This can be achieved with the STAR schema approach.

The STAR schema approach consists of 1 or more fact tables referencing any number of dimension tables. In this case I modelled the data as follows:

- Fact table: songplays table
- Dimension tables: User table, Song, table, Artist table, Time table.

## List of files

1. *create_tables.py* - script to create sparkify database and tables in the database.
2. *sql_queries.py* - script that contains all sql queries to create tables, insert data and query the database.
3. *test.ipnyb* - notebook file to test if all the tables correctly made.
4. *etl.ipnyb* - notebook file to prototype etl queries.
5. *etl.py* - script to process JSON files and insert data appropriately into database tables.

## ETL process

1. Extract data from songs_data, transform and load into songs and artists tables.
2. Extract data from log_data, transform and load into users and time tables.
3. Compile data from all the tables to create the songplays table.

## Libraries required

- os - traverse file system
- glob - obtain JSON filepaths
- psycopg2 - postgreSQL wrapper
- pandas - load JSON files as dataframe into python

Each of these libraries can be installed using *pip install* e.g. To install psycopg2, do

```console
pip3 install psycopg2
```

## Order of execution

Run files in the following order:

1. *create_tables.py*

    ```python
    python create_tables.py
    ```
    
2. *test.ipnyb* (Run all the cells and check if all tables are appropriately created with correct columns)
3. *etl.py*

    ```python
    python etl.py
    ```
    






