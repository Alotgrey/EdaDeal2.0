//
//  DetailView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct DetailView: View {
    var product : Product
    var body: some View {
        NavigationStack {
            Text(product.name)
            Text(product.description)
            List {
                ForEach(product.prices.sorted(by: { $0.key < $1.key }), id: \.key) { (shop, price) in
                    Text("\(shop) - \(price)")
                }
            }.listStyle(.inset)
            Button(action: { }, label: {
                Text("В корзину")
            }).padding()
                .background(Color.green)
                .foregroundColor(.white)
                .clipShape(Capsule())
        }
    }
}

#Preview {
    DetailView(product: Product(id: 1, name: "Test", description: "Testing descr", prices: ["Магнит": 75, "Лента": 95, "Пятерочка": 85, "Светофор": 65]))
}
