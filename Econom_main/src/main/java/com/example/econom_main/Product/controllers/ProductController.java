package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.services.ProductCostService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequiredArgsConstructor
public class ProductController {
    @Autowired
    private ProductCostService productCostService;

    @GetMapping("/")
    private String getMainPage(){
        return "mainPage";
    }
    @GetMapping ("/products/{product_id}")
    private String getProduct(@PathVariable("product_id") Long product_id, Model model){
        model.addAttribute("product", productCostService.getProductCostById(product_id));
        return "productPage";
    }


}
