package com.example.econom_main.Product.dtos;

import com.example.econom_main.Product.entities.product_cost.ProductCost;
import com.example.econom_main.Product.entities.product_cost.ShopCost;
import lombok.AllArgsConstructor;

@AllArgsConstructor
public class CartItem {
    public Long product_id;
    public String product_name;
    public String image_url;
    public ShopCost cost;
    public Long count;

}
