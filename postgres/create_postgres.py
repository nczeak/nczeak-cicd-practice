class PostgresCreator:

    def create_tables(self, db_connection):
        """

        :return:
        """

        db_cursor = db_connection.cursor()
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

    def _create_games_table(self, db_connection):
        """

        """

        ''''''
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                gamePk INT4 NOT NULL,
                gameDate DATE NOT NULL,
                awayId INT2 NOT NULL,
                homeId INT2 NOT NULL,
                awayScore INT2 NOT NULL,
                homeScore INT2 NOT NULL,
                venueId INT2 NOT NULL,
                highHitPlayerId INT4,
                highHit REAL,

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

    def _create_teams_table(self, db_connection):
        """

        """

        ''''''
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                teamId INT2 NOT NULL,
                teamName VARCHAR(20) NOT NULL,

                CONSTRAINT PK__teams PRIMARY KEY (
                    teamId
                )
            );
        """)

        ''''''
        db_cursor.execute("""
            CREATE INDEX IF NOT EXISTS IX__teams__teamName
                ON teams(
                    teamName
                )
            ;
        """)

        ''''''
        db_connection.commit()
        db_cursor.close()

    def _create_players_table(self, db_connection):
        """

        """

        ''''''
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                playerId INT4 NOT NULL,
                playerName VARCHAR(20),

                CONSTRAINT PK__players PRIMARY KEY (
                    playerId
                )
            );
        """)

        ''''''
        db_connection.commit()
        db_cursor.close()

    def _create_venues_table(self, db_connection):
        """
        Create the venues table.
        """

    def create_foreign_keys(self, db_connection):
        """
        Creates the foreign key restraints in the database.
        """

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