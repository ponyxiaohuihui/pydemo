import jaydebeapi

url = 'jdbc:hsqldb:file:C:\\codes\\fio\\webapps\\webroot\\WEB-INF\\embed\\finedb\\db'
user = 'sa'
password = ''
# jarFile = [
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\antlr4-runtime-4.5.3.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\swift-jdbc-client.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-annotations-2.9.0.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-core-2.9.8.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-databind-2.9.8.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-datatype-jdk8-2.9.8.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-datatype-jsr310-2.9.8.jar',
#     'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-module-parameter-names-2.9.8.jar']
dirver = 'com.fr.third.org.hsqldb.jdbcDriver'
sqlStr = 'select * from PUBLIC.FINE_SWIFT_SEGMENTS'

conn = jaydebeapi.connect(dirver, url, [user, password], 'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\fine-third-10.0.jar')
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchall()
print(result)
curs.close()
conn.close()
