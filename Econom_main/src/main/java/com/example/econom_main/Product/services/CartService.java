package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CartItem;
import com.example.econom_main.Product.entities.cart.SessionCart;
import com.example.econom_main.Product.entities.cart.ShopCart;
import com.example.econom_main.Product.entities.product_cost.ProductCost;
import com.example.econom_main.Product.entities.product_cost.ShopCost;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.*;

@Service
@RequiredArgsConstructor
public class CartService {
    private final ProductCostService productCostService;
    public ShopCart getCart(HttpSession session) throws IOException {
        SessionCart cart = (SessionCart) session.getAttribute("cart");
        if (cart == null){
            cart = new SessionCart();
            session.setAttribute("cart", cart);
        }
        return cart.getMostProfitableCart();
    }

    public void addToCart(HttpSession session, Long product_id) throws IOException {
        SessionCart cart = (SessionCart) session.getAttribute("cart");
        if (cart == null){
            cart = new SessionCart();
        }
        ProductCost productCost = productCostService.getProductCostById(product_id);
        List<ShopCost> shopCostList = productCost.priceList;
        for (ShopCost shopCost : shopCostList){
            cart.addCartItem(new CartItem(product_id, productCost.name, productCost.image_url, shopCost, 1L));
        }
        cart.addCartItem(new CartItem(product_id, productCost.name, productCost.image_url, productCost.best_cost,1L));
        session.setAttribute("cart", cart);
    }

    public void deleteFromCart(HttpSession session, Long product_id) throws IOException {
        SessionCart cart = (SessionCart) session.getAttribute("cart");
        if (cart == null){
            cart = new SessionCart();
            session.setAttribute("cart", cart);
            return;
        }
        cart.deleteCartItem(product_id);


    }

}
