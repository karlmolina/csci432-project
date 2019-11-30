from dbscan import Dbscan
import time

background_color = 255

def setup():
    # random.seed(1)
    # random.seed(6)
    # random.seed(6)
    size(600, 600)
    pixelDensity(2)
    # noFill()
    background(background_color)
    stroke(255)
    noStroke()
    colorMode(HSB)
    
    data = load_data('../generate_convex_clusters/data/with_noise.csv')
    global dbscan
    # dbscan = Dbscan(data, 5, 20)
    min_pts = 1
    eps = 22
    process_amount = 10
    dbscan = Dbscan(data, min_pts, eps, process_amount)
    print(len(data))
    print(len(dbscan.labels))
    
def draw():
    
    
    # dbscan.show_points()
    # noFill()
    # stroke(0)
    # ellipse(mouseX, mouseY, dbscan.eps *2, dbscan.eps *2)
    # noStroke()
    
    global dbscan
    background(255)
    dbscan.show_points()
    dbscan.run()
        
        
    
    
    
def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
