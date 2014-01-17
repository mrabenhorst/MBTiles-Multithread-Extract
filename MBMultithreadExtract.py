import sys, os, shutil, glob, sqlite3
from PIL import Image
import datetime
from multiprocessing import Pool

inputMBTilesFolderPath = None
outputTilesFolderPath = None
allImageData = None

def extractDataToTile(i):
	global outputTilesFolderPath
	global inputMBTilesFolderPath
	global allImageData
	
	tmpImage = open(outputTilesFolderPath+'/'+str(allImageData[i][0])+'/'+str(allImageData[i][1])+'/'+str((2 ** allImageData[i][0])-allImageData[i][2]-1)+'.png','w+')
	tmpImage.write(allImageData[i][5])
	tmpImage.close()
		
	return None

def main(argv):
	global inputMBTilesFolderPath
	global outputTilesFolderPath
	global allImageData
		
	if( len(sys.argv) < 3 or len(sys.argv) > 4 ):
		print "MBMultithreadExtract.py <input mbtiles> <output folder> [<# processes>]"
		sys.exit()
	
	curpath = os.path.abspath(os.curdir)
	
	inputMBTilesFolderPath = str(sys.argv[1])
	outputTilesFolderPath = curpath+'/'+str(sys.argv[2])
	numProcesses = -1
	if len(sys.argv) == 4:
		numProcesses = int(sys.argv[3])
	if numProcesses < 1:
		numProcesses = 20
		
	print "numProcesses: " + str(numProcesses)
	
	# Open SQLite connectioin
	sqliteCon = None
	try:
		sqliteCon = sqlite3.connect(inputMBTilesFolderPath)
		cur = sqliteCon.cursor()
		
		# Obtain Folder Structure
		startTime = datetime.datetime.now() # * SQL DB Profiling
		folderStructureData = None
		cur.execute('SELECT DISTINCT zoom_level, tile_column FROM map')
		folderStructureData = cur.fetchall()
		endTime = datetime.datetime.now() # * SQL DB Profiling
		# * SQL DB Profiling
		timeForOp = endTime - startTime
		print "Folder Structure Extract Op Time: " + str(timeForOp)
		
		# Create Folder Structure
		startTime = datetime.datetime.now() # * SQL DB Profiling
		for folderData in folderStructureData:
			try:
				os.makedirs(outputTilesFolderPath+"/"+str(folderData[0])+"/"+str(folderData[1]))
			except:
				None
		endTime = datetime.datetime.now() # * SQL DB Profiling
		# * SQL DB Profiling
		timeForOp = endTime - startTime
		print "Folder Structure Creation Op Time: " + str(timeForOp)
		
		# Get All Images
		startTime = datetime.datetime.now() # * SQL DB Profiling
		cur.execute('SELECT * FROM map JOIN images ON map.tile_id=images.tile_id')
		allImageData = cur.fetchall()
		endTime = datetime.datetime.now() # * SQL DB Profiling
		
		# * SQL DB Profiling
		timeForOp = endTime - startTime
		print "Data Query Extract Op Time: " + str(timeForOp)
		
		pool = Pool(processes=numProcesses) #
		startTime = datetime.datetime.now() # * SQL DB Profiling
		result = pool.apply_async(extractDataToTile,range(0,len(allImageData)))
		pool.map(extractDataToTile,range(0,len(allImageData)))
		endTime = datetime.datetime.now() # * SQL DB Profiling
		
		# * SQL DB Profiling
		timeForOp = endTime - startTime
		print "Image write Op Time: " + str(timeForOp)
		
	except sqlite3.Error, e:
	    print "Error %s:" % e.args[0]
	    sys.exit(1)
		
	finally:
	    if sqliteCon:
	        sqliteCon.close() 




if __name__ == "__main__":
	main(sys.argv[1:])