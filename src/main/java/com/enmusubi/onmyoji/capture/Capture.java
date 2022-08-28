package com.enmusubi.onmyoji.capture;

import java.io.*;

/**
 * @author Enmusushi
 */
public class Capture {

    public static void capture() {
        String[] commands = new String[4];
        commands[0] = "adb";
        commands[1] = "shell";
        commands[2] = "screencap";
        commands[3] = "-p";
        ProcessBuilder processBuilder = new ProcessBuilder(commands);
        Process process = null;
        try {
            process = processBuilder.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (process != null) {
            InputStream inputStream = process.getInputStream();

            File file = new File("C:\\Users\\Enmusushi\\Desktop\\test.png");
            try {
                FileOutputStream fileOutputStream = new FileOutputStream(file);
                byte[] bytes1 = inputStream.readAllBytes();
                fileOutputStream.write(bytes1);
                long bytes = inputStream.transferTo(fileOutputStream);
                System.out.println(bytes);
                inputStream.close();
                fileOutputStream.close();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Capture.capture();
        //Capture.test();
    }

    public static void test() {
        File file = new File("C:\\Users\\Enmusushi\\Desktop\\fsdownload\\test.png");
        File newFile = new File("C:\\Users\\Enmusushi\\Desktop\\test.png");
        BufferedReader br = null;
        try {
            br = new BufferedReader(new InputStreamReader(new FileInputStream(file), "gbk"));
        } catch (UnsupportedEncodingException | FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(newFile)));
            String line = br.readLine();
            while (line != null && line.length() > 0) {
                System.out.println(line);
                bw.write(line);
                bw.newLine();
                line = br.readLine();
            }
            br.close();
            bw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
