select * from globalfirepower;

ALTER TABLE globalfirepower
ADD COLUMN id INT auto_increment PRIMARY KEY FIRST;

-- Turn off safe updates
SET SQL_SAFE_UPDATES = 0;

DELETE FROM globalfirepower
WHERE ReservePersonnel = 0;

UPDATE globalfirepower
SET FighterAircraft = 1
WHERE FighterAircraft = 0;

UPDATE globalfirepower
SET TotalAircraftStrength = FighterAircraft + AttackAircraft + TransportAircraft + TrainerAircraft;

SELECT AVG(TotalMilitaryPersonnel) as Avg_Personnel,
AVG(TotalAircraftStrength) as Avg_Aircraft,
AVG(TotalHelicopterStrength) as Avg_Helicopter,
AVG(TotalPopulation) as Avg_Populaiton
FROM globalfirepower;

INSERT Into globalfirepower (Country, TotalPopulation)
values("new country", Avg_Population);