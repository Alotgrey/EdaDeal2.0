package com.example.econom_main.Product.dtos;

import lombok.Data;
import lombok.RequiredArgsConstructor;

@Data
@RequiredArgsConstructor
public class ProductDto {
    public Long id;
    public String name;
    public String image_url;
    public Long category_id;
    public String link;
}
