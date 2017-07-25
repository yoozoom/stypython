# input a world to upper world and write to a file
def toUpper(s):
    return s.upper();

testStr = raw_input("input a world:");

testStr = toUpper(testStr);

file1 = open("t1.txt", "w");
file1.write(testStr);