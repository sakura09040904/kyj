/*  Data Analysis with Java
 *  John R. Hubbard
 *  Jun 18, 2017
 */

package com.example.chapter08;

import java.util.ArrayList;
import weka.clusterers.SimpleKMeans;
import weka.core.Attribute;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.SparseInstance;

public class KMeansWeka {
    private static final double[][] DATA = {{1,1}, {1,3}, {1,5}, {2,6}, {3,2}, 
        {3,4}, {4,3}, {5,6}, {6,3}, {6,4}, {7,1}, {7,5}, {7,6}};
    private static final int M = DATA.length;  // number of points
    private static final int K = 3;            // number of clusters

    public static void main(String[] args) {
        Instances dataset = load(DATA);
        SimpleKMeans skm = new SimpleKMeans();
        System.out.printf("%d clusters:%n", K);
        try {
            skm.setNumClusters(K);
            skm.buildClusterer(dataset);
            for (Instance instance : dataset) {
                System.out.printf("(%.0f,%.0f): %s%n", 
                        instance.value(0), instance.value(1), 
                        skm.clusterInstance(instance));
            }
        } catch (Exception e) {
            System.err.println(e);
        }
    }
    
    private static Instances load(double[][] data) {
        ArrayList<Attribute> attributes = new ArrayList<Attribute>();
        attributes.add(new Attribute("X"));
        attributes.add(new Attribute("Y"));
        Instances dataset = new Instances("Dataset", attributes, M);
        for (double[] datum : data) {
            Instance instance = new SparseInstance(2);
            instance.setValue(0, datum[0]);
            instance.setValue(1, datum[1]);
            dataset.add(instance);
        }
        return dataset;
    }
}

/*
run:
3 clusters:
(1,1): 1
(1,3): 1
(1,5): 0
(2,6): 0
(3,2): 1
(3,4): 0
(4,3): 0
(5,6): 0
(6,3): 2
(6,4): 2
(7,1): 2
(7,5): 2
(7,6): 2
*/
