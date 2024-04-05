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
    @Column
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column
    String name;

    @Column
    private String image_url;

    @ManyToOne()
    @JoinColumn(name = "category_id")
    private Category category;

    @Column
    private String link_magnit;

    @Column
    private String link_5ka;

    @Column
    private String link_crossroad;

    @Column
    private String link_lenta;

    @Column
    private String link_metro;
}
