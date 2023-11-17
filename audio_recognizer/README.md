audio_recognizer
==========


AudioRecognizer can memorize audio by listening to it once and fingerprinting it. Then by playing a song and recording microphone input or reading from disk, AudioRecognizer attempts to match the audio against the fingerprints held in the database, returning the song being played. 

Note: for voice recognition, *AudioRecognizer is not the right tool!* AudioRecognizer excels at recognition of exact signals with reasonable amounts of noise.
 
# build and then run our containers
```
$ docker-compose build
$ docker-compose up -d
```
# get a shell inside the container
```
$ docker-compose run python /bin/bash
Starting AudioRecognizer_db_1 ... done
root@f9ea95ce5cea:/code# python example_docker_postgres.py 
Fingerprinting channel 1/2 for test/woodward_43s.wav
Fingerprinting channel 1/2 for test/sean_secs.wav
```

```
# connect to the database and poke around
root@f9ea95ce5cea:/code# psql -h db -U postgres AudioRecognizer
Password for user postgres:  # type "password", as specified in the docker-compose.yml !
psql (11.7 (Debian 11.7-0+deb10u1), server 10.7)
Type "help" for help.

AudioRecognizer=# \dt
            List of relations
 Schema |     Name     | Type  |  Owner   
--------+--------------+-------+----------
 public | fingerprints | table | postgres
 public | songs        | table | postgres
(2 rows)

AudioRecognizer=# select * from fingerprints limit 5;
          hash          | song_id | offset |        date_created        |       date_modified        
------------------------+---------+--------+----------------------------+----------------------------
 \x71ffcb900d06fe642a18 |       1 |    137 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \xf731d792977330e6cc9f |       1 |    148 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x71ff24aaeeb55d7b60c4 |       1 |    146 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x29349c79b317d45a45a8 |       1 |    101 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x5a052144e67d2248ccf4 |       1 |    123 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
(10 rows)

# then to shut it all down...
$ docker-compose down
``` 
