package com.example.econom_main.Product.entities;

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
    public Long id;
    String name;
    public String image_url;

    @ManyToOne()
    @JoinColumn(name = "category_id")
    public Category category;
    public String link;
}
