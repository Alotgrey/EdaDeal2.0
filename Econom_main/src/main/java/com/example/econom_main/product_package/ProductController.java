package com.example.econom_main.product_package;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class ProductController {

    @Autowired
    private ProductService productService;

    @GetMapping("/products")
    private List<Product> getAllProducts(){
        return productService.getAllProducts();
    }

    @GetMapping("/products/{product_id}")
    private Product getProduct(@PathVariable("product_id") long product_id){
        return productService.getProductById(product_id);
    }

    @PostMapping("/add")
    private void addNewProduct(@RequestBody Product product){
        productService.addNewProduct(product);
    }
}
