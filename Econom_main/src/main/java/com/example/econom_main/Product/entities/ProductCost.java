package com.example.econom_main.Product.entities;

import lombok.Data;
import org.springframework.format.annotation.DateTimeFormat;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
@Data
public class ProductCost {
    public Long id;
    public String name;
    public String image_url;
    public List<ShopCost> priceList;
    public ShopCost bestCost;

    public ProductCost(Product product, Cost cost){
        id = product.getId();
        name = product.getName();
        image_url = product.getImage_url();
        priceList = new ArrayList<>();
        if (cost.getPrice_5ka() > 0){
            priceList.add(new ShopCost("Пятёрочка", cost.getPrice_5ka()));
        }
        if (cost.getPrice_magnit() > 0){
            priceList.add(new ShopCost("Магнит", cost.getPrice_magnit()));
        }
        if (cost.getPrice_lenta() > 0){
            priceList.add(new ShopCost("Лента", cost.getPrice_lenta()));
        }
        if (cost.getPrice_metro() > 0){
            priceList.add(new ShopCost("Метро ", cost.getPrice_metro()));
        }
        if (cost.getPrice_crossroad() > 0){
            priceList.add(new ShopCost("Перекрёсток", cost.getPrice_crossroad()));
        }
        priceList.sort(Comparator.comparing(o -> o.getCost()));
        bestCost = priceList.get(0);
        priceList.remove(0);
    }
}
