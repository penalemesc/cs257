--Find all earthquakes that happened between april 6th and may 2nd of any year
SELECT * 
  FROM earthquakes e 
  WHERE e.quaketime 
  BETWEEN '%04-06%' AND '%05-02%';

--find the magnitude of any earthquake that happened at an latitude of at least 20
SELECT mag 
  FROM earthquakes e 
  WHERE e.latitude >= 20;

--FInd how many earthquakes there where in the dataset and print the average magnitude
SELECT count(quaketime), (SELECT AVG(mag) FROM earthquakes) AS averageStrength 
  FROM earthquakes
  GROUP BY (averageStrength);
