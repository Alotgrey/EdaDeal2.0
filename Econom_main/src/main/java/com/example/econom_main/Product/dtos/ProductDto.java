package com.example.econom_main.Product.dtos;

import com.example.econom_main.Product.entities.Category;
import jakarta.persistence.*;
import lombok.Data;
import lombok.RequiredArgsConstructor;

@Data
@RequiredArgsConstructor
public class ProductDto {

    String name;
    private String image_url;
    private Long category_id;
    private String link_magnit;
    private String link_5ka;
    private String link_crossroad;
    private String link_lenta;
    private String link_metro;
}
