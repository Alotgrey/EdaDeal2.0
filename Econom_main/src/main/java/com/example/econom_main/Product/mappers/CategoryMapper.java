package com.example.econom_main.Product.mappers;

import com.example.econom_main.Product.dtos.CategoryDto;
import com.example.econom_main.Product.dtos.CategoryListDto;
import com.example.econom_main.Product.entities.Category;
import com.example.econom_main.Product.repositories.CategoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
@Component
@RequiredArgsConstructor
public class CategoryMapper {
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
        categoryDto.setId(category.getId());
        categoryDto.setName(category.getName());
        categoryDto.setImage_url(category.getImage_url());
        categoryDto.setIsFinal(category.getIsFinal());
        Category parent = category.getParent();
        if (null != parent){
            categoryDto.setParent_id(parent.getId());
        }
        else{
            categoryDto.setParent_id(0L);
        }
        return categoryDto;
    }

    public CategoryListDto listGenerator(Category category) {
        CategoryListDto categoryListDto = new CategoryListDto();
        categoryListDto.setId(category.getId());
        categoryListDto.setName(category.getName());
        categoryListDto.setImage_url(category.getImage_url());
        categoryListDto.setIsFinal(category.getIsFinal());
        categoryListDto.setChildren(new ArrayList<>());
        if (!categoryListDto.getIsFinal()){
            List<Category> categories = categoryRepository.findCategoriesByParent_Id(category.getId());
            for (Category c : categories){
                categoryListDto.getChildren().add(listGenerator(c));
            }
        }
        return categoryListDto;
    }
}
