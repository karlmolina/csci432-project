size(600, 600)
# pixelDensity(2)
# noFill()
background(0)
stroke(255)
noStroke()

radius = 150
offset_mag = 40
hole_size = 40
noise_amount = 1000
# noise_amount = 0
cluster_amount = 2000
    
def generate(filename):
    points = []

    def make_cluster(amount, angle, hole_size, radius, offset_mag, center):
        for i in range(amount):
            r = PVector.random2D()
            a = degrees(r.heading()) + 180
            if abs(a - angle) < hole_size:
                continue

            m = random(radius - offset_mag, radius + offset_mag)
            r.setMag(m)
            r.add(center)
            rand_offset = PVector.random2D()
            rand_offset.setMag(offset_mag)
            # r.add(rand_offset)

            # if a > h_angle or a < l_angle:
            ellipse(r.x, r.y, 5, 5)
            points.append([r.x, r.y])

    

    one = PVector(225, height / 2)
    two = PVector(375, height / 2)

    make_cluster(cluster_amount, 250, hole_size, radius, offset_mag, one)
    make_cluster(cluster_amount, 70, hole_size, radius, offset_mag, two)

    for i in range(noise_amount):
        x = random(0, width)
        y = random(0, height)
        ellipse(x, y, 5, 5)
        points.append([x, y])

    points = (','.join((str(int(x)) for x in p)) for p in points)

    saveStrings(filename, points)


def show_data(filename):
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        ellipse(x[0], x[1], 5, 5)


# show_data('data/with_noise.csv')
generate('data/with_noise.csv')
saveFrame('with_noise.jpeg')
