package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.entities.Cost;
import com.example.econom_main.Product.entities.Product;
import com.example.econom_main.Product.mappers.CategoryMapper;
import com.example.econom_main.Product.mappers.ProductMapper;
import com.example.econom_main.Product.services.CostService;
import com.example.econom_main.Product.services.ProductCostService;
import com.example.econom_main.Product.services.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class DataInsert {
    private final CostService costService;
    private final ProductService productService;
    private final ProductCostService productCostService;

    @GetMapping ("/api/categories")
    private List<CategoryDto> getCategories(){
        return productService.getAllCategories();
    }

    @GetMapping ("/api/products")
    private List<ProductDto> getProducts(){
        return productService.getAllProducts();
    }

    @PostMapping("/api/costs/add")
    private void saveCost(@RequestBody Cost cost){
        costService.save(cost);
    }

    @PostMapping("/api/categories/add")
    private void addCategory(@RequestBody CategoryDto categoryDto){
        productService.addNewCategory(categoryDto);
    }

    @PostMapping("/api/products/add")
    private void addProduct(@RequestBody ProductDto productDto){
        productService.addNewProduct(productDto);
    }

    @GetMapping("/categories")
    private CategoryListDto getMainCategory(){
        return productCostService.getCategoriesTree();
    }

}
