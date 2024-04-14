import argparse
import point


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = 'mcm',
        description = 'Sint-Maarten Bovenschool - Wiskunde OC - Monte-Carlo Method - 2024')
    parser.add_argument('-n', '--npoints', type=int)
    parser.add_argument('-r', '--radius', type=int)
    args = parser.parse_args()
    
    points = [point.random_point(args.radius) for _ in range(args.npoints)]
    points_in_circle = [p for p in points if p.in_circle(args.radius)]
    
    print(len(points), len(points_in_circle), (len(points_in_circle)*4)/len(points))
