size(600, 600)
pixelDensity(2)
# noFill()
background(0)
stroke(255)
noStroke()


def show_data(filename):
    count = 0
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        ellipse(x[0], x[1], 5, 5)
        count += 1
    print('Data count:', count)


# show_data('../generate_convex_clusters/data/with_noise.csv')
# show_data('../generate_convex_clusters/data/without_noise.csv')
# show_data('../generate_clusters/data/with_noise.csv')
show_data('../generate_clusters/data/without_noise.csv')
