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

    @ManyToOne
    private Category category;

    @Column
    String link_magnit;

    @Column
    String link_5ka;

    @Column
    String link_crossroad;

    @Column
    String link_lenta;

    @Column
    String link_metro;
}
