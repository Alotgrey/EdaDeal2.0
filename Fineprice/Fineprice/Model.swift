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

class Model : ObservableObject {
    @Published var products : [Product]
    @Published var shoppingCart : [Product]
    //@Published var searchProducts : [Product]
    
    init() {
        self.products = []
        self.shoppingCart = []
        Task {
            await jsonInit()
        }
    }
    
//    func getImage(string : String) async -> UIImage {
//        if let url = URL(string: string), let (data, _) = try? await URLSession.shared.data(from: url) {
//            return UIImage(data: data) ?? UIImage(resource: .noimg)
//        }
//        else {
//            return UIImage(resource: .noimg)
//        }
//    }
    
    func jsonInitLOCAL() {
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

    func jsonInit() async {
        if let url = URL(string: "https://run.mocky.io/v3/eb7c3125-8885-40a5-897d-52162bfb08ea") {
            do {
                let (data, _) = try await URLSession.shared.data(from: url)
                self.products = try JSONDecoder().decode([Product].self, from: data)
            }
            catch {
                print("Error fetching data")
            }
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
    }
}
