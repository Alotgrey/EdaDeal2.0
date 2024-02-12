package com.example.econom_main.Product.entities;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.math.BigDecimal;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name = "products")
public class Product {
    @Id
    @Column
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column
    String name;

    @Column
    BigDecimal cost;

    @Column
    String image_url;

    @Column
    Boolean status;

    @ManyToOne
    Shop shop;

    @ManyToOne
    Category category;
}
