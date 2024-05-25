package com.example.econom_main.Product.entities.cart;

import com.example.econom_main.Product.dtos.CartItem;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;


public class ShopCart {
    public final String name;
    public List<CartItem> products;
    public Double total;

    public ShopCart(String name) {
        this.name = name;
        this.products = new ArrayList<>();
        this.total = 0.0;
    }

    public void addCartItem(CartItem cartItem){
        boolean f = true;
        for (int i = 0; i < products.size(); i++) {
            if (products.get(i).product_id == cartItem.product_id){
                products.get(i).count++;
                f = false;
            }
        }
        if (f){
            products.add(cartItem);
        }
        total += cartItem.cost.price;
        total = Math.round(total * 100) / 100.0;
    }

    public void deleteCartItem(Long product_id){
        for (int i =0; i < products.size(); i++){
            if (Objects.equals(products.get(i).product_id, product_id)){
                total -= products.get(i).cost.price;
                total = Math.round(total * 100) / 100.0;
                if (products.get(i).count == 1){
                    products.remove(i);
                }
                else {
                    products.get(i).count--;
                }
                break;
            }
        }
    }
}
