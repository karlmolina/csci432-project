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
    rectMode(CENTER)
    randomSeed(3)
    
    colors = {i: random(0, 255) for i in range(100)}

    global dbscan_list
    process_amount = 1
    dbscan_list = [
               Dbscan('../generate_clusters/data/without_noise.csv', 3, 30, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 1, 20, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 20, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 10, 20, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 1, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 5, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 15, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 20, process_amount, colors),
               Dbscan('../generate_clusters/data/with_noise.csv', 4, 50, process_amount, colors),
               Dbscan('../generate_convex_clusters/data/without_noise.csv', 3, 20, process_amount, colors),
               Dbscan('../generate_convex_clusters/data/with_noise.csv', 4, 18, process_amount, colors),
               ]
               
    
def draw():
    global dbscan_list
    global index
    background(255)
    dbscan = dbscan_list[index]
    dbscan.show()
    if dbscan.run() and index < len(dbscan_list) - 1:
        index += 1
        
        
    
    
    
