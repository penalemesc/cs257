DROP VIEW if EXISTS furthestWest;

DROP VIEW if EXISTS furthestEast;

DROP VIEW if EXISTS furthestNorth;

DROP VIEW if EXISTS furthestSouth;

   CREATE VIEW furthestEast AS (
   SELECT min(lot) AS FEast
     FROM USCitiesTop1k
);

   CREATE VIEW furthestNorth AS (
   SELECT max(lat) AS FNorth
     FROM USCitiesTop1k
);

   CREATE VIEW furthestSouth AS (
   SELECT min(lat) AS FSouth
     FROM USCitiesTop1k
);
   CREATE VIEW furthestWest AS (
   SELECT max(lot) AS FWest
     FROM USCitiesTop1k
);

   SELECT UCT.city AS furthestWest
     FROM USCitiesTop1k UCT,
          furthestWest FW
    WHERE UCT.lot = Fw.Fwest;

   SELECT UCT.city AS furthestEast
     FROM USCitiesTop1k UCT,
          furthestEast FE
    WHERE UCT.lot = FE.FEast;

	SELECT UCT.city AS furthestNorth
     FROM USCitiesTop1k UCT,
          furthestNorth FN
    WHERE UCT.lat = FN.FNorth;

	SELECT UCT.city AS furthestSouth
     FROM USCitiesTop1k UCT,
          furthestSouth FS
    WHERE UCT.lat = FS.FSouth;