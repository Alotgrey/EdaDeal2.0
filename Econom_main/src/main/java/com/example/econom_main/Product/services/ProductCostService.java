package com.example.econom_main.Product.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ProductCostService {
    private final CostService costService;
    private final ProductService productService;

    @Autowired
    public ProductCostService(CostService costService, ProductService productService) {
        this.costService = costService;
        this.productService = productService;
    }


}
