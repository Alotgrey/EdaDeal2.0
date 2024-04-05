package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.dtos.ProductDto;
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
        return categoryRepository.findAll();
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

    public void addNewCategory(CategoryDto categoryDto){
        Category category = new Category();
        category.setName(categoryDto.getName());
        category.setImage_url(categoryDto.getImage_url());
        category.setIsFinal(categoryDto.getIsFinal());
        category.setParent(categoryRepository.getById(categoryDto.getParent_id()));
        categoryRepository.save(category);
    }
    public List<Product> getAllProducts(){
        return productRepository.findAll();
    }

    public List<Product> getAllProductsFromCategory(Long category_id){
        return productRepository.findProductsByCategory_Id(category_id);
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

    public void addNewProduct(ProductDto productDto){
        Product product = new Product();
        product.setName(productDto.getName());
        product.setImage_url(productDto.getImage_url());
        product.setCategory(categoryRepository.getById(productDto.getId()));
        product.setLink_crossroad(productDto.getLink_crossroad());
        product.setLink_5ka(productDto.getLink_5ka());
        product.setLink_lenta(productDto.getLink_lenta());
        product.setLink_magnit(productDto.getLink_magnit());
        product.setLink_metro(productDto.getLink_metro());
        productRepository.save(product);
    }
}
