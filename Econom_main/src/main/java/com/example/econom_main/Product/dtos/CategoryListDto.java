package com.example.econom_main.Product.dtos;

import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.List;

@Data
@RequiredArgsConstructor
public class CategoryListDto {
    private Long id;
    private String name;
    private String image_url;
    private Boolean isFinal;
    private List<CategoryListDto> children;
}
