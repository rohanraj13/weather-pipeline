import sqlite3
import pandas as pd

def update_database(df, connection):
    df.to_sql('Weather', connection, if_exists='append', index=True)
    print("Uploaded to database!")


if __name__ == "__main__":
    import doctest
    doctest.testmod()