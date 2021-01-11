# Index-test
Creates a random SQL database and measures the time it takes to create, index and query the database.

A database of 1,000,000 random "movie" entries is created. Each movie has a name consisting of 10 random 
ascii-letters and a production year from 1900 to 2000. Database is then indexed and queried to find
movies with 1000 random production years. When finished, program prints the time taken for each step.

This was used to measure differences indexing makes to query time or the creation of the database, when indexed
individually.
