package com.example.econom_main.Product.services;
import java.security.SecureRandom;
import java.util.Base64;

public class KeyGenerator {

    public static String getSecretKey() {
        SecureRandom random = new SecureRandom();
        byte[] key = new byte[64];
        random.nextBytes(key);
        String encodedKey = Base64.getEncoder().encodeToString(key);
        return encodedKey;
    }

}
