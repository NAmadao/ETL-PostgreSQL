import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
from sql_queries import *

def main():
    # Connect to database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")

    # Read contents of each table into dataframe
    songplays = sqlio.read_sql_query(songplays_table_select, conn)
    users = sqlio.read_sql_query(users_table_select, conn)
    songs = sqlio.read_sql_query(songs_table_select, conn)
    artists = sqlio.read_sql_query(artists_table_select, conn)
    time = sqlio.read_sql_query(time_table_select, conn)

    # Save each dataframe as csv file
    songplays.to_csv('songplays.csv', index=False)
    users.to_csv('users.csv', index=False)
    songs.to_csv('songs.csv', index=False)
    artists.to_csv('artists.csv', index=False)
    time.to_csv('time.csv', index=False)

    # Close connection to database
    conn.close()


if __name__ == "__main__":
    main()