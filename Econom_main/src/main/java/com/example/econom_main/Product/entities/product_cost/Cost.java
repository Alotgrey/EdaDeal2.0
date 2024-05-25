package com.example.econom_main.Product.entities.product_cost;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;

import java.io.Serializable;
import java.sql.Date;


@Data
@AllArgsConstructor
@NoArgsConstructor
public class Cost {
    @Id
    private Long id;
    public double price_magnit;
    public double price_5ka;
    public double price_crossroad;
    public double price_lenta;
    public double price_metro;
    public double price_auchan;
    public Date date;
}
