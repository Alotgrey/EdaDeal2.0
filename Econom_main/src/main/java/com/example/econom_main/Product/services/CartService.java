package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CartItem;
import com.example.econom_main.Product.entities.cart.RedisCart;
import com.example.econom_main.Product.entities.cart.ShopCart;
import com.example.econom_main.Product.entities.product_cost.ProductCost;
import com.example.econom_main.Product.entities.product_cost.ShopCost;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
@RequiredArgsConstructor
public class CartService {
    private final ProductCostService productCostService;
    private final static String HASH_KEY = "Cart";

    private final RedisTemplate redisTemplate;

    public String createCart(){
        String secretKey = KeyGenerator.getSecretKey();
        RedisCart redisCart = new RedisCart(secretKey);
        redisTemplate.opsForHash().put(HASH_KEY, redisCart.getId(), redisCart);
        return secretKey;
    }

    public List<ShopCart> getCart(String token) throws Exception {
        RedisCart redisCart = (RedisCart) redisTemplate.opsForHash().get("Cart", token);
        if (redisCart == null){
            throw (new Exception());
        }
        return redisCart.getCarts();
    }

    public void addToCart(String token,
                          Long product_id,
                          String shop_name,
                          String lon,
                          String lat) throws Exception {
        RedisCart redisCart = (RedisCart) redisTemplate.opsForHash().get("Cart", token);
        if (redisCart == null){
            throw (new Exception());
        }
        ProductCost productCost = productCostService.getProductCostById(product_id, lon, lat);
        List<ShopCost> shopCostList = productCost.priceList;
        CartItem cartItem;
        for (ShopCost shopCost : shopCostList){
            if (Objects.equals(shopCost.en_name, shop_name)){
                cartItem = new CartItem(product_id, productCost.name, productCost.image_url, shopCost, 1L);
                redisCart.addCartItem(cartItem);
            }
        }
        if (Objects.equals(productCost.best_cost.en_name, shop_name)){
            cartItem = new CartItem(product_id, productCost.name, productCost.image_url, productCost.best_cost,1L);
            redisCart.addCartItem(cartItem);
        }
        redisTemplate.opsForHash().put(HASH_KEY, redisCart.getId(), redisCart);
    }

    public void deleteFromCart(String token,
                               Long product_id,
                               String shop_name,
                               String lon,
                               String lat) throws Exception {
        RedisCart redisCart = (RedisCart) redisTemplate.opsForHash().get("Cart", token);
        if (redisCart == null){
            throw (new Exception());
        }
        ProductCost productCost = productCostService.getProductCostById(product_id, lon, lat);
        List<ShopCost> shopCostList = productCost.priceList;
        for (ShopCost shopCost : shopCostList){
            if (Objects.equals(shopCost.en_name, shop_name)){
                redisCart.deleteCartItem(product_id, shopCost.rus_name);
            }
        }
        if (Objects.equals(productCost.best_cost.en_name, shop_name)){
            redisCart.deleteCartItem(product_id, productCost.best_cost.rus_name);
        }
        redisTemplate.opsForHash().put(HASH_KEY, redisCart.getId(), redisCart);
    }
}
