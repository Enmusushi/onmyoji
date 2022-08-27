package com.enmusushi.onmyoji.event;

import com.enmusushi.onmyoji.robot.EndBattleClicker;
import com.enmusushi.onmyoji.util.ExecClicker;
import com.enmusushi.onmyoji.util.OnmyojiConstants;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * @author Enmusushi
 */
public class Totem {
    /**
     * 默认20s点击一次
     */
    private Integer internal = 24000;
    /**
     * 点击的横坐标 1750-1950
     */
    private Integer axisX = 1750;

    /**
     * 点击的纵坐标 850-1050
     */

    private Integer axisY = 850;

    private int bound = 100;

    public Integer getInternal() {
        return internal;
    }

    public void setInternal(Integer internal) {
        this.internal = internal;
    }

    /**
     * 通过adb命令自动点击御灵挑战按钮
     */
    public void autoClickTotem() {
        Random random = new Random();
        int x = axisX + random.nextInt(bound);
        int y = axisY + random.nextInt(bound);
        ExecClicker.execClickPoint(x, y);
    }


}
