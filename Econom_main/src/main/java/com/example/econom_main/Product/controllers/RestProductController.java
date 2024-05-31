package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.product_cost.Product;
import com.example.econom_main.Product.entities.product_cost.ProductCost;
import com.example.econom_main.Product.services.CartService;
import com.example.econom_main.Product.services.ProductCostService;
import com.example.econom_main.Product.services.ProductService;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@RestController
@RequiredArgsConstructor
public class RestProductController {
    private final ProductService productService;
    private final ProductCostService productCostService;
    private final CartService cartService;

    @GetMapping ("/api/categories")
    private CategoryListDto getCategories(){
        return productCostService.getCategoriesTree();
    }

    @GetMapping ("/api/categories/{category_id}")
    private List<ProductDto> getCategories(@PathVariable("category_id") Long category_id,
                                           @RequestParam(value = "page", defaultValue = "1") int pageNo){
        return productService.getAllProductsFromCategory(category_id, pageNo);
    }

    @GetMapping ("/api/products")
    private List<ProductDto> getProducts(@RequestParam(value = "page", defaultValue = "1") int pageNo){
        return productService.getAllProductsPage(pageNo);
    }

    @GetMapping ("/api/products/{product_id}")
    private ProductCost getProduct(@PathVariable("product_id") Long product_id,
                                   @RequestParam("lon") String lon,
                                   @RequestParam("lat") String lat) throws IOException {
        lon = "45.955370";
        lat = "51.502440";
        return productCostService.getProductCostById(product_id, lon, lat);
    }

}
