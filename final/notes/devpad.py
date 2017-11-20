

def writeNodesToSQLite(db, datastore, tags):
    cur = db.cursor()
    for node in datastore.getNodesIter():
        if not node["tags"]:
            continue
        point = Point(node["point"])
        cur.execute("INSERT INTO world_point(osm_id,way) VALUES ((?),GeomFromWKB((?),4326))", [node["id"],sqlite.Binary(point.wkb)])
        rowid = cur.lastrowid
        sqlTags = []
        sqlTagKeys = []
        for tag in tags:
            if tag in node["tags"]:
                sqlTags.append(tag)
                sqlTagKeys.append(node["tags"][tag])  
        if len(sqlTagKeys) > 0:
            sql = "UPDATE world_point SET %s WHERE rowid == (?)" % (','.join(['\"%s\" = ?' % (x) for x in sqlTags]))
            sqlTagKeys.append(rowid)
            cur.execute(sql, sqlTagKeys)
    cur.close()



/* daniel code */


-------------------------
sql research
--------------




-------------------
conn = sqlite3.connect('rednews.db')
c = conn.cursor()
sql = "SELECT * FROM stuffToPlot WHERE keyword =? AND source =?"

wordUsed = 'isis'
sourceVariable = 'reddit'

    def readData():
        for row in c.execute(sql, [(wordUsed), (sourceVariable)]):
            print row


-------------------



okay so, tomorrow lets pull some of these values out from the .keys().  titles, author, score.
And then add them as entries into our database file.
Then lets write some simple enquiries so that we can search for this data.