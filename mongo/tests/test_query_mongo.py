from pytest import CaptureFixture
from pymongo import MongoClient


def test_home_run_query(capsys: CaptureFixture):
    """
    Test the home run query required in the project.
    """

    ''''''
    client = MongoClient()

    # "gameData.liveData.plays.allPlays