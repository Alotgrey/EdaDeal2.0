package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.entities.ProductCost;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ProductCostService {
    @Autowired
    private final CostService costService;
    @Autowired
    private final ProductService productService;

    public ProductCost getProductCostById(Long id) {
        return new ProductCost(productService.getProductById(id), costService.findCostById(id));
    }

    public CategoryListDto getCategoriesTree(){
        return productService.getCategoryListDtoById(1L);
    }


}
