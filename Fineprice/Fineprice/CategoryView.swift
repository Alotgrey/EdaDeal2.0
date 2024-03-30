//
//  CategoryView.swift
//  Fineprice
//
//  Created by Кирилл Архипов on 06.04.2024.
//

import SwiftUI

struct CategoryView: View {
    @State private var categories = ["Овощи", "Мясо", "Фрукты", "Алкоголь"]
    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns:
                            [GridItem(.adaptive(minimum: 150), spacing: 15)],
                          spacing: 15) {
                    ForEach(categories, id: \.self) { category in
                        NavigationLink(destination: SearchView())
                        {
                            VStack {
                                Text("\(category)")
                                    .foregroundStyle(Color.black)
                                    .fontWeight(.bold)
                                    .lineLimit(1)
                                //                                    AsyncImage(url: URL(string: product.selectedShop.urlImage)) { image in
                                //                                        image
                                //                                            .resizable()
                                //                                            .aspectRatio(contentMode: .fit)
                                //                                            .clipShape(RoundedRectangle(cornerRadius: 20))
                                //                                    } placeholder: {
                                //                                        Image("noimg")
                                //                                            .resizable()
                                //                                            .aspectRatio(contentMode: .fit)
                                //                                            .clipShape(RoundedRectangle(cornerRadius: 20))
                                //                                    }
                                
                            }
                            .frame(width: 130)
                            .padding(20)
                            .background(.pinkieElem)
                            .clipShape(RoundedRectangle(cornerRadius: 20))
                            //.fixedSize(horizontal: false, vertical: true)
                            
                        }
                    }
                    
                }
                .padding(20)
            }
        }
    }
}

#Preview {
    CategoryView()
}
