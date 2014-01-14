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
530.6mb Tileset
5,068,344 Tiles
609,925,821 bytes (20.81 GB on disk)

Multithread Extraction:
Folder Structure Extract Op Time: 0:00:19.879711
Folder Structure Creation Op Time: 0:00:00.505282
Data Query Extract Op Time: 0:00:36.107347
Image write Op Time: 0:22:46.895491
Total: 0:23:43.387831

MBUtil:
