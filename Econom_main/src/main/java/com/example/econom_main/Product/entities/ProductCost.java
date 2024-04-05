package com.example.econom_main.Product.entities;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

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
        priceList.add(new ShopCost("Пятёрочка", cost.getPrice_5ka()));
        priceList.add(new ShopCost("Магнит", cost.getPrice_magnit()));
        priceList.add(new ShopCost("Лента", cost.getPrice_lenta()));
        priceList.add(new ShopCost("Метро ", cost.getPrice_metro()));
        priceList.add(new ShopCost("Перекрёсток", cost.getPrice_crossroad()));
        priceList.sort(Comparator.comparing(o -> o.cost));
        bestCost = priceList.get(0);
        priceList.remove(0);
    }
}
