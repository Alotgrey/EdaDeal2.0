//
//  SearchView.swift
//  Fineprice
//
//  Created by Кирилл Архипов on 06.04.2024.
//

import SwiftUI

struct SearchView: View {
    @ObservedObject var model : Model
    
    @State var searchText = ""
    //Реализация поиска
    var filteredProducts : [Product] {
        guard !searchText.isEmpty else { return model.searchProducts }
        return model.searchProducts.filter { $0.name.localizedCaseInsensitiveContains(searchText) }
    }
    
    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns:
                            [GridItem(.adaptive(minimum: 150), spacing: 15)],
                          spacing: 15) {
                    ForEach(filteredProducts, id: \.id) { product in
                        NavigationLink(destination: DetailView(product: product, model: model))
                                {
                                    VStack {
                                        Text("\(product.name)")
                                            .foregroundStyle(Color.black)
                                            .fontWeight(.bold)
                                            .lineLimit(1)
                                        AsyncImage(url: URL(string: product.selectedShop.urlImage)) { image in
                                            image
                                                .resizable()
                                                .aspectRatio(contentMode: .fit)
                                                .clipShape(RoundedRectangle(cornerRadius: 20))
                                        } placeholder: {
                                            Image("noimg")
                                                .resizable()
                                                .aspectRatio(contentMode: .fit)
                                                .clipShape(RoundedRectangle(cornerRadius: 20))
                                        }.frame(width: 130)
                                        Button(action: {
                                            UIApplication.shared.open(URL(string: product.selectedShop.url)!)
                                        }) {
//                                                Text("\(String(format: "%.2f", product.selectedShop.price)) руб")
                                            Text(product.selectedShop.price)
                                                .fontWeight(.semibold)
                                        }.padding(.horizontal, 20)
                                            .padding(.vertical, 10)
                                            .foregroundStyle(Color.black)
                                            .background(.darkPinkie)
                                            .clipShape(Capsule())
                                    }.padding(20)
                                    .background(.pinkieElem)
                                    .clipShape(RoundedRectangle(cornerRadius: 20))
                                    //.fixedSize(horizontal: false, vertical: true)
                                    
                                }
                            }
                            
                        }
                        .padding(20)
            }.searchable(text: $searchText, placement: .automatic, prompt: "Найти по названию")
                .onAppear {
                    Task {
                        await model.searchInit()
                    }
                }
                
        }
    }
}

#Preview {
    SearchView(model: Model())
}
