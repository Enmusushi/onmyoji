package com.enmusubi.onmyoji.schedule;

import com.enmusubi.onmyoji.onmyoji.device.Android;
import com.enmusubi.onmyoji.onmyoji.device.Pad;
import com.enmusubi.onmyoji.onmyoji.robot.AutoClicker;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.Arrays;

/**
 * @author Enmusushi
 */
@Component
public class ScheduledClick {
    private static final Logger logger = LoggerFactory.getLogger(ScheduledClick.class);
    private Android android = new Android();
    private Pad pad = new Pad();

    @Scheduled(fixedRate = 1000)
    public void executeAutoClick() {
        android.localeRandomPoint();
        execClick(android.getCommand());
        pad.localeRandomPoint();
        execClick(pad.getCommand());
    }

    public static void execClick(final String[] command) {
        ProcessBuilder processBuilder = new ProcessBuilder(command);
        try {
            logger.info(Arrays.toString(command));
            processBuilder.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
