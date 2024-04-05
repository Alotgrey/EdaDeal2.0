package com.example.econom_main.Product.services;

import com.example.econom_main.Product.entities.Cost;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CostService {
    public final static String HASH_KEY = "Cost";
    @Autowired
    private RedisTemplate redisTemplate;

    public void save(Cost cost){
        redisTemplate.opsForHash().put(HASH_KEY, cost.getId(), cost);
    }

    public List<Cost> findAll(){
        return redisTemplate.opsForHash().values(HASH_KEY);
    }

    public Cost findCostById(Long id){
        return (Cost) redisTemplate.opsForHash().get(HASH_KEY, id);
    }

    public String deleteCost(int id){
        redisTemplate.opsForHash().delete(HASH_KEY, id);
        return "Cost removed!";
    }
}
