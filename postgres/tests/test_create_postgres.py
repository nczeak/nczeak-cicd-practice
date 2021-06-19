'''import psycopg2
creator = PostgresCreator()
creator.create_tables(psycopg2.connect(
    host="chcubs.crtnht6h1zib.us-east-1.rds.amazonaws.com",
    database="ajkasmun",
    user="ajkasmun",
    password="zkcqvnau"
))'''
from pytest import CaptureFixture


def test_postgres_creation(capsys: CaptureFixture):
    """
    Tests the creation of the Postgres db on the local machine.
    """

    ''''''