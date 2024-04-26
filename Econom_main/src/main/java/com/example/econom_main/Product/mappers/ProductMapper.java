package com.example.econom_main.Product.mappers;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.entities.Product;
import com.example.econom_main.Product.repositories.CategoryRepository;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
@AllArgsConstructor
public class ProductMapper {

    private final CategoryRepository categoryRepository;

    public Product toProduct(ProductDto productDto){
        Product product = new Product();
        product.setName(productDto.getName());
        product.setImage_url(productDto.getImage_url());
        Optional<Category> optionalCategory = categoryRepository.findById(productDto.getCategory_id());
        optionalCategory.ifPresent(product::setCategory);
        product.setLink(productDto.getLink());
        return product;
    }

    public ProductDto toDto(Product product){
        ProductDto productDto = new ProductDto();
        productDto.setId(product.getId());
        productDto.setName(product.getName());
        productDto.setImage_url(product.getImage_url());
        productDto.setCategory_id(product.getCategory().getId());
        productDto.setLink(product.getLink());
        return productDto;
    }
}
