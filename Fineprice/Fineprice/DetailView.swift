//
//  DetailView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct DetailView: View {
    var product : Product
    var items = ["man", "shut", "yo", "ass", "up"]
    @State var showAlert = false
    @State var tighten = true
    
    
    var body: some View {
        ScrollView {
            Text(product.name)
                .font(.system(size: 30))
                .fontWeight(.black)
            TabView {
                ForEach (items, id: \.self) { item in
                    Image(product.urlImage)
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                }
            }.tabViewStyle(.page(indexDisplayMode: .always))
                .frame(height: 250)
            
            Section {
                Text("Описание:")
                    .font(.system(size: 20))
                    .fontWeight(.semibold)
                if tighten {
                    Text(product.description)
                    .lineLimit(3)
                    .transition(.opacity)
                }
                else {
                    Text(product.description)
                    .transition(.opacity)
                }
                    
                    
                Button(action: {
                    withAnimation {
                        tighten.toggle()
                    }
                }) {
                    if tighten {
                        Text("Показать больше")
                    }
                    else {
                        Text("Скрыть")
                    }
                }
            }.padding(.horizontal, 40)
                .padding(.bottom)
            Section {
                ForEach(product.shops, id: \.name) { shop in
                    HStack {
                        Image(shop.logoUrl)
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 30)
                        VStack {
                            Text("\(shop.name):")
                            Text("\(String(format: "%.2f", shop.price)) руб")
                        }.padding(.horizontal, 20)
                        
                        Button(action: {
                            showAlert = !showAlert
                            //addToCart
                        }) {
                            Text("В корзину")
                                .padding(.horizontal, 15)
                                .padding(.vertical, 5)
                                .background(Color.green)
                                .foregroundColor(.black)
                                .clipShape(Capsule())
                        }.frame(maxWidth: .infinity, alignment: .trailing)
                            .alert(isPresented: $showAlert) {
                                Alert(title: Text("WOW"))
                            }
                    }//TODO: Добавить информацию о количестве уже имеющихся в корзине из определенного магазина + убрать алерт
                    
                }
            }.padding(.horizontal, 20)
            Button(action: {
                //addToCart
            }) {
                Text("В корзину")
                    .fontWeight(.bold)
                    .fontWidth(.standard)
            }.padding()
                .padding(.horizontal, 40)
                .background(Color.green)
                .foregroundColor(.black)
                .clipShape(Capsule())
        }//.background(Color.accentColor, ignoresSafeAreaEdges: .all) //Цвет фона
    }
}

#Preview {
    DetailView(product: Product(id: 1,
                                name: "Майонез",
                                description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
                                shops: [Shop(price: 75000, name: "Магнит", logoUrl: "logo1", url: "URLtemplate1"),
                                         Shop(price: 95, name: "Лента", logoUrl: "logo2",url: "URLtemplate2"),
                                         Shop(price: 85, name: "Пятерочка", logoUrl: "logo3", url: "URLtemplate3"),
                                         Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4")],
                                selectedShop: Shop(price: 65, name: "Светофор", logoUrl: "logo4", url: "URLtemplate4"),
                                urlImage: "product"))
}
