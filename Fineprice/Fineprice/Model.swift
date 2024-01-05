//
//  Model.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import Foundation


struct Shop : Codable {
    var price : Double
    var name : String
    var logoUrl : String
    var url : String
}

struct Product : Codable, Identifiable {
    var id : Int
    var name : String
    var description : String
    var shops : [Shop]
    var selectedShop : Shop
    var urlImage : String
}

class Model : Codable {
    var products : [Product]
    var shoppingCart : [Product]
    
    init() {
        self.products = []
        self.shoppingCart = []
        self.testinit()
    }
    
    func testinit() {
        self.products.append(
            Product(id: 1,
                    name: "Майонез", 
                    description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
                    shops: [Shop(price: 75, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                             Shop(price: 95, name: "Лента", logoUrl: "logo2",url: "URLtemplate2"),
                             Shop(price: 85, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                             Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")],
                    selectedShop: Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4"),
                    urlImage: "product"))
        self.products.append(
            Product(
                id: 2,
                name: "Хлеб",
                description: "Белый хлеб",
                shops: [
                    Shop(price: 30, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 35, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 28, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 32, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 28, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 3,
                name: "Молоко",
                description: "Обезжиренное молоко",
                shops: [
                    Shop(price: 50, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 55, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 52, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 4,
                name: "Яйца",
                description: "Куриные яйца, 10 шт.",
                shops: [
                    Shop(price: 70, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 75, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 68, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 72, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 68, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 5,
                name: "Картошка",
                description: "Свежая картошка",
                shops: [
                    Shop(price: 40, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 45, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 42, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 6,
                name: "Сыр",
                description: "Гауда, 200 г",
                shops: [
                    Shop(price: 120, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 130, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 118, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 125, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 118, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 7,
                name: "Колбаса",
                description: "Вареная колбаса, 300 г",
                shops: [
                    Shop(price: 180, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 190, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 175, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 185, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 175, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 8,
                name: "Пельмени",
                description: "Сибирские пельмени, 500 г",
                shops: [
                    Shop(price: 150, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 160, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 145, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 155, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 145, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 9,
                name: "Макароны",
                description: "Спагетти, 500 г",
                shops: [
                    Shop(price: 40, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 45, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 42, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 10,
                name: "Оливковое масло",
                description: "Extra Virgin, 250 мл",
                shops: [
                    Shop(price: 250, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 270, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 245, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 260, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 245, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 11,
                name: "Куриное филе",
                description: "Свежее куриное филе, 1 кг",
                shops: [
                    Shop(price: 250, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 270, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 245, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 260, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 245, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 12,
                name: "Сок апельсиновый",
                description: "100% сок, 1 л",
                shops: [
                    Shop(price: 90, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 95, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 88, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 92, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 88, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 13,
                name: "Кофе молотый",
                description: "Арабика, 250 г",
                shops: [
                    Shop(price: 120, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 130, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 118, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 125, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 118, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 14,
                name: "Яблоки",
                description: "Сорт Голден, 1 кг",
                shops: [
                    Shop(price: 80, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 85, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 78, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 82, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 78, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 15,
                name: "Тунец консервированный",
                description: "В собственном соку, 200 г",
                shops: [
                    Shop(price: 110, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 120, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 108, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 115, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 108, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 16,
                name: "Мед натуральный",
                description: "Цветочный мед, 500 г",
                shops: [
                    Shop(price: 180, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 190, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 175, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 185, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 175, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 17,
                name: "Гречка",
                description: "Отборная гречка, 1 кг",
                shops: [
                    Shop(price: 60, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 65, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 58, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 62, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 58, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 18,
                name: "Творог",
                description: "5%, 400 г",
                shops: [
                    Shop(price: 90, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 95, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 88, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 92, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 88, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 19,
                name: "Шоколад",
                description: "Молочный шоколад, 100 г",
                shops: [
                    Shop(price: 50, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 55, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 52, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

        self.products.append(
            Product(
                id: 20,
                name: "Газировка",
                description: "Кола, 1 л",
                shops: [
                    Shop(price: 40, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                    Shop(price: 45, name: "Лента", logoUrl: "logo2", url: "URLtemplate2"),
                    Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                    Shop(price: 42, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")
                ],
                selectedShop: Shop(price: 38, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                urlImage: "product"
            )
        )

    }
}
