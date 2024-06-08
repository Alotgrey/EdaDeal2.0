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
import jakarta.persistence.EntityManager;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Predicate;
import jakarta.persistence.criteria.Root;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.PageRequest;
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
    private final EntityManager entityManager;

    public List<ProductDto> getAllProductsPage(int pageNo){
        PageRequest pageable = PageRequest.of(pageNo - 1, 10);
        return productRepository.findAll(pageable).stream().map(productMapper::toDto).toList();
    }

    public List<ProductDto> searchProductsByKeywords(String keywords, int pageNo){
        String[] keywordArray = keywords.toLowerCase().split("\\s+");
        CriteriaBuilder cb = entityManager.getCriteriaBuilder();
        CriteriaQuery<Product> query = cb.createQuery(Product.class);
        Root<Product> root = query.from(Product.class);
        List<Predicate> predicates = new ArrayList<>();
        for (String keyword : keywordArray) {
            Predicate predicate = cb.or(
                    cb.like(cb.lower(root.get("name")), "%" + keyword + "%")
            );
            predicates.add(predicate);
        }
        Predicate finalPredicate = cb.and(predicates.toArray(new Predicate[0]));
        query.where(finalPredicate);
        List<Product> allProducts = entityManager.createQuery(query).getResultList();
        return allProducts
                .stream()
                .map(productMapper::toDto)
                .toList()
                .subList( (pageNo - 1) * 10
                        , Integer.min( (pageNo - 1) * 10 + 10
                                     , allProducts.size()));
    }

    public List<ProductDto> getAllProductsFromCategory(Long category_id, int pageNo){
        List<Product> products = new ArrayList<>();
        Category category = getCategoryById(category_id);
        if (category.getIsFinal()){
            products = productRepository.findProductsByCategory_Id(category_id);
        }
        else {
            List<Category> children = categoryRepository.findCategoriesByParent_Id(category_id);
            for (Category child : children){
                products.addAll(productRepository.findProductsByCategory_Id(child.getId()));
            }
        }

        return products
                .stream()
                .map(productMapper::toDto)
                .toList()
                .subList((pageNo - 1) * 10, Integer.min((pageNo - 1) * 10 + 10, products.size()));
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
}
