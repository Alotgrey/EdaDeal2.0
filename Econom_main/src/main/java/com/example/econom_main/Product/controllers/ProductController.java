package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.services.CartService;
import com.example.econom_main.Product.services.ProductCostService;
import com.example.econom_main.Product.services.ProductService;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@Controller
@RequiredArgsConstructor
public class ProductController {
    private final ProductService productService;
    private final ProductCostService productCostService;
    private final CartService cartService;

    @GetMapping("/")
    private String getMainPage(Model model, HttpSession session) throws IOException {
        CategoryListDto allCategories = productCostService.getCategoriesTree();
        model.addAttribute("sweets", allCategories.getChildren().get(2).children.get(1));
        model.addAttribute("products", productService.getAllProducts());
        model.addAttribute("cart", cartService.getCart(session));
        return "mainPage";
    }

    @GetMapping("/category/{category_id}")
    private String getCategoryPage(@PathVariable("category_id") Long category_id, Model model, HttpSession session) throws IOException {
        CategoryListDto allCategories = productCostService.getCategoriesTree();
        model.addAttribute("milkcheeze", allCategories.getChildren().get(0));
        model.addAttribute("meatbird", allCategories.getChildren().get(1));
        model.addAttribute("milkcheeze", allCategories.getChildren().get(2));
        model.addAttribute("category_name", productService.getCategoryById(category_id).getName());
        model.addAttribute("products", productService.getAllProductsFromCategory(category_id));
        model.addAttribute("cart", cartService.getCart(session));
        return "categoryPage";
    }
    @GetMapping ("/products/{product_id}")
    private String getProduct(@PathVariable("product_id") Long product_id, Model model) throws IOException {
        model.addAttribute("product", productCostService.getProductCostById(product_id));
        return "productPage";
    }

    @GetMapping("/add-to-cart/{product_id}/{shop_name}")
    private void addToCart(@PathVariable("product_id") Long product_id, @PathVariable("shop_name") String shop_name, HttpSession session) throws IOException {
        cartService.addToCart(session, product_id, shop_name);
    }

    @GetMapping("/delete-from-cart/{product_id}/{shop_name}")
    private void deleteFromCart(@PathVariable("product_id") Long product_id, @PathVariable("shop_name") String shop_name, HttpSession session) throws IOException {
        cartService.deleteFromCart(session, product_id, shop_name);
    }
}