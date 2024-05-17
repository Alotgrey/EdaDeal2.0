package com.example.econom_main.Product.entities.product_cost;

import lombok.Data;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
@Data
public class ProductCost {
    public Long id;
    public String name;
    public String image_url;
    public List<ShopCost> priceList;
    public ShopCost best_cost;

    public ProductCost(Product product, Cost cost){
        id = product.getId();
        name = product.getName();
        image_url = product.getImage_url();
        priceList = new ArrayList<>();
        if (cost.getPrice_5ka() > 0){
            priceList.add(new ShopCost("Пятёрочка", "5ka" , cost.getPrice_5ka()));
        }
        if (cost.getPrice_magnit() > 0){
            priceList.add(new ShopCost("Магнит", "magnit" , cost.getPrice_magnit()));
        }
        if (cost.getPrice_lenta() > 0){
            priceList.add(new ShopCost("Лента","lenta" , cost.getPrice_lenta()));
        }
        if (cost.getPrice_metro() > 0){
            priceList.add(new ShopCost("Метро ","metro" , cost.getPrice_metro()));
        }
        if (cost.getPrice_crossroad() > 0){
            priceList.add(new ShopCost("Перекрёсток","crossroad" , cost.getPrice_crossroad()));
        }
        priceList.sort(Comparator.comparing(ShopCost::getCost));
        best_cost = priceList.get(0);
        priceList.remove(0);
    }
}
