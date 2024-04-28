     DROP TABLE randomN;
   CREATE TABLE randomN (
          rNum int not null,
		  rName varchar(25) NOT NULL
          );

\copy randomN from 'RandomData.data'