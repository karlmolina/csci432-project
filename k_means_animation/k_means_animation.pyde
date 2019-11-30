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
    centroid_lerp_value = 0.1
    k_means = KMeans(data, k, min_change, centroid_lerp_value)
    k_means.initialize_centroids()
    k_means.assign_data()
            
    
    
def draw():
    background(background_color)
    global started
    global k_means
    
    k_means.show_points()
    k_means.show_centroids()
    fill(0)
    text('k-means  k={}, min_change={}, iteration={}, change={}'.format(k_means.k, k_means.min_change, k_means.iteration, k_means.change), 10, 20)
    
    if not started:
        if frameCount == 100:
            started = True
        return
    
    if not k_means.is_converged():
        if not k_means.moving_centroids:
            k_means.assign_data()
        
            k_means.move_centroids()
            k_means.moving_centroids = True
        else:
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
