package com.enmusubi.onmyoji.onmyoji.device;

import java.util.Random;

/**
 * @author Enmusushi
 */
public class Pad {


    /**
     * 点击的横坐标 1750-1950
     * 1900
     */
    private Integer axisX = 1750;

    /**
     * 点击的纵坐标 850-1050
     */

    private Integer axisY = 1050;

    private int bound = 100;

    private Random random = new Random();

    private final String[] command = new String[8];

    public Pad() {
        command[0] = "adb";
        command[1] = "-s";
        command[2] = "192.168.1.64:5555";
        command[3] = "shell";
        command[4] = "input";
        command[5] = "tap";
    }

    /**
     * 通过adb命令自动点击御灵挑战按钮
     */
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
