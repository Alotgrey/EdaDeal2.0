package com.example.econom_main.product_package;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
@Service
public class ProductService {
    @Autowired
    ProductRepository productRepository;

    public List<Product> getAllProducts(){
        return (List<Product>) productRepository.findAll();
    }

    public Product getProductById(Long id){
        Optional<Product> optionalProduct = this.productRepository.findById(id);
        Product product = null;
        if (optionalProduct.isPresent()){
            product = optionalProduct.get();
        }
        else{
            throw new RuntimeException("Note not found for id: " + id);
        }
        return product;
    }

    public void addNewProduct(Product product){
        this.productRepository.save(product);
    }
}
