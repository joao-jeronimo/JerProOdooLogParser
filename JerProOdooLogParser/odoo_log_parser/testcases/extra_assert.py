# -*- coding: utf-8 -*-

class ExtraAssert:
    def assertLength(self, collection, thelen, msg=None):
        self.assertEqual( len(collection), thelen, msg=(msg or "Length of this collection is not %d: %s"%(
            thelen, repr(collection), ) ) )
