package com.enmusubi.onmyoji.event;

import com.enmusubi.onmyoji.util.OnmyojiConstants;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @author Enmusushi
 */
public class TotemThread implements Runnable {
    private Totem totem = new Totem();
    private Lock lock = new ReentrantLock();

    @Override
    public void run() {
        lock.lock();
        try {
            totem.autoClickTotem();
            Thread.sleep(OnmyojiConstants.RESPOND_TIME);
            totem.autoClickTotem();
            Thread.sleep(totem.getInternal());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }


}
