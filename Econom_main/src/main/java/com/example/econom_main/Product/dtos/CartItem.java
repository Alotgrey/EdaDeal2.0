package com.example.econom_main.Product.dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.RequiredArgsConstructor;


@Data
@AllArgsConstructor
public class CartItem {
    public Long product_id;
    public String product_name;
    public Double cost;
    public Long count;
}
