package com.example.econom_main.Product.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

import java.io.Serializable;
import java.sql.Date;

@RedisHash("Cost")
@Data
public class Cost implements Serializable {
    @Id
    private Long id;
    double price_magnit;
    double price_5ka;
    double price_crossroad;
    double price_lenta;
    double price_metro;
    private Date date;
}