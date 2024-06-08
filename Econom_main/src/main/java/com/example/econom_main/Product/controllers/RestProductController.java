package com.example.econom_main.Product.controllers;

import com.example.econom_main.Product.dtos.CartControllerDto;
import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.cart.ShopCart;
import com.example.econom_main.Product.entities.product_cost.ProductCost;
import com.example.econom_main.Product.services.CartService;
import com.example.econom_main.Product.services.ProductCostService;
import com.example.econom_main.Product.services.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class RestProductController {
    private final ProductService productService;
    private final ProductCostService productCostService;
    private final CartService cartService;

    @GetMapping ("/categories")
    private CategoryListDto getCategories(){
        return productCostService.getCategoriesTree();
    }

    @GetMapping ("/categories/{category_id}")
    private List<ProductDto> getCategories(@PathVariable("category_id") Long category_id,
                                           @RequestParam(value = "page", defaultValue = "1") int pageNo){
        return productService.getAllProductsFromCategory(category_id, pageNo);
    }

    @GetMapping ("/products")
    private List<ProductDto> getProducts(@RequestParam(value = "page", defaultValue = "1") int pageNo){
        return productService.getAllProductsPage(pageNo);
    }

    @GetMapping ("/products/find")
    private List<ProductDto> getProducts(@RequestParam("search") String search,
                                         @RequestParam(value="page", defaultValue = "1") int pageNo){
        return productService.searchProductsByKeywords(search, pageNo);
    }

    @GetMapping ("/products/{product_id}")
    private ProductCost getProduct(@PathVariable("product_id") Long product_id,
                                   @RequestParam("lon") String lon,
                                   @RequestParam("lat") String lat) throws IOException {

        return productCostService.getProductCostById(product_id, lon, lat);
    }

    @GetMapping("/create-cart")
    private String createCart(){
        return cartService.createCart();
    }

    @GetMapping("/cart")
    private List<ShopCart> getCart(@RequestHeader("Authorization") String token) throws Exception {
        return cartService.getCart(token);
    }

    @PostMapping("/cart/add")
    private List<ShopCart> addToCart(@RequestHeader("Authorization") String token,
                                     @RequestBody CartControllerDto cartControllerDto) throws Exception {
        cartService.addToCart(
                token,
                cartControllerDto.getProduct_id(),
                cartControllerDto.getShop_name(),
                cartControllerDto.getLon(),
                cartControllerDto.getLat());
        return cartService.getCart(token);
    }

    @PostMapping("/cart/delete")
    private List<ShopCart> deleteFromCart(@RequestHeader("Authorization") String token,
                                          @RequestBody CartControllerDto cartControllerDto) throws Exception {
        cartService.deleteFromCart(
                token,
                cartControllerDto.getProduct_id(),
                cartControllerDto.getShop_name(),
                cartControllerDto.getLon(),
                cartControllerDto.getLat());
        return cartService.getCart(token);
    }
}
