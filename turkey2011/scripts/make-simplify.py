# -*- coding: utf-8 -*-

import pg, private


def process():
	table = 't2011.districts'
	fullGeom = 'full_geom'
	googGeom = 'goog_geom'
	boxGeom = googGeom
	#db.addGoogleGeometry( table, fullGeom, googGeom )
	
	for tolerance in ( 10, 100, 1000, 10000, 100000, ):
		simpleGeom = '%s_%d' %( googGeom, tolerance )
		db.simplifyGeometry( table, googGeom, simpleGeom, tolerance )
		
		#filename = '%s/%s-%s.json' %(
		#	private.GEOJSON_PATH, table, simpleGeom
		#)
		#db.makeGeoJSON( filename, table, boxGeom, simpleGeom, '' )


def main():
	global db
	db = pg.Database( database = 'turkey' )
	process()
	db.connection.close()


if __name__ == "__main__":
	main()
