//
//  ContentView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct ContentView: View {
    @ObservedObject var model = Model()
    
    var body: some View {
        TabView {
            MainPageView(model: model).tabItem {
                Image(systemName: "house")
                Text("Домашняя") }
            SearchView(model: model).tabItem {
                Image(systemName: "magnifyingglass")
                Text("Поиск") }
            CategoryView(model: model).tabItem {
                Image(systemName: "square.grid.3x3.fill")
                Text("Категории") }
            CartView(shoppingCart: $model.shoppingCart).tabItem {
                Image(systemName: "cart")
                Text("Корзина") }
        }
    }
}

#Preview {
    ContentView()
}
