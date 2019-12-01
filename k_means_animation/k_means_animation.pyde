from k_means import KMeans
import random
import time

started = False
background_color = 255
index = 0
wait = 3

def setup():
    # random.seed(1)
    # random.seed(6)
    random.seed(7)
    size(600, 600)
    pixelDensity(2)
    # noFill()
    background(background_color)
    stroke(255)
    noStroke()
    colorMode(HSB)
    rectMode(CENTER)
    # frameRate(1)
    
    # data = load_data('../generate_clusters/data/without_noise.csv')
    global k_means_list
    k = 2
    min_change = 1
    centroid_lerp_value = 0.1
    k_means_list = [
               KMeans('../generate_clusters/data/without_noise.csv', 2, min_change, centroid_lerp_value, 1),
               KMeans('../generate_clusters/data/with_noise.csv', 2, min_change, centroid_lerp_value, 1),
               KMeans('../generate_convex_clusters/data/without_noise.csv', 3, min_change, centroid_lerp_value, 2),
               KMeans('../generate_convex_clusters/data/without_noise.csv', 3, min_change, centroid_lerp_value, 16),
               KMeans('../generate_convex_clusters/data/with_noise.csv', 3, min_change, centroid_lerp_value, 3),
               KMeans('../generate_convex_clusters/data/with_noise.csv', 4, min_change, centroid_lerp_value, 11),
               ]
            
    
    k_means_list[0].initialize()
    
def draw():
    background(background_color)
    global started
    global k_means_list
    global index
    k_means = k_means_list[index]
    
    k_means.show()
    
    # if not started:
    #     if frameCount == 100:
    #         started = True
    #     return
    
    if k_means.run() and index < len(k_means_list) - 1:
        index += 1
        k_means_list[index].initialize()
        time.sleep(wait)
   
    
