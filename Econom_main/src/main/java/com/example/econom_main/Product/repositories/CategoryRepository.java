package com.example.econom_main.Product.repositories;

import com.example.econom_main.Product.entities.Category;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CategoryRepository extends JpaRepository<Category, Long> {
    List<Category> findCategoriesByParent_Id(Long id);
}
