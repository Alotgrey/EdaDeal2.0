package com.example.econom_main.Product.mappers;

import com.example.econom_main.Product.dtos.CostDto;
import com.example.econom_main.Product.entities.Cost;
import org.springframework.stereotype.Component;

import java.sql.Date;
import java.time.LocalDate;

@Component
public class CostMapper {
    public Cost toCost(Long id, CostDto costDto){
        Cost cost = new Cost();
        cost.setId(id);
        cost.setDate(Date.valueOf(LocalDate.now()));
        cost.setPrice_5ka(costDto.getOffers().get_5ka());
        cost.setPrice_magnit(costDto.getOffers().getMagnit());
        cost.setPrice_lenta(costDto.getOffers().getLenta());
        cost.setPrice_crossroad(costDto.getOffers().getCrossroad());
        cost.setPrice_metro(costDto.getOffers().getMetro());
        return cost;
    }
}
