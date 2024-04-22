--1 Determine if Northfield is present in the database. If it is, print its location (Latitude and Longitude). If it is not, print an appropriate message for the user.
select lot, lat from USCitiesTop1k where city = 'N%';
--2 Print out the name of the city with the largest population.
     WITH maxCityPop AS (
             SELECT max(cityPop) AS MaxCP
               FROM USCitiesTop1k
          )
   SELECT city AS BiggestCity
     FROM USCitiesTop1k,
          maxCityPop
    WHERE cityPop = MaxCP;
--3 Print out the name of the city in Minnesota with the smallest population.
     WITH minCityPop AS (
             SELECT min(cityPop) AS MinCP
               FROM USCitiesTop1k
              WHERE stateName = 'Minnesota'
          )
   SELECT city AS SmallestCityInMinnesota
     FROM USCitiesTop1k,
          minCityPop
    WHERE cityPop = MinCP;
--4 Print out the names of the cities that is furthest North, furthest East, furthest South, and furthest West

--5 Have the user enter a State from the keyboard. Print the Total population of all the cities in that state. The user should be able to enter either an abbreviation or the full name of the sate. If the user enters an abbreviation, then you should look up the abbreviation in the second table to learn the full name of the state.