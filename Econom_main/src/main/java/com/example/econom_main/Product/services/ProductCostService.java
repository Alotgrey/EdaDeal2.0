package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.entities.product_cost.ProductCost;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service
@RequiredArgsConstructor
public class ProductCostService {
    private final CostService costService;
    private final ProductService productService;

    public ProductCost getProductCostById(Long id) throws IOException {
        return new ProductCost(productService.getProductById(id), costService.findCostById(id, "45.955370", "51.502440"));
    }

    public CategoryListDto getCategoriesTree(){
        return productService.getCategoryListDtoById(0L);
    }


}
