from pytest import CaptureFixture
import pymongo


def test_create_mongo(capsys: CaptureFixture):
    """
    Test the creation of the MongoDB.
    """

    ''''''
    client = pymongo.MongoClient("localhost", port=8081)

    ''''''
