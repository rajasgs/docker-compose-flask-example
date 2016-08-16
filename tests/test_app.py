import unittest
from context import *

class TestResources(unittest.TestCase):

    def setUp(self):
#        wget database
        pass

# Tests for Playlists
    def test_Playlists(self):
        foo = Playlists()
        assert foo.get()
        assert isinstance(foo.get(), dict)
#        print "test_Playlist: success"

# Tests for Songs_Of_Artist
    def test_Songs_Of_Artist(self):
        foo = Songs_Of_Artist() 
        assert isinstance(foo.get(1), dict)
#        print "test_Songs_Of_Artist: success" 

# Tests for Show_Artists       
    def test_Show_Artists(self):
        foo = Show_Artists()
        assert isinstance(foo.get(), dict)
#        print "test_Show_Artists : success"

    def tearDown(self):
        pass
#       delete database

if __name__ == '__main__':
    unittest.main()
