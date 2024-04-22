package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CartItem;
import com.example.econom_main.Product.entities.ProductCost;
import com.example.econom_main.Product.entities.ShopCost;
import com.example.econom_main.Product.entities.ShoppingCart;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.*;

@Service
@RequiredArgsConstructor
public class CartService {
    private final ProductCostService productCostService;
    public List<List<CartItem>> getCart(HttpSession session) throws IOException {
        ShoppingCart cart = (ShoppingCart) session.getAttribute("cart");
        if (cart == null){
            cart = new ShoppingCart();
            session.setAttribute("cart", cart);
        }
        List<List<CartItem>> cartList = new ArrayList<>();
        for (int i  = 0; i < 5; i++){
            cartList.add(new ArrayList<>());
        }
        if (cart.getCart() != null) {
            for (Long id : cart.getCart().descendingKeySet()) {
                ProductCost productCost = productCostService.getProductCostById(id);
                for (ShopCost shopCost : cart.getCart().get(id).keySet()) {
                    if (Objects.equals(shopCost.getEn_name(), "magnit")) {
                        cartList.get(0).add(new CartItem(id, productCost.getName(), shopCost.getCost(), cart.getCart().get(id).get(shopCost)));
                    } else if (Objects.equals(shopCost.getEn_name(), "5ka")) {
                        cartList.get(1).add(new CartItem(id, productCost.getName(), shopCost.getCost(), cart.getCart().get(id).get(shopCost)));
                    } else if (Objects.equals(shopCost.getEn_name(), "crossroad")) {
                        cartList.get(2).add(new CartItem(id, productCost.getName(), shopCost.getCost(), cart.getCart().get(id).get(shopCost)));
                    } else if (Objects.equals(shopCost.getEn_name(), "lenta")) {
                        cartList.get(3).add(new CartItem(id, productCost.getName(), shopCost.getCost(), cart.getCart().get(id).get(shopCost)));
                    } else if (Objects.equals(shopCost.getEn_name(), "metro")) {
                        cartList.get(4).add(new CartItem(id, productCost.getName(), shopCost.getCost(), cart.getCart().get(id).get(shopCost)));
                    }
                }
            }
        }
        return cartList;
    }

    public void addToCart(HttpSession session, Long product_id, String shopName) throws IOException {
        ShoppingCart cart = (ShoppingCart) session.getAttribute("cart");
        if (cart == null){
            cart = new ShoppingCart();
        }
        ProductCost productCost = productCostService.getProductCostById(product_id);
        List<ShopCost> shopCostList = productCost.getPriceList();
        for (ShopCost shopCost : shopCostList){
            if (Objects.equals(shopCost.getEn_name(), shopName)){
                cart.addProduct(product_id, shopCost);
                break;
            }
        }
        if (Objects.equals(productCost.getBest_cost().getEn_name(), shopName)){
            cart.addProduct(product_id, productCost.getBest_cost());
        }
        session.setAttribute("cart", cart);
    }

    public void deleteFromCart(HttpSession session, Long product_id, String shopName) throws IOException {
        ShoppingCart cart = (ShoppingCart) session.getAttribute("cart");
        if (cart == null){
            cart = new ShoppingCart();
        }
        ProductCost productCost = productCostService.getProductCostById(product_id);
        List<ShopCost> shopCostList = productCost.getPriceList();
        for (ShopCost shopCost : shopCostList){
            if (Objects.equals(shopCost.getEn_name(), shopName)){
                cart.deleteProduct(product_id, shopCost);
                break;
            }
        }
        session.setAttribute("cart", cart);
    }

}
