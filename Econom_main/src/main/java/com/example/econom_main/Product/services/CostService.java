package com.example.econom_main.Product.services;

import com.example.econom_main.Product.entities.Cost;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class CostService {
    public final static String HASH_KEY = "Cost";
    private final RedisTemplate redisTemplate;

    public void save(Cost cost){
        redisTemplate.opsForHash().put(HASH_KEY, cost.getId(), cost);
    }

    public List<Cost> findAll(){
        return redisTemplate.opsForHash().values(HASH_KEY);
    }

    public Cost findCostById(Long id){
        redisTemplate.opsForHash().delete(HASH_KEY, id);
        Cost cost = (Cost) redisTemplate.opsForHash().get(HASH_KEY, id);
        return cost;
        /*
        if (cost != null){
            return cost;
        }
        else{
            String url = "";

            HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create(url))
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            // Десериализация JSON ответа в объект Weather
            Weather weather = objectMapper.readValue(response.body(), Weather.class);

            return weather;


        }
        */
    }

    public String deleteCost(int id){
        redisTemplate.opsForHash().delete(HASH_KEY, id);
        return "Cost removed!";
    }
}
