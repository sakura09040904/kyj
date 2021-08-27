package com.example.chapter02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

public class FilteringData {
    private static final int MIN_AREA = 1000000;  // one million 
    public static void main(String[] args) {
        File file = new File("data/Countries2.dat");
        Set<Country> dataset = readDataset(file);
        
        for (Country country : dataset) {
            if (country.landlocked && country.area >= MIN_AREA) {
                System.out.println(country);
            }
        }
    }
    
    public static Set readDataset(File file) {
        Set<Country> set = new HashSet();
        try {
            Scanner input = new Scanner(file);
            input.nextLine();  // read past headers
            while (input.hasNextLine()) {
                set.add(new Country(input));
            }
            input.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
        return set;
    }
}