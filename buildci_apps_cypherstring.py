# python script to build neo4js Cypher queries used to build Graph database of DB application estate.
# script is run <python buildcountmethods_cypher.py > xxx.out

# import textwrap lib to ensure query string does not split across lines.
import textwrap

# std python routine to open file

f = open('apps_list.txt')
# f1 file handle not used at the moment
f1 = open('apps_out.txt', 'a')

# loop that reads each line in the input file

for line in f:

    # create strip white space from incoming line read in the file, then build neo4j cypher string
    xvalue = line.strip()
    bigstring = "MATCH (ciDataL:ciData {application: "'"'+ xvalue +'"'"}),(AppList:Apps {application: "'"'+ xvalue +'"'"}) CREATE (ciDataL)-[r:CI_OF_ALLAPPS]->(AppList);"

    # print out line, this line is redirected into file at command line
    print(textwrap.fill(bigstring, 250))
# close file handle.
f.close()
