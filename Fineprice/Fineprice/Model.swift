//
//  Model.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import Foundation
import UIKit

struct Shop : Codable {
    var price : String //Double
    var name : String
    var logoUrl : String
    var url : String
	var urlImage : String
}

struct Product : Codable, Identifiable {
    var id : Int
    var name : String
    var description : String
    var shops : [Shop]
    var selectedShop : Shop
}



class Model : Codable {
    var products : [Product]
    var shoppingCart : [Product]
    
    init() {
        self.products = []
        self.shoppingCart = []
        self.jsonInit()
    }
    
//    func getImage(string : String) async -> UIImage {
//        if let url = URL(string: string), let (data, _) = try? await URLSession.shared.data(from: url) {
//            return UIImage(data: data) ?? UIImage(resource: .noimg)
//        }
//        else {
//            return UIImage(resource: .noimg)
//        }
//    }
    
    func jsonInit() {
        if let path = Bundle.main.url(forResource: "merged", withExtension: "json") {
            do {
                let data = try Data(contentsOf: path)
                products = try JSONDecoder().decode([Product].self, from: data)
            }
            catch {
                print("Error loading JSON: \(error)")
            }
        }
        else {
            print("File not found")
        }
    }
    
    func testInit() {
//        self.products.append(
//            Product(id: 1,
//                    name: "Майонез", 
//                    description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
//                    shops: [Shop(price: 75, name: "Магнит", logoUrl: "logo1", url: "https://vk.com/keril1", urlImage: "product"),
//                             Shop(price: 95, name: "Лента", logoUrl: "logo2",url: "https://vk.com/keril1", urlImage: "product"),
//                             Shop(price: 85, name: "Пятерочка", logoUrl: "logo3", url: "https://vk.com/keril1", urlImage: "product"),
//                             Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "https://vk.com/keril1", urlImage: "product")],
//                    selectedShop: Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "https://vk.com/keril1", urlImage: "product")))
//        self.products.append(
//            Product(
//                id: 2,
//                name: "Хлеб",
//                description: "Белый хлеб",
//                shops: [
//                    Shop(price: 30, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1", urlImage: "product"),
//                    Shop(price: 35, name: "Лента", logoUrl: "logo2", url: "URLtemplate2", urlImage: "product"),
//                    Shop(price: 28, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product"),
//                    Shop(price: 32, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4", urlImage: "product")
//                ],
//                selectedShop: Shop(price: 28, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product"))
//        )
//
//        self.products.append(
//            Product(
//                id: 3,
//                name: "Молоко",
//                description: "Обезжиренное молоко",
//                shops: [
//                    Shop(price: 50, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1", urlImage: "product"),
//                    Shop(price: 55, name: "Лента", logoUrl: "logo2", url: "URLtemplate2", urlImage: "product"),
//                    Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product"),
//                    Shop(price: 52, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4", urlImage: "product")
//                ],
//                selectedShop: Shop(price: 48, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product"))
//        )
//
//        self.products.append(
//            Product(
//                id: 4,
//                name: "Яйца",
//                description: "Куриные яйца, 10 шт.",
//                shops: [
//                    Shop(price: 70, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1", urlImage: "product"),
//                    Shop(price: 75, name: "Лента", logoUrl: "logo2", url: "URLtemplate2", urlImage: "product"),
//                    Shop(price: 68, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product"),
//                    Shop(price: 72, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4", urlImage: "product")
//                ],
//                selectedShop: Shop(price: 68, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3", urlImage: "product")
//            )
//        )

    }
}
