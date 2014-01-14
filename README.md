MBTiles Multithread Extract
===========================

Current version: 0.1.0
Currently in early alpha, use at your own risk.

An alternative MBTiles extraction utility written in Python which takes advantage of multithreading to extract large MBTiles files quickly.

Usage:
python MBMultithreadExtract.py <input mbtiles file> <output folder>

Requirements:
TBA


Speed Testing
===========================

Test 1:
=======

530.6mb Tileset
5,068,344 Tiles
609,925,821 bytes (20.81 GB on disk)

Multithread Extraction:
Total: 0:23:43.387

MBUtil:
Total: 0:25:29.414


Test 2:
=======

150.8mb Tileset
5,857 tiles
148,359,960 bytes (160.3 MB on disk)

Multithread Extraction: 
Total: 1.883

MBUtil: 
Total: 2.682
