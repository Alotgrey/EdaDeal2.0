package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.services.ProductService;
import com.example.econom_main.Product.entities.Product;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class ProductController {

    @Autowired
    private ProductService productService;

    @GetMapping("/products")
    private String getProduct(){
        return "productPage";
    }
}
