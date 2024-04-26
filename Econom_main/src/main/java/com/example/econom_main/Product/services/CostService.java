package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CostDto;
import com.example.econom_main.Product.entities.Cost;
import com.example.econom_main.Product.mappers.CostMapper;
import com.example.econom_main.Product.repositories.ProductRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;


import java.io.IOException;
import java.net.URL;
import java.sql.Date;
import java.time.LocalDate;
import java.util.List;

@Service
@AllArgsConstructor
public class CostService {
    private final static String HASH_KEY = "Cost";
    private final RedisTemplate redisTemplate;
    private final ProductRepository productRepository;
    private final CostMapper costMapper;

    public void save(Cost cost){
        redisTemplate.opsForHash().put(HASH_KEY, cost.getId(), cost);
    }

    public List<Cost> findAll(){
        return redisTemplate.opsForHash().values(HASH_KEY);
    }

    public Cost findCostById(Long id) throws IOException {
        Cost cost = (Cost) redisTemplate.opsForHash().get(HASH_KEY, id);
        if (cost == null || cost.getDate().equals(Date.valueOf(LocalDate.now()))){
            String lon = "45.955370";
            String lat = "51.502440";
            String url_str = "http://127.0.0.1:8000/api/v2/parser/item/?lon="+ lon +"&lat=" + lat + "&item_name=";
            url_str += productRepository.findById(id).get().getLink();
            URL url = new URL(url_str);
            ObjectMapper objectMapper = new ObjectMapper();
            CostDto costDto = objectMapper.readValue(url, CostDto.class);
            save(costMapper.toCost(id, costDto));
        }
        return cost;

    }

    public void deleteCost(Long id){
        redisTemplate.opsForHash().delete(HASH_KEY, id);
    }
}
