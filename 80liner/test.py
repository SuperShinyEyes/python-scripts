import unittest
import eightyLiner

fileRead = "text"
fileWrite = eightyLiner.getNameForFileWrite(fileRead)
eightyLiner.perform80Liner(fileRead)

class Test80Liner(unittest.TestCase):
    # fr = open(fileRead)
    # fw = open(fileWrite)

    def testIsLengthUnder81(self):
        with open(fileWrite) as fw:
            for l in fw.readlines():
                self.assertTrue(len(l) < 81)

    def testContainsSameContent(self):
        fr = open(fileRead)
        fw = open(fileWrite)
        frStream = fr.read()
        fwStream = fw.read()

        frStreamWithoutNewLines = " ".join(frStream.splitlines())
        fwStreamWithoutNewLines = " ".join(fwStream.splitlines())

        self.assertEqual(fwStreamWithoutNewLines, frStreamWithoutNewLines)

        fr.close()
        fw.close()



if __name__ == '__main__':
    unittest.main()
