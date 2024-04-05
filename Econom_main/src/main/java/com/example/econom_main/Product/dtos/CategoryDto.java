package com.example.econom_main.Product.dtos;

import com.example.econom_main.Product.entities.Category;
import jakarta.persistence.*;
import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.ArrayList;
import java.util.List;
@Data
@RequiredArgsConstructor
public class CategoryDto {
    private String name;
    private String image_url;
    private Boolean isFinal;
    private Long parent_id;
}
