# PROYECTO 1 DATA ENGINEERING 
## Data Modeling with Postgres

- In this project, I applied everything I learned during the classes regarding data modeling with postgres and building ETL pipes with python.

- Tables  were created through the execution of constructed scripts, data with python code were inserted in the jupyter notebook and the final construction of these was verified through the same method.

- With the files that are in the data folder (log_data and song_data) I was able to fill the tables: songs, artists, users, time and songsplay.

**- These tables contained the following:**

1. songs: song_id, title, artist_id, year, duration
   It contains the list of songs, where the name appears, the id of the artist who sings the song, in which year it was created and its duration.
   
    ![Image][1]
    ⋮
    [1]: https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/data/songs.png

2. artists: artist_id, name, location, latitude, longitude
   Contains all the artist data, such as name, location, among others.
   
    ![Image][1]
    ⋮
    [2]: https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/data/artists.png

3. users: user_id, first_name, last_name, gender, level
   Contains user records of songs.
   
    ![Image][1]
    ⋮
    [3]: https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/data/users.png

4. time: start_time, hour, day, week, month, year, weekday
   Contains timestamps of songs.

    ![Image][1]
    ⋮
    [4]: https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/data/time.png
   
5. songsplay: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
   Table that is made up of what is important, such as the song id, the artist id, the time, the user agent, among others. The important thing about        this   table is that the songplay_id is built by default taking a serial format.
   
    ![Image][1]
    ⋮
    [5]: https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/data/songplays.png

**- SCRIPTS EXECUTION**

_THE_ _SCRIPTS_ _WERE_ _RUN_ _THROUGH_ _THE_ _CONSOLE_, _WITH_ _THE_ _COMMAND_ 
1. !python create_tables.py
- This will create the postgres database and all relevant tables

2. !python etl.py
- This will start the etl process and fill all the tables with data