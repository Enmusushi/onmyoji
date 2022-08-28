package com.enmusubi.onmyoji.util;

import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author Enmusushi
 */
public class ExecClicker {
    private static AtomicInteger count = new AtomicInteger(0);

    public static void execClickPoint(int axisX, int axisY) {
        OnmyojiConstants.COMMANDS[OnmyojiConstants.AXIS_X] = String.valueOf(axisX);
        OnmyojiConstants.COMMANDS[OnmyojiConstants.AXIS_Y] = String.valueOf(axisY);
        execClick();
    }


    public static void execClick() {
        ProcessBuilder processBuilder = new ProcessBuilder(OnmyojiConstants.COMMANDS);
        try {
            System.out.print(count.incrementAndGet() + "\t");
            System.out.println(processBuilder.command());
            processBuilder.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            Thread.sleep(OnmyojiConstants.RESPOND_TIME);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
