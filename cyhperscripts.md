# file contains Cypher query strings for NEO4J community addition
# neo4j graph Cypher query language

# load all ci data from csv file

LOAD CSV WITH HEADERS FROM "file:///tplus_min.csv" AS row
CREATE (:ciData { narid: row.narid, application: row.application, level: row.level, category: row.category,
method1: row.method1, method2: row.method2, country: row.country, finalactiontype: row.finalactiontype,
finaltargettype: row.finaltargettype, citype: row.citype, os: row.os, osversion: row.osversion
})

# load all apps list from csv file

LOAD CSV WITH HEADERS FROM "file:///apps1.csv" AS row
CREATE (:Apps { narid: row.narid, application: row.application, level: row.level})

# load all apps transform/migration records from csv

LOAD CSV WITH HEADERS FROM "file:///ap_methods.csv" AS row
CREATE (:Methods { method1: row.method1, method2: row.method2})

# cypher match queries

MATCH (ci.App), (apps.Applications) WHERE ci.application = apps.application RETURN ci, apps

MATCH (ci:App) WHERE ci.application = "3D Cash-3D Cash" AND ci.level = "App" RETURN ci.application, ci.os, ci.osversion, ci.finalactiontype, ci.finaltargettype

MATCH (ci:App) WHERE ci.level = "CI" RETURN ci.application, ci.os, ci.osversion, ci.category, ci.finalactiontype, ci.finaltargettype

MATCH (ci:App), (apps:Applications) WHERE ci.application = "3D Cash-3D Cash" AND ci.level = "CI" CREATE (ci)-[r: CIPARTOFAPP]->(apps) RETURN ci.application, ci.os, ci.osversion, ci.category, ci.finalactiontype, ci.finaltargettype

# Build Relationships for CI's to Apps.

MATCH (ciData:ciData), (App:Applications) WHERE ciData.application = "3D Cash-3D Cash" AND App.application = "3D Cash-3D Cash" CREATE (ciData)-[r:CI_OF_APP1]->(App)

MATCH (ciData:ciData), (App:Apps) WHERE ciData.application = "3D Gateway" AND App.application = "3D Gateway" CREATE (ciData)-[r:CI_OF_APP2]->(App)

MATCH (ciDataL:ciData {application: "3D Static"}), (AppList:Apps {application: "3D Static"}) CREATE (ciDataL)-[r:CI_OF_APP5]->(AppList)

MATCH (ciDataL:ciData), (AppList:Apps) CREATE (ciDataL)-[r:CI_OF_APPS ]->(AppList)

# delete relationship 'CI_OF_APP_MAX' leave nodes alone.

MATCH (n)-[r:CI_OF_APP_MAX]->() DELETE r

# create a unique constraint

CREATE CONSTRAINT ON (n:Methods) ASSERT n.method1 IS UNIQUE

# match count

MATCH (n:ciData {method2: "TI-C 1.1 License Cluster" }) RETURN COUNT(n)

# match based on WHERE clause and pull all relationships out in and outbound

MATCH (a:Apps {application: 'AcS-Accounting Sub Ledger-Global'})-[r*1..3]-(b) RETURN r, a, b

MATCH p=(c:ciData {os: "SLES 11 SP3"} )-[r:CI_OF_ALLAPPS]->() RETURN p LIMIT 200

# optional match

MATCH (a:Apps), (n:ciData {os: "SLES 11 SP3", finalactiontype: "MIGRATE"}) OPTIONAL MATCH (n)-[r:CI_OF_ALLAPPS]-(a) ORDER BY n.finaltargettype RETURN a.application, n.os, n.finalactiontype, n.finaltargettype

# match and create relationship to transform node

MATCH (c:ciData), (t:Transform) WHERE c.method1 = "Transform" AND t.metod = "Transform" CREATE (c)-[:APP_TRANSFORM_METHOD1]->(t)

# cypher query maps base ci to transform target method condiational on target method1 and method2

MATCH (c:ciData), (m:Methods) WHERE c.method2 = "Sybase CMO" AND c.method1 = "Transform" AND m.method2 = "Sybase CMO" AND m.method1 = "Transform" CREATE (c)-[:TRANSFORM_SYBASE_CMO]->(m)


# hold

CREATE (c)-[:TRANSFORM_TIC_COMPUTEVIRTUALV1]->(m)

MATCH (c:ciData), (m:Methods) WHERE c.method2 = "TI-C 1.0 Compute Virtual v.1" AND c.method1 = "Transform" AND m.method2 = "TI-C 1.0 Compute Virtual v.1" RETURN c.application, c.method1, c.method2, m.method2


MATCH (m:Methods), (n:ciData {os: "SLES 11 SP3"}) WHERE m.method1 = "MIGRATE" AND n.method1 = "MIGRATE"  OPTIONAL MATCH (n)-[r*1..3]-(m) RETURN m,n,r LIMIT 50

MATCH (m:Methods)-[r*1..2]-(n:ciData) WHERE n.os = "SLES 11 SP3" RETURN m, n, r

MATCH (m:Methods)-[r*1..2]-(n:ciData) WHERE n.os = "SLES 11 SP3" RETURN m, r, n


# powershell cmd

cat C:\python27\test.txt | cmd /k 'cypher-shell.bat -u neo4j -p pen.see.hen-919 --format plain'
