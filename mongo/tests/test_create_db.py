class PostgresCreator:

    def create_tables(self, db_connection):
        """

        :return:
        """

        db_cursor = db_connection.cursor()

        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                gamePk int4 NOT NULL,
                gameDate date NOT NULL,
                awayId int2 NOT NULL,
                homeId int2 NOT NULL,
                awayScore int2 NOT NULL,
                homeScore int2 NOT NULL,
                venueId int2 NOT NULL,
                highHitPlayerId int4,
                highHit real,

                CONSTRAINT PK__games PRIMARY KEY (
                    gamePk
                )
            );
        """)
        db_cursor.execute("""
            CREATE INDEX IF NOT EXISTS IX__games__gameDate
                ON games(
                    gameDate
                )
            ;
        """)

        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                teamId int2 NOT NULL,
                teamName varchar(20) NOT NULL,

                CONSTRAINT PK__teams PRIMARY KEY (
                    teamId
                )
            );
        """)
        db_connection.commit()

        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                playerId int4 NOT NULL,
                playerName varchar(20),

                CONSTRAINT PK__players PRIMARY KEY (
                    playerId
                )
            );
        """)

        db_cursor.execute("""
            ALTER TABLE games
                ADD CONSTRAINT FK__games__awayId__teams__teamId
                    FOREIGN KEY (awayId) REFERENCES teams(teamId)
            ;        
        """)
        db_cursor.execute("""
            ALTER TABLE games
                ADD CONSTRAINT FK__games__homeId__teams__teamId
                    FOREIGN KEY (homeId) REFERENCES teams(teamId)
            ;        
        """)
        db_cursor.execute("""
            ALTER TABLE games
                ADD CONSTRAINT FK__games__highHitPlayerId__players__playerId
                    FOREIGN KEY (highHitPlayerId) REFERENCES players(playerId)
            ;        
        """)
        db_connection.commit()
        db_cursor.close()

import psycopg2
creator = PostgresCreator()
creator.create_tables(psycopg2.connect(
    host="chcubs.crtnht6h1zib.us-east-1.rds.amazonaws.com",
    database="ajkasmun",
    user="ajkasmun",
    password="zkcqvnau"
))
