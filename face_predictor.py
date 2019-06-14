from PIL import Image
import requests
import urllib.request
import numpy as np
import json
import cv2
import sys

#access_token = 'a18df9e34b12ad1f'

def face_predictor(access_token):
	#api-endpoint
	URL = 'https://hackattic.com/challenges/basic_face_detection/problem'
	
	PARAMS = {'access_token': access_token}

	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS) 
	  
	# extracting data in json format 
	data = r.json()

	# Retrieve image url
	image_url = data['image_url']

	# Load the cascade
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	# Read the input image
	resp = urllib.request.urlopen(image_url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# Convert into grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Slice the image into 64 pieces
	im = gray

	M = im.shape[0]//8
	N = im.shape[1]//8

	tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

	# Create placeholder for face_titles

	face_tiles = []

	# Loop through all 64 tiles and pick up tiles with detected face and insert into face_tiles
	for i in range(len(tiles)):
		tile = tiles[i]
		
		# Calculate Tile Number
		x = i//8
		y = i%8
		
		faces = face_cascade.detectMultiScale(tile, 1.1, 5)
		
		# Face deteced
		if(len(faces) > 0):
			face_tiles.append([x,y])
	
	# Convert to JSON format and return
	print(json.dumps(face_tiles))
	
if __name__ == "__main__":
    access_token = sys.argv[1]
    face_predictor(access_token)
