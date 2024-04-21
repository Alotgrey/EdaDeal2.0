package com.example.econom_main.Product.dtos;

import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.List;

@Data
@RequiredArgsConstructor
public class CategoryListDto {
    public Long id;
    public String name;
    public String image_url;
    public Boolean isFinal;
    public List<CategoryListDto> children;
}
