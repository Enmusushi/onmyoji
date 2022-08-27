package com.enmusushi.onmyoji;

import com.enmusushi.onmyoji.event.TotemThread;

import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * @author Enmusushi
 */
public class Onmyoji {

    private static ScheduledExecutorService scheduler;

    public static void main(String[] args) {
        scheduler = new ScheduledThreadPoolExecutor(1);
        int times = 3000;
        TotemThread totemThread = new TotemThread();
        for (int i = 0; i < times; i++) {
            scheduler.schedule(totemThread, 1000L, TimeUnit.MILLISECONDS);
        }
    }
}
