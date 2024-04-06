package com.example.econom_main.Product.entities;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    String name;
    private String image_url;

    @ManyToOne()
    @JoinColumn(name = "category_id")
    private Category category;
    private String link_magnit;
    private String link_5ka;
    private String link_crossroad;
    private String link_lenta;
    private String link_metro;
}
