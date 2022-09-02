package com.enmusubi.onmyoji.onmyoji.robot;

import java.util.Random;

/**
 * @author Enmusushi
 */
public class AutoClicker {

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


    /**
     * 通过adb命令自动点击御灵挑战按钮
     */
    public void localePoint(final String[] command) {
        int x = axisX + random.nextInt(bound);
        int y = axisY + random.nextInt(bound);
        command[6] = String.valueOf(x);
        command[7] = String.valueOf(y);
    }


}
