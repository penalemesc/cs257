DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime date with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  rms real,
  net text,
  id text, 
  updated time,
  place text,
  quaketype text,
  horError real,
  depthError real,
  magError real
);
