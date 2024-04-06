package com.example.econom_main.Product.mappers;
import com.example.econom_main.Product.dtos.ProductDto;
import com.example.econom_main.Product.entities.Product;
import com.example.econom_main.Product.repositories.CategoryRepository;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class ProductMapper {
    @Autowired
    private final CategoryRepository categoryRepository;

    public Product toProduct(ProductDto productDto){
        Product product = new Product();
        product.setName(productDto.getName());
        product.setImage_url(productDto.getImage_url());
        product.setCategory(categoryRepository.getById(productDto.getCategory_id()));
        product.setLink_crossroad(productDto.getLink_crossroad());
        product.setLink_5ka(productDto.getLink_5ka());
        product.setLink_lenta(productDto.getLink_lenta());
        product.setLink_magnit(productDto.getLink_magnit());
        product.setLink_metro(productDto.getLink_metro());
        return product;
    }

    public ProductDto toDto(Product product){
        ProductDto productDto = new ProductDto();
        productDto.setName(product.getName());
        productDto.setImage_url(product.getImage_url());
        productDto.setCategory_id(product.getCategory().getId());
        productDto.setLink_magnit(product.getLink_magnit());
        productDto.setLink_crossroad(product.getLink_crossroad());
        productDto.setLink_lenta(product.getLink_lenta());
        productDto.setLink_5ka(productDto.getLink_5ka());
        productDto.setLink_metro(product.getLink_metro());
        return productDto;
    }
}
