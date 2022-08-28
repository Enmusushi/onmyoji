package com.enmusubi.onmyoji.test;

import org.opencv.core.Core;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TestReadFile {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("C:\\Users\\Enmusushi\\Desktop\\test.png");
        FileInputStream fileInputStream = new FileInputStream(file);
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        try {
            byte[] bytes = fileInputStream.readAllBytes();
            System.out.println();
            for (byte b : bytes) {
                System.out.print(b);
            }
            System.out.println();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
