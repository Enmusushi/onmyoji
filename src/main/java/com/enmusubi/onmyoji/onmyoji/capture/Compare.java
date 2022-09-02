package com.enmusubi.onmyoji.onmyoji.capture;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/**
 * @author Enmusushi
 */
public class Compare {

    private static final String path = "D:\\GitRoot\\GitHub\\onmyoji\\py\\screen\\";

    public static void main(String[] args) {
        File f = new File(path + "test.png");
        File p = new File(path + "testp.png");
        try {
            FileInputStream fis = new FileInputStream(f);
            FileInputStream fp = new FileInputStream(p);
            byte[] fisb = fis.readAllBytes();
            byte[] fpb = fp.readAllBytes();
            int count = 0;
            for (int i = 0; i < fisb.length && i < fpb.length; i++) {
                if (fisb[i] != fpb[i]) {
                    System.out.println(i + ": " + fisb[i] + " , " + fpb[i]);
                    count++;
                    break;
                }
            }
            System.out.println(count);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }

}
