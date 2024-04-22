package com.example.econom_main.Product.entities;

import com.example.econom_main.Product.entities.ShopCost;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.HashMap;
import java.util.TreeMap;
@Getter
public class ShoppingCart {
    private TreeMap<Long, HashMap<ShopCost, Long>> cart;
    private Double total_price;

    public void addProduct(Long id, ShopCost shopCost){
        if (cart.containsKey(id)){
            if (cart.get(id).containsKey(shopCost)){
                cart.get(id).put(shopCost, cart.get(id).get(shopCost) + 1);
            }
            else{
                cart.get(id).put(shopCost, 1L);
            }
        }
        else{
            cart.put(id, new HashMap<ShopCost, Long>());
            cart.get(id).put(shopCost, 1L);
        }
        total_price += shopCost.getCost();
    }

    public void deleteProduct(Long id, ShopCost shopCost){
        Long count = cart.get(id).get(shopCost);
        if (count > 1){
            cart.get(id).put(shopCost, count - 1);
        }
        else{
            cart.get(id).remove(shopCost);
            if (cart.get(id).isEmpty()){
                cart.remove(id);
            }
        }
        total_price -= shopCost.getCost();
    }

    public ShoppingCart() {
        cart = new TreeMap<Long, HashMap<ShopCost, Long>>();
        total_price = (double) 0;

    }
}
