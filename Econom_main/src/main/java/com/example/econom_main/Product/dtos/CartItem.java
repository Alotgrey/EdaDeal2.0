package com.example.econom_main.Product.dtos;

import lombok.Data;
import lombok.RequiredArgsConstructor;


@Data
public class CartItem {
    public Long product_id;
    public String product_name;
    public Double cost;
    public Long count;

    public CartItem(Long id, String name, Double cost, Long aLong) {
    }
}
