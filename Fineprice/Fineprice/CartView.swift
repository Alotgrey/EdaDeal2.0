//
//  CartView.swift
//  Fineprice
//
//  Created by Кирилл Архипов on 30.03.2024.
//

import SwiftUI

struct CartView: View {
    @Binding var shoppingCart : [String:[Product]]
    
    var body: some View {
        VStack {
            List {
                ForEach (shoppingCart.sorted(by: { $0.key < $1.key }), id: \.key) { shop, products in
                    Section(header: Text(shop)) {
                        ForEach(products, id: \.id) { product in
                            HStack {
                                Text(product.name)
                                    .lineLimit(1)
                                Spacer()
                                Text(product.selectedShop.price)
                                Button(action: {
                                    if let url = URL(string: product.selectedShop.url) {
                                        UIApplication.shared.open(url)
                                    }
                                }) {
                                    Text("В магазин")
                                }
                            }
                        }
                        //Text("Итого: \(shoppingCart)" )
                    }
                }
            }
            Button(action: {
                shoppingCart.forEach { shop, _ in
                    shoppingCart[shop] = [Product(id: 99, name: "Итог: ", description: "", shops: [], selectedShop: Shop(price: "\(0)", name: "", logoUrl: "", url: "", urlImage: ""))]
                }
            }) {
                Text("Очистить корзины")
            }
        }
    }
}

#Preview {
    CartView(shoppingCart: .constant(["sss": [Product(id: 1,
                                 name: "Майонез",
                                 description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
                                 shops: [Shop(price: "75000", name: "Магнит", logoUrl: "magnitLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                         Shop(price: "95", name: "Лента", logoUrl: "lentaLogo",url: "https://vk.com/keril1", urlImage: "product"),
                                         Shop(price: "85", name: "Пятерочка", logoUrl: "pyatLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                         Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")],
                                 selectedShop: Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")
                 )]]))
}
