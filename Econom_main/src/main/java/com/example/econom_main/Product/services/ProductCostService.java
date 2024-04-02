package com.example.econom_main.Product.services;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProductCostService {
    private final CostService costService;
    private final ProductService productService;


}
