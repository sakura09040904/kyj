/*  Data Analysis with Java
 *  John R. Hubbard
 *  June 7, 2017
 */

package com.example.chapter08;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

import org.apache.commons.math3.ml.clustering.CentroidCluster;
import org.apache.commons.math3.ml.clustering.DoublePoint;
import org.apache.commons.math3.ml.clustering.KMeansPlusPlusClusterer;

public class KMeans {
    private static final double[][] DATA = {{1,1}, {1,3}, {1,5}, {2,6}, {3,2}, 
        {3,4}, {4,3}, {5,6}, {6,3}, {6,4}, {7,1}, {7,5}, {7,6}};
    private static final int M = DATA.length;  // number of points
    private static final int K = 3;  // number of clusters
    private static HashSet<Point> points;  // maximum number of iterations
    private static HashSet<Cluster> clusters = new HashSet();
    private static Random RANDOM = new Random();
    
    public static void main(String[] args) {
        points = load(DATA);
        
        int i0 = RANDOM.nextInt(M);
        Point p = new Point(DATA[i0][0], DATA[i0][1]);
        points.remove(p);
        
        HashSet<Point> initSet = new HashSet();
        initSet.add(p);
        
        for(int i=0; i<K-1; i++) {
        	p = farthestFrom(initSet);
        	initSet.add(p);
        	points.remove(p);
        }

        for(Point point : initSet) {
        	Cluster cluster = new Cluster(point);
        	clusters.add(cluster);
        }
        
        for(Point point : points) {
        	Cluster cluster = closestTo(point);
        	cluster.add(point);
        	cluster.recomputeCentroid();
        }
        
       System.out.println(clusters);
    }
    
    private static HashSet<Point> load(double[][] data) {
        HashSet<Point> points = new HashSet();
        for (double[] datum : DATA) {
            points.add(new Point(datum[0], datum[1]));
        }
        return points;
    } 
    
    private static Cluster closestTo(Point point) {
    	double minDist = Double.POSITIVE_INFINITY;
    	Cluster c = null;
    	for(Cluster cluster:clusters) {
    		double d = distance2(cluster.getCentroid(),point);
    		if(d<minDist) {
    			minDist = d;
    			c = cluster;
    		}
    	} return c;
    }
    
    private static Point farthestFrom(Set<Point> set) {
    	Point p = null;
    	double maxDist = 0.0;
    	for(Point point: points) {
    		if(set.contains(point)) {
    			continue;
    		}
    		double d = dist(point,set);
    		if(d>maxDist) {
    			p = point;
    			maxDist = d;
    		}
    	} return p;
    }
     
    public static double dist(Point p, Set<Point> set) {
    	double minDist = Double.POSITIVE_INFINITY;
    	for (Point point:set) {
    		double d = distance2(p,point);
    		minDist = (d<minDist ? d:minDist);
    	} return minDist;
    }
    
    public static double distance2(Point p, Point q) {
    	double dx = p.getX() - q.getX();
    	double dy = p.getY() - q.getY();
    	return dx*dx + dy*dy;
    }
}
/*
run:
[[1.0, 1.0], [1.0, 3.0], [1.0, 5.0], [2.0, 6.0], [3.0, 2.0], [3.0, 4.0], [4.0, 3.0]]
[[5.0, 6.0], [6.0, 3.0], [6.0, 4.0], [7.0, 5.0], [7.0, 6.0]]
[[7.0, 1.0]]
run:
[[5.0, 6.0], [6.0, 3.0], [6.0, 4.0], [7.0, 1.0], [7.0, 5.0], [7.0, 6.0]]
[[1.0, 1.0], [1.0, 3.0], [3.0, 2.0], [3.0, 4.0], [4.0, 3.0]]
[[1.0, 5.0], [2.0, 6.0]]
*/
