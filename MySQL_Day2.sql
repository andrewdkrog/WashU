use washu_day2;



select * from players_nba;

select * from seasons_stats;

select 
	players_nba.Player as Player, height, weight, college, born, birth_city
from 
	players_nba 
		JOIN 
    seasons_stats ON players_nba.player = seasons_stats.player;
    
    