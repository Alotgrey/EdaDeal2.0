package com.example.econom_main.Product.dtos;

import lombok.Data;
import lombok.RequiredArgsConstructor;

@Data
@RequiredArgsConstructor
public class CategoryDto {
    public Long id;
    public String name;
    public String image_url;
    public Boolean isFinal;
    public Long parent_id;
}
