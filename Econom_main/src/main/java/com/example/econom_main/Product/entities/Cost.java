package com.example.econom_main.Product.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

import java.sql.Date;

@RedisHash("Cost")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Cost {
    @Id
    private int id;
    private String imageUrl;
    private double price;
    private Date date;
}
