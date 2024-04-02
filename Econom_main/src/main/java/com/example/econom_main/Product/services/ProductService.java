package com.example.econom_main.Product.services;

import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.entities.Product;
import com.example.econom_main.Product.repositories.CategoryRepository;
import com.example.econom_main.Product.repositories.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductRepository productRepository;
    private final CategoryRepository categoryRepository;

    public List<Category> getAllCategories() {
        return (List<Category>) categoryRepository.findAll();
    }

    public Category getCategoryById(Long id){
        Optional<Category> optionalCategory = categoryRepository.findById(id);
        Category category = null;
        if (optionalCategory.isPresent()){
            category = optionalCategory.get();
        }
        else{
            throw new RuntimeException("Category not found for id: " + id);
        }
        return category;
    }

    public void addNewCategory(Category category){
        categoryRepository.save(category);
    }
    public List<Product> getAllProducts(){
        return (List<Product>) productRepository.findAll();
    }

    public List<Product> getAllProductsFromCategory(Long category_id){
        return (List<Product>) productRepository.findProductByCategory_Id(category_id);
    }

    public Product getProductById(Long id){
        Optional<Product> optionalProduct = productRepository.findById(id);
        Product product = null;
        if (optionalProduct.isPresent()){
            product = optionalProduct.get();
        }
        else{
            throw new RuntimeException("Product not found for id: " + id);
        }
        return product;
    }

    public void addNewProduct(Product product){
        productRepository.save(product);
    }
}
