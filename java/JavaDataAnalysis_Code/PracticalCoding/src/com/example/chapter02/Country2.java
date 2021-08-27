package com.example.chapter02;

import java.util.Scanner;

public class Country2 implements Comparable {
    protected String name;
    protected int population;

	public Country2(String name, int population) {
		this.name = name;
		this.population = population;
	}
 
    public Country2(Scanner in) {
        if (in.hasNextLine()) {
            this.name = in.next();
            this.population = in.nextInt();
 
        }
    }
    
    public boolean isNull() {
    	return this.name==null;
    }
    @Override
	public int compareTo(Object object) {
		Country2 that = (Country2) object;
		return this.population-that.population;
	}

	@Override
    public String toString() {
        return String.format("%-10s %12d",name, population);
    }



}
