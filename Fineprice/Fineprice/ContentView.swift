//
//  ContentView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct ContentView: View {
    @State var model = Model(products: [])
    @State var searchText = ""
    
    var filteredProducts : [Product] {
        guard !searchText.isEmpty else { return model.products }
        return model.products.filter { $0.name.localizedCaseInsensitiveContains(searchText) }
    }
    
    var body: some View {
        TabView {
            NavigationStack {
                Text("1")
            }.tabItem {
                Image(systemName: "house")
                Text("Домашняя") }
            NavigationStack {
                List (filteredProducts) { product in
                    NavigationLink(destination: DetailView(product: product), label: { Text("\(product.name)") }
                     )
                }.searchable(text: $searchText, placement: .automatic, prompt: "Найти по названию")
            }.tabItem {
                Image(systemName: "magnifyingglass")
                Text("Finder") }
            NavigationStack {
                Text("3")
            }.tabItem {
                Image(systemName: "cart")
                Text("Корзина") }
        }
    }
}

#Preview {
    ContentView()
}
