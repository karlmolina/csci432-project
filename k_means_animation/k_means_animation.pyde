

from k_means import KMeans

size(600, 600)
pixelDensity(2)
# noFill()
background(0)
stroke(255)
noStroke()
colorMode(HSB)


def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
    
def main():
    data = load_data('../generate_convex_clusters/data/without_noise.csv')
    k_means = KMeans(data, 3, 0.01)
    
    # for x in data:
    #     ellipse(x[0], x[1], 5, 5)
    
    # print(data)
        
    k_means.k_means()
    
    for centroid_index, points in k_means.centroid_assignments.items():
        fill(centroid_index * 100, 255, 255)
        for p in points:
            ellipse(p[0], p[1], 5, 5)
    
    for i, x in enumerate(k_means.centroids):
        fill(i* 100, 255, 255)
        ellipse(x[0], x[1], 30, 30)
    
    print(k_means.centroids)
    
    
main()
