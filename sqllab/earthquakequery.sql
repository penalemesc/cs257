--Find all earthquakes that happened in Argentina
SELECT * 
  FROM earthquakes  
  WHERE place LIKE '%Argentina%';

--find the magnitude of any earthquake that happened at an latitude of at least 20
SELECT mag 
  FROM earthquakes e 
  WHERE e.latitude >= 20;

--FInd how many earthquakes there where in the dataset and print the average magnitude
SELECT count(quaketime) AS amountOfEarthquakes, (SELECT AVG(mag) FROM earthquakes) AS averageStrength 
  FROM earthquakes
  GROUP BY (averageStrength);
