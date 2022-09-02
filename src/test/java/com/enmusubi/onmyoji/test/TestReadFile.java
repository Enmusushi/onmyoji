package com.enmusubi.onmyoji.test;

import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TestReadFile {

    public static Mat testMat()  {
        File file = new File("C:\\Users\\Enmusushi\\Desktop\\test.png");
        FileInputStream fileInputStream = null;
        try {
            fileInputStream = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        Mat mat;
        try {
            BufferedImage image = ImageIO.read(fileInputStream);
            mat = bufImg2Mat(image, BufferedImage.TYPE_BYTE_BINARY, CvType.CV_8UC1);
            System.out.println();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return mat;
    }

    public static Mat bufImg2Mat(BufferedImage original, int imgType, int matType) {
        if (original == null) {
            throw new IllegalArgumentException("original == null");
        }
        // Don't convert if it already has correct type
        if (original.getType() != imgType) {
            // Create a buffered image
            BufferedImage image = new BufferedImage(original.getWidth(), original.getHeight(), imgType);
            // Draw the image onto the new buffer
            Graphics2D g = image.createGraphics();
            try {
                g.setComposite(AlphaComposite.Src);
                g.drawImage(original, 0, 0, null);
                original = image;
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                g.dispose();
            }
        }
        byte[] pixels = ((DataBufferByte) original.getRaster().getDataBuffer()).getData();
        Mat mat = Mat.eye(original.getHeight(), original.getWidth(), matType);
        mat.put(0, 0, pixels);
        return mat;
    }

}
