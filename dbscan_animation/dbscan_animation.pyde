from dbscan import Dbscan
import time

background_color = 255
index = 0

def setup():
    size(600, 600)
    pixelDensity(2)
    background(background_color)
    stroke(255)
    noStroke()
    colorMode(HSB)

    global dbscan_list
    process_amount = 20
    dbscan_list = [
               Dbscan('../generate_clusters/data/without_noise.csv', 3, 30, process_amount),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 20, process_amount),
               Dbscan('../generate_convex_clusters/data/without_noise.csv', 3, 20, process_amount),
               Dbscan('../generate_convex_clusters/data/with_noise.csv', 4, 18, process_amount),
               ]
               
    
def draw():
    global dbscan_list
    global index
    background(255)
    dbscan = dbscan_list[index]
    dbscan.show_points()
    if dbscan.run() and index < len(dbscan_list) - 1:
        index += 1
        
        
    
    
    
