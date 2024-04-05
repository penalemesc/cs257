DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone PRIMARY KEY,
  latitude real PRIMARY KEY,
  longitude real PRIMARY KEY,
  quakedepth real,
  mag real,
  magType text,
  rms real,
  net text,
  id text, 
  updated time with time zone,
  place text,
  quaketype text,
  horError real,
  depthError real,
  magError real
);