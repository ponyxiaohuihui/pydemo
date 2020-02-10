import jaydebeapi

url = 'jdbc:swift:remote://192.168.5.66:7000/cube'
user = 'a'
password = 'a'
jarFile = [
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\antlr4-runtime-4.5.3.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\netty-all-4.1.17.Final.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\swift-jdbc-client.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-annotations-2.9.0.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-core-2.9.8.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-databind-2.9.8.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-datatype-jdk8-2.9.8.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-datatype-jsr310-2.9.8.jar',
    'C:\\tools\\FineReport10\\webapps\\webroot\\WEB-INF\\lib\\jackson-module-parameter-names-2.9.8.jar']
dirver = 'com.fr.swift.jdbc.Driver'
sqlStr = 'select * from `template_info`'

conn = jaydebeapi.connect(dirver, url, [user, password], jarFile)
curs = conn.cursor()
curs.execute(sqlStr)
result = curs.fetchone()
print(result)
curs.close()
conn.close()
