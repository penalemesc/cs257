     DROP TABLE USStatesPop CASCADE;

     DROP TABLE USCitiesTop1k CASCADE;

   CREATE TABLE USStatesPop (
          code char(2) NOT NULL,
          stateName varchar(25) NOT NULL,
          staPop int NOT NULL,
          PRIMARY KEY (code)
          );

   CREATE TABLE USCitiesTop1k (
          city varchar(75) NOT NULL,
          stateName varchar(25) NOT NULL REFERENCES USStatesPop,
          cityPop int NOT NULL,
          lat real NOT NULL,
          lot real NOT NULL,
          PRIMARY KEY (city, stateName)
          );

\copy USStatesPop from 'us-state-pop.csv' DELIMITER ',' CSV
\copy USCitiesTop1k from 'us-cities-top-1k.csv' DELIMITER ',' CSV