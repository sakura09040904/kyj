package com.example.chapter08;

import org.apache.commons.math3.ml.distance.*;

public class CalEuclide {

	public static void main(String[] args) {
		double[] a = {-1,2,3};
		double[] b = {4,0,-3};
		
		calEuclideanDist(a,b);

	}
	
	public static void calEuclideanDist(double[] a, double[] b) {
		double sum = 0;
		for (int i =0; i< a.length; i++) {
			sum += Math.pow(a[i]-b[i], 2);
		}
		double distance = Math.sqrt(sum);
		System.out.println(distance);
		
	}

}
