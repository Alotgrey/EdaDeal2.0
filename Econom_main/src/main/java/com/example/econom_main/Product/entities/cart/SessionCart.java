package com.example.econom_main.Product.entities.cart;

import com.example.econom_main.Product.dtos.CartItem;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;

public class SessionCart {
    private List<ShopCart> carts;

    public SessionCart() {
        this.carts = new ArrayList<>();
        this.carts.add(new ShopCart("Магнит"));
        this.carts.add(new ShopCart("Пятёрочка"));
        this.carts.add(new ShopCart("Лента"));
        this.carts.add(new ShopCart("Метро"));
        this.carts.add(new ShopCart("Перекрёсток"));
        this.carts.add(new ShopCart("Ашан"));
    }

    public  List<ShopCart> getCarts(){
        return carts.stream().sorted(new Comparator<ShopCart>() {
            @Override
            public int compare(ShopCart o1, ShopCart o2) {
                return o1.total.compareTo(o2.total);
            }
        }).toList();
    }

    public void addCartItem(CartItem cartItem){
        for (ShopCart shopCart : carts){
            if (Objects.equals(cartItem.cost.rus_name, shopCart.name)){
                shopCart.addCartItem(cartItem);
            }
        }
    }

    public void deleteCartItem(Long product_id, String shop_name){
        for (ShopCart shopCart : carts){
            if (Objects.equals(shop_name, shopCart.name)){
                shopCart.deleteCartItem(product_id);
            }
        }
    }

}
