package com.example.econom_main.Product.services;

import com.example.econom_main.Product.entities.Cost;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CostService {
    public final static String HASH_KEY = "Cost";
    private RedisTemplate redisTemplate;

    public Cost save(Cost cost){
        redisTemplate.opsForHash().put(HASH_KEY, cost.getId(), cost);
        return cost;
    }

    public List<Cost> findAll(){
        return redisTemplate.opsForHash().values(HASH_KEY);
    }

    public Cost findCostById(int id){
        return (Cost) redisTemplate.opsForHash().get(HASH_KEY, id);
    }

    public String deleteCost(int id){
        redisTemplate.opsForHash().delete(HASH_KEY, id);
        return "Cost removed!";
    }
}
