#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def divideLineIntoLinesGenerator(line):
    # First split liens by spaces
    lineSplitedBySpace = line.split(" ")
    # Concatenate words with space until it's 80
    lineUnderLength81 = ""
    for l in lineSplitedBySpace:
        if len(lineUnderLength81) == 0:
            lineUnderLength81 = l
        # The sum has to be less than 79 because it will add " " and "\n"
        elif len(lineUnderLength81) + len(l) < 79:
            lineUnderLength81 += " " + l
        else:
            yield lineUnderLength81 + "\n"
            lineUnderLength81 = l
    yield lineUnderLength81


def getNameForFileWrite(fileRead):
    fileReadSplitted = fileRead.split(".")
    if len(fileReadSplitted) == 2:
        return fileReadSplitted[0] + "-80ed." + fileReadSplitted[-1]
    else:
        return fileRead + "-80ed"

def fileReadGenerator(fileRead):
    with open(fileRead) as f:
        for l in f.readlines():
            yield l

def writeLineToFile(f, line):
    if len(line) <= 80:
        f.write(line)
    else:
        dividedLinesAsIterator = divideLineIntoLinesGenerator(line)
        while True:
            nextValue = next(dividedLinesAsIterator, None)
            if nextValue == None:
                break
            else:
                f.write(nextValue)


def perform80Liner(fileRead):
    fileWrite = getNameForFileWrite(fileRead)

    # with open(fileRead) as f:
    #     lines = f.readlines()
    linesIterator = fileReadGenerator(fileRead)

    with open(fileWrite, 'w') as f:
        while True:
            line = next(linesIterator, None)
            if line == None:
                # You've read all the lines in the file!
                break
            else:
                writeLineToFile(f, line)

if __name__ == "__main__":
    perform80Liner("ignored/text")
