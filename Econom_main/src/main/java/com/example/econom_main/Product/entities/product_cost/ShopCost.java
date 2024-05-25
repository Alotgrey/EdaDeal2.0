package com.example.econom_main.Product.entities.product_cost;

import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
public class ShopCost{
    public String rus_name;
    public String en_name;
    public Double price;

    @Override
    public int hashCode() {
        return en_name.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }
}
