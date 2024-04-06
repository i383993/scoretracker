INSERT INTO games (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('PBKS', '177', 6, 'DC', '174', 9)

ALTER TABLE games ADD COLUMN home_wickets Number;
ALTER TABLE games ADD COLUMN visitor_wickets DATE;

-- Create a new table with the modified column
CREATE TABLE ipl (
    home_team TEXT,
    home_score TEXT,
    home_wickets INTEGER,
    visitor_team TEXT,
    visitor_score TEXT,
    visitor_wickets INTEGER
);

INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('PBKS', '177', 6, 'DC', '174', 9);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('KKR', '208', 7, 'SRH', '204', 7);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('RR', '193', 4, 'LSG', '173', 6);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('GT', '168', 6, 'MI', '162', 9);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('RCB', '178', 6, 'PBKS', '176', 6);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('CSK', '206', 6, 'GT', '143', 8);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('SRH', '277', 3, 'MI', '246', 5);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('RR', '185', 5, 'DC', '173', 5);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('RCB', '182', 6, 'KKR', '186',3);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('LSG', '199', 8, 'PBKS', '178',5);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('GT', '168', 3, 'SRH', '162',8);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('DC', '191', 5, 'CSK', '171',6);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('MI', '125', 9, 'RR', '127', 4);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('RCB', '153', 10, 'LSG', '181', 5);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('DC', '166', 10, 'KKR', '272', 7);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('GT', '199', 4, 'PBKS', '200', 7);
INSERT INTO ipl (home_team, home_score, home_wickets, visitor_team, visitor_score, visitor_wickets) VALUES ('SRH', '166', 4, 'CSK', '165', 5);