package com.example.econom_main.Product.entities.cart;

import com.example.econom_main.Product.dtos.CartItem;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
public class SessionCart {
    private List<ShopCart> carts;

    public SessionCart() {
        this.carts = new ArrayList<>();
        this.carts.add(new ShopCart("Корзина пуста"));
        this.carts.add(new ShopCart("Магнит"));
        this.carts.add(new ShopCart("Пятёрочка"));
        this.carts.add(new ShopCart("Лента"));
        this.carts.add(new ShopCart("Метро"));
        this.carts.add(new ShopCart("Перекрёсток"));
    }

    public ShopCart getMostProfitableCart(){
        carts.sort(new Comparator<ShopCart>() {
            @Override
            public int compare(ShopCart o1, ShopCart o2) {
                return o1.total.compareTo(o2.total);
            }
        });
        int ind = 0;
        while (ind < carts.size() && carts.get(ind).products.isEmpty()){
            ind++;
        }
        if (ind < carts.size()){
            return carts.get(ind);
        }
        return carts.get(0);
    }

    public void addCartItem(CartItem cartItem){
        for (ShopCart shopCart : carts){
            if (cartItem.cost.rus_name == shopCart.name){
                shopCart.addCartItem(cartItem);
            }
        }
    }

    public void deleteCartItem(Long product_id){
        for (ShopCart shopCart : carts){
            shopCart.deleteCartItem(product_id);
        }
    }

}
