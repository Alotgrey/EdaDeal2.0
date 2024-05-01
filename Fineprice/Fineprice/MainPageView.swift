//
//  MainPageView.swift
//  Fineprice
//
//  Created by Кирилл Архипов on 13.04.2024.
//

import SwiftUI

struct MainPageView: View {
    let testProduct = Product(id: 1,
                              name: "Майонез",
                              description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
                              shops: [Shop(price: "75", name: "Магнит", logoUrl: "logo1", url: "https://vk.com/keril1", urlImage: "product"),
                                       Shop(price: "95", name: "Лента", logoUrl: "logo2",url: "https://vk.com/keril1", urlImage: "product"),
                                       Shop(price: "85", name: "Пятерочка", logoUrl: "logo3", url: "https://vk.com/keril1", urlImage: "product"),
                                       Shop(price: "65", name: "Светофор", logoUrl: "logo4", url: "https://vk.com/keril1", urlImage: "product")],
          selectedShop: Shop(price: "65", name: "Светофор", logoUrl: "logo4", url: "https://vk.com/keril1", urlImage: "product"))
    @ObservedObject var model : Model
    var body: some View {
        NavigationStack {
            //Text("ECO")
            TabView {
                NavigationLink {
                    StoreView()
                } label: {
                    Image("lentaLogo")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                }.buttonStyle(PlainButtonStyle())
                NavigationLink {
                    StoreView()
                } label: {
                    Image("pyatLogo")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                }.buttonStyle(PlainButtonStyle())
                NavigationLink {
                    StoreView()
                } label: {
                    Image("magnitLogo")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                }.buttonStyle(PlainButtonStyle())
                NavigationLink {
                    StoreView()
                } label: {
                    Image("svetLogo")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                }.buttonStyle(PlainButtonStyle())

            }.frame(height: 200)
                .clipShape(RoundedRectangle(cornerRadius: 20))
                .tabViewStyle(.page(indexDisplayMode: .always))
                .padding()
            HStack {
                NavigationLink {
                    DetailView(product: testProduct, model: model)
                } label: {
                    Image("noimg")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        
                }.buttonStyle(PlainButtonStyle())
                    .frame(width: 100, height: 200)
                        .clipShape(RoundedRectangle(cornerRadius: 20))
                NavigationLink {
                    DetailView(product: testProduct, model: model)
                } label: {
                    Image("noimg")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        
                }.buttonStyle(PlainButtonStyle())
                    .frame(width: 100, height: 200)
                        .clipShape(RoundedRectangle(cornerRadius: 20))
                NavigationLink {
                    DetailView(product: testProduct, model: model)
                } label: {
                    Image("noimg")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        
                }.buttonStyle(PlainButtonStyle())
                    .frame(width: 100, height: 200)
                        .clipShape(RoundedRectangle(cornerRadius: 20))
            }.padding()
            Spacer()
        }
    }
}

#Preview {
    MainPageView(model: Model())
}
