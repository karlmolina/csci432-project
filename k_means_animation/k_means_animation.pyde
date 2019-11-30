from k_means import KMeans
import random
import time

started = False
background_color = 255

def setup():
    # random.seed(1)
    # random.seed(6)
    random.seed(6)
    size(600, 600)
    pixelDensity(2)
    # noFill()
    background(background_color)
    stroke(255)
    noStroke()
    colorMode(HSB)
    # frameRate(1)
    
    data = load_data('../generate_clusters/data/without_noise.csv')
    global k_means
    k = 2
    min_change = 1
    centroid_lerp_value = 0.01
    k_means = KMeans(data, k, min_change, centroid_lerp_value)
    k_means.initialize_centroids()
    k_means.assign_data()
            
    k_means.show_points()
    k_means.show_centroids()
    
def draw():
    global started
    if not started:
        time.sleep(1)
        started = True
        return
    
    global k_means
    if not k_means.is_converged():
        if not k_means.moving_centroids:
            background(background_color)
            k_means.assign_data()
            
            k_means.show_points()
            k_means.show_centroids()
        
            k_means.move_centroids()
            k_means.moving_centroids = True
        else:
            background(background_color)
            k_means.show_points()
            k_means.show_centroids()
            k_means.update_centroids()
    # else:
    #     exit()
    
def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
