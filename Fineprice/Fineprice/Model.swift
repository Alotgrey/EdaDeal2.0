//
//  Model.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import Foundation

struct Product : Identifiable, Codable {
    var id : Int
    var name : String
    var description : String
    var prices : [String:Double]
}

class Model : Codable {
    var products : [Product]
    
    init(products: [Product]) {
        self.products = products
        self.testinit()
    }
    
    func testinit() {
        self.products.append(Product(id: 1, name: "Майонез", description: "Простой майонез", prices: ["Магнит": 75, "Лента": 95, "Пятерочка": 85, "Светофор": 65]))
        self.products.append(Product(id: 2, name: "Хлеб", description: "Белый хлеб", prices: ["Магнит": 30, "Лента": 35, "Пятерочка": 28, "Светофор": 32]))
        self.products.append(Product(id: 3, name: "Молоко", description: "Обезжиренное молоко", prices: ["Магнит": 50, "Лента": 55, "Пятерочка": 48, "Светофор": 52]))
        self.products.append(Product(id: 4, name: "Яйца", description: "Куриные яйца, 10 шт.", prices: ["Магнит": 70, "Лента": 75, "Пятерочка": 68, "Светофор": 72]))
        self.products.append(Product(id: 5, name: "Картошка", description: "Свежая картошка", prices: ["Магнит": 40, "Лента": 45, "Пятерочка": 38, "Светофор": 42]))
        self.products.append(Product(id: 6, name: "Сыр", description: "Гауда, 200 г", prices: ["Магнит": 120, "Лента": 130, "Пятерочка": 118, "Светофор": 125]))
        self.products.append(Product(id: 7, name: "Колбаса", description: "Вареная колбаса, 300 г", prices: ["Магнит": 180, "Лента": 190, "Пятерочка": 175, "Светофор": 185]))
        self.products.append(Product(id: 8, name: "Пельмени", description: "Сибирские пельмени, 500 г", prices: ["Магнит": 150, "Лента": 160, "Пятерочка": 145, "Светофор": 155]))
        self.products.append(Product(id: 9, name: "Макароны", description: "Спагетти, 500 г", prices: ["Магнит": 40, "Лента": 45, "Пятерочка": 38, "Светофор": 42]))
        self.products.append(Product(id: 10, name: "Оливковое масло", description: "Extra Virgin, 250 мл", prices: ["Магнит": 250, "Лента": 270, "Пятерочка": 245, "Светофор": 260]))
        self.products.append(Product(id: 11, name: "Куриное филе", description: "Свежее куриное филе, 1 кг", prices: ["Магнит": 250, "Лента": 270, "Пятерочка": 245, "Светофор": 260]))
            self.products.append(Product(id: 12, name: "Сок апельсиновый", description: "100% сок, 1 л", prices: ["Магнит": 90, "Лента": 95, "Пятерочка": 88, "Светофор": 92]))
            self.products.append(Product(id: 13, name: "Кофе молотый", description: "Арабика, 250 г", prices: ["Магнит": 120, "Лента": 130, "Пятерочка": 118, "Светофор": 125]))
            self.products.append(Product(id: 14, name: "Яблоки", description: "Сорт Голден, 1 кг", prices: ["Магнит": 80, "Лента": 85, "Пятерочка": 78, "Светофор": 82]))
            self.products.append(Product(id: 15, name: "Тунец консервированный", description: "В собственном соку, 200 г", prices: ["Магнит": 110, "Лента": 120, "Пятерочка": 108, "Светофор": 115]))
            self.products.append(Product(id: 16, name: "Мед натуральный", description: "Цветочный мед, 500 г", prices: ["Магнит": 180, "Лента": 190, "Пятерочка": 175, "Светофор": 185]))
            self.products.append(Product(id: 17, name: "Гречка", description: "Отборная гречка, 1 кг", prices: ["Магнит": 60, "Лента": 65, "Пятерочка": 58, "Светофор": 62]))
            self.products.append(Product(id: 18, name: "Творог", description: "5%, 400 г", prices: ["Магнит": 90, "Лента": 95, "Пятерочка": 88, "Светофор": 92]))
            self.products.append(Product(id: 19, name: "Шоколад", description: "Молочный шоколад, 100 г", prices: ["Магнит": 50, "Лента": 55, "Пятерочка": 48, "Светофор": 52]))
            self.products.append(Product(id: 20, name: "Газировка", description: "Кола, 1 л", prices: ["Магнит": 40, "Лента": 45, "Пятерочка": 38, "Светофор": 42]))
            // Добавьте еще продуктов по аналогии...
    }
}
