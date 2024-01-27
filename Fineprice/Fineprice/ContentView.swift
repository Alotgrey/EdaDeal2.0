//
//  ContentView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct ContentView: View {
    @State var model = Model()
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
                ScrollView {
                    LazyVGrid(columns:
                                [GridItem(.adaptive(minimum: 150), spacing: 15)],
                              spacing: 15) {
                        ForEach(filteredProducts, id: \.id) { product in
                                    NavigationLink(destination: DetailView(product: product))
                                    {
                                        VStack {
                                            Text("\(product.name)")
                                                .foregroundStyle(Color.black)
                                                .fontWeight(.bold)
                                                .lineLimit(1)
                                            Image(uiImage: getImage(string: product.selectedShop.urlImage))
                                                .resizable()
                                                .aspectRatio(contentMode: .fit)
                                                .frame(width: 130)
                                                .clipShape(RoundedRectangle(cornerRadius: 20))
                                            Button(action: {
                                                UIApplication.shared.open(URL(string: product.selectedShop.url)!)
                                            }) {
//                                                Text("\(String(format: "%.2f", product.selectedShop.price)) руб")
                                                Text(product.selectedShop.price)
                                                    .fontWeight(.semibold)
                                            }.padding(.horizontal, 20)
                                                .padding(.vertical, 10)
                                                .foregroundStyle(Color.white)
                                                .background(.darkPinkie)
                                                .clipShape(Capsule())
                                        }
                                    }
                                }.padding(20)
                            .background(.pinkieElem)
                                .clipShape(RoundedRectangle(cornerRadius: 20))
                            }
                            .padding(15)
                            
                        }.searchable(text: $searchText, placement: .automatic, prompt: "Найти по названию")
            }.tabItem {
                Image(systemName: "magnifyingglass")
                Text("Поиск") }
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
