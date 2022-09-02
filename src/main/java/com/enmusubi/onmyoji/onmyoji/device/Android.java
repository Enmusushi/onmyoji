package com.enmusubi.onmyoji.onmyoji.device;

import java.util.Random;

/**
 * @author Enmusushi
 */
public class Android {

    private Integer axisX = 1750;

    /**
     * 点击的纵坐标 850-1050
     */

    private Integer axisY = 850;

    private int bound = 100;

    private Random random = new Random();

    private final String[] command = new String[8];

    public Android() {
        command[0] = "adb";
        command[1] = "-s";
        command[2] = "192.168.1.57:5555";
        command[3] = "shell";
        command[4] = "input";
        command[5] = "tap";
    }

    public void localeRandomPoint() {
        int x = axisX + random.nextInt(bound);
        int y = axisY + random.nextInt(bound);
        command[6] = String.valueOf(x);
        command[7] = String.valueOf(y);
    }

    public String[] getCommand() {
        return this.command;
    }


}
