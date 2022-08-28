package com.enmusushi.onmyoji.util;

/**
 * @author Enmusushi
 */
public class OnmyojiConstants {
    public final static String[] COMMANDS = new String[6];
    public final static int AXIS_X = 4;
    public final static int AXIS_Y = 5;
    public final static int MAX_SCREEN_X = 1920;
    public final static int MAX_SCREEN_Y = 1080;
    public final static int RESPOND_TIME = 3000;
    static {
        COMMANDS[0] = "adb";
        COMMANDS[1] = "shell";
        COMMANDS[2] = "input";
        COMMANDS[3] = "tap";
    }
}
