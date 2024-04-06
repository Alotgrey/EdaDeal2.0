package com.example.econom_main.Product.mappers;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.repositories.CategoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Optional;
@Component
@RequiredArgsConstructor
public class CategoryMapper {
    @Autowired
    private final CategoryRepository categoryRepository;
    public Category toCategory(CategoryDto categoryDto){
        Category category = new Category();
        category.setName(categoryDto.getName());
        category.setImage_url(categoryDto.getImage_url());
        category.setIsFinal(categoryDto.getIsFinal());

        Optional<Category> optionalCategory = categoryRepository.findById(categoryDto.getParent_id());
        Category parent = null;
        if (optionalCategory.isPresent()){
            parent = optionalCategory.get();
        }
        category.setParent(parent);
        return category;
    }

    public CategoryDto toDto(Category category){
        CategoryDto categoryDto = new CategoryDto();
        categoryDto.setName(category.getName());
        categoryDto.setImage_url(category.getImage_url());
        categoryDto.setIsFinal(category.getIsFinal());
        categoryDto.setParent_id(category.getParent().getId());
        return categoryDto;
    }
}
