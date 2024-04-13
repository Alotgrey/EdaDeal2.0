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



class Model : ObservableObject, Codable {
    @Published var searchProducts : [Product]
    @Published var categoryProducts : [Product]
    @Published var shoppingCart : [String : [Product]] {
        didSet {
            let defaults = UserDefaults.standard
            let encoder = JSONEncoder()
            if let m = try? encoder.encode(self) {
                defaults.set(m, forKey: "model")
            }
        }
    }
    
    private enum CodingKeys: String, CodingKey {
            case searchProducts, categoryProducts, shoppingCart
    }
    
    public func encode(to encoder: Encoder) throws {
            var values = encoder.container(keyedBy: CodingKeys.self)
            try values.encode(searchProducts, forKey: .searchProducts)
            try values.encode(categoryProducts, forKey: .categoryProducts)
            try values.encode(shoppingCart, forKey: .shoppingCart)
    }
    
    required init(from decoder: any Decoder) throws {
        let values = try decoder.container(keyedBy: CodingKeys.self)
        searchProducts = try values.decode([Product].self, forKey: .searchProducts)
        categoryProducts = try values.decode([Product].self, forKey: .categoryProducts)
        shoppingCart = try values.decode([String : [Product]].self, forKey: .shoppingCart)
    }
    
    
    init() {
        let defaults = UserDefaults.standard
        if let data = defaults.object(forKey: "model") as? Data,
           let model = try? JSONDecoder().decode(Model.self, from: data) {
            self.searchProducts = model.searchProducts
            self.categoryProducts = model.categoryProducts
            self.shoppingCart = model.shoppingCart
            //self.shoppingCart = ["Magnit": [], "Pyatorochka" : []]
        }
        else {
            print("Bad init")
            self.searchProducts = []
            self.categoryProducts = []
            self.shoppingCart = ["Magnit": [], "Pyatorochka" : []]
            
        }
        
        //self.jsonInitLOCAL()
//        Task {
//            await jsonInit()
//        }
    }
    
//    func getImage(string : String) async -> UIImage {
//        if let url = URL(string: string), let (data, _) = try? await URLSession.shared.data(from: url) {
//            return UIImage(data: data) ?? UIImage(resource: .noimg)
//        }
//        else {
//            return UIImage(resource: .noimg)
//        }
//    }
//    func addToShoppingCart(product: Product, shop: String) {
//        shoppingCart[shop]?.append(product)
//    }
    
    func jsonInitLOCAL() {
        if let path = Bundle.main.url(forResource: "merged", withExtension: "json") {
            do {
                let data = try Data(contentsOf: path)
                searchProducts = try JSONDecoder().decode([Product].self, from: data)
                categoryProducts = try JSONDecoder().decode([Product].self, from: data)
            }
            catch {
                print("Error loading JSON: \(error)")
            }
        }
        else {
            print("File not found")
        }
    }

    func searchInit() async {
        if let url = URL(string: "https://run.mocky.io/v3/37c404b2-90fa-4b19-aa10-2e2e7fffe32b") {
            do {
                let (data, _) = try await URLSession.shared.data(from: url)
                DispatchQueue.main.async {
                    do {
                        self.searchProducts = try JSONDecoder().decode([Product].self, from: data)
                    }
                    catch {
                        print("Error parsing JSON from WEB")
                    }
                }
                
            }
            catch {
                print("Error fetching data")
            }
        }
    }
    
    func categoriesInit() async {
        if let url = URL(string: "https://run.mocky.io/v3/37c404b2-90fa-4b19-aa10-2e2e7fffe32b") {
            do {
                let (data, _) = try await URLSession.shared.data(from: url)
                DispatchQueue.main.async {
                    do {
                        self.categoryProducts = try JSONDecoder().decode([Product].self, from: data)
                    }
                    catch {
                        print("Error parsing JSON from WEB")
                    }
                }
                
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
