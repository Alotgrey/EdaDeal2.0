package com.example.econom_main.Product.dtos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class CartControllerDto {
    Long product_id;
    String shop_name;
    String lon;
    String lat;
}
