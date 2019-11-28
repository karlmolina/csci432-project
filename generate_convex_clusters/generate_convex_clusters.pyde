size(600, 600)
pixelDensity(2)
# noFill()
background(0)
stroke(255)
noStroke()

noise_amount = 100
gaussian = False

def generate_convex_clusters(filename):
    points = []
    def generate_cluster(center, amount, radius):
        for i in range(amount):
            r = PVector.random2D()
            
            if gaussian:
                while True:
                    m = randomGaussian() * radius
                    if abs(m) < radius * 2:
                        break
            else:
                m = random(2) * radius

            r.setMag(m)
            r.add(center)
            ellipse(r.x, r.y, 5, 5)
            points.append([r.x, r.y])

    generate_cluster(PVector(200, 180), 500, 50)
    generate_cluster(PVector(400, 400), 700, 70)
    generate_cluster(PVector(150, 350), 200, 30)
    
    for i in range(noise_amount):
        x = random(0, width)
        y = random(0, height)
        ellipse(x, y, 5, 5)
        points.append([x, y])

    points = (','.join((str(int(x)) for x in p)) for p in points)

    saveStrings(filename, points)


generate_convex_clusters('data/with_noise.csv')
