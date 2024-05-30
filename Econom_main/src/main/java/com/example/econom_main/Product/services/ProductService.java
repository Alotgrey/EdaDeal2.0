package com.example.econom_main.Product.services;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.entities.product_cost.Product;
import com.example.econom_main.Product.mappers.CategoryMapper;
import com.example.econom_main.Product.mappers.ProductMapper;
import com.example.econom_main.Product.repositories.CategoryRepository;
import com.example.econom_main.Product.repositories.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductRepository productRepository;
    private final CategoryRepository categoryRepository;
    private final CategoryMapper categoryMapper;
    private final ProductMapper productMapper;

    public List<CategoryDto> getAllCategories() {
        return categoryRepository.findAll().stream().map(categoryMapper::toDto).toList();
    }

    public List<ProductDto> getAllProducts(){
        return productRepository.findAll().stream().map(productMapper::toDto).toList().subList(0, 10);
    }

    public List<Category> getAllCategoriesByParentId(Long id){
        return categoryRepository.findCategoriesByParent_Id(id);
    }

    public List<Product> getAllProductsFromCategory(Long category_id){
        List<Product> products = new ArrayList<>();
        Category category = categoryRepository.findById(category_id).get();
        if (category.getIsFinal()){
            products = productRepository.findProductsByCategory_Id(category_id);
        }
        else {
            List<Category> children = categoryRepository.findCategoriesByParent_Id(category_id);
            for (Category child : children){
                products.addAll(productRepository.findProductsByCategory_Id(child.getId()));
            }
        }
        return products.subList(0, 10);
    }

    public Category getCategoryById(Long id){
        Optional<Category> optionalCategory = categoryRepository.findById(id);
        Category category = null;
        if (optionalCategory.isPresent()){
            category = optionalCategory.get();
        }
        return category;
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

    public CategoryListDto getCategoryListDtoById(Long id){
        return categoryMapper.listGenerator(this.getCategoryById(id));
    }

    public void addNewCategory(CategoryDto categoryDto){
        categoryRepository.save(categoryMapper.toCategory(categoryDto));
    }

    public void addNewProduct(ProductDto productDto){
        productRepository.save(productMapper.toProduct(productDto));
    }
}
