package com.enmusushi.onmyoji.robot;

import com.enmusushi.onmyoji.util.ExecClicker;
import com.enmusushi.onmyoji.util.OnmyojiConstants;

import java.util.Random;

/**
 * @author Enmusushi
 */
public class EndBattleClicker {


    public static void randomClicker() {
        Random random = new Random();
        int axisX = random.nextInt(OnmyojiConstants.MAX_SCREEN_X);
        int axisY = random.nextInt(OnmyojiConstants.MAX_SCREEN_Y);
        ExecClicker.execClickPoint(axisX, axisY);
    }

}
