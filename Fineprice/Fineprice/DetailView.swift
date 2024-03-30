//
//  DetailView.swift
//  Fineprice
//
//  Created by admin on 04.01.2024.
//

import SwiftUI

struct DetailView: View {
    
    var product : Product
    @Binding var cart : [String:[Product]]
    
    @State var showAlert = false
    @State var tighten = true
    
    
    var body: some View {
        ScrollView {
            Text(product.name)
                .padding()
                .font(.system(size: 30))
                .fontWeight(.black)
            TabView {
                ForEach (product.shops, id: \.name) { shop in
                    AsyncImage(url: URL(string: shop.urlImage)) { image in
                        image
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                    } placeholder: {
                        Image("noimg")
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                    }
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
                        VStack (alignment: .leading) {
                            Text("\(shop.name):")
                            Text(shop.price)
                            //Text("\(String(format: "%.2f", shop.price)) руб")
                        }.padding(.horizontal, 20)
                        
                        Button(action: {
                            var changedProduct = product
                            let indexOfShop = product.shops.firstIndex(where: { shopFor in
                                shopFor.name == shop.name
                            })
                            changedProduct.selectedShop = product.shops[indexOfShop!]
                            let oldAllInAll = cart[shop.name]!.last!
                            cart[shop.name]! = cart[shop.name]!.dropLast() + [changedProduct]
                            cart[shop.name]! = cart[shop.name]! + [oldAllInAll]
                            
                            cart.forEach { shopName, products in
                                var sum = 0
                                products.dropLast().forEach { product in
                                    let value = product.selectedShop.price.components(separatedBy: ",")
                                    print(value[0])
                                    sum += Int(value[0]) ?? 0
                                }
                                cart[shopName]! = products.dropLast() + [Product(id: 99, name: "Итог: ", description: "", shops: [], selectedShop: Shop(price: "\(sum)", name: "", logoUrl: "", url: "", urlImage: ""))]
                                //print("\(shoppingCart)")
                                //shoppingCart[shop]!.append() //TODO: DANGER!
                            }
                            //cart.updateValue(newProducts, forKey: shop.name)
                            //UIApplication.shared.open(URL(string: shop.url)!)
                        }) {
                            Text("В корзину")
                                .padding(.horizontal, 15)
                                .padding(.vertical, 5)
                                .background(Color.green)
                                .foregroundColor(.black)
                                .clipShape(Capsule())
                        }.frame(maxWidth: .infinity, alignment: .trailing)
                    }//TODO: Добавить информацию о количестве уже имеющихся в корзине из определенного магазина + убрать алерт
                    
                }
            }.padding(.horizontal, 20)
            Button(action: {
                UIApplication.shared.open(URL(string: product.selectedShop.url)!)
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
                                                shops: [Shop(price: "75000", name: "Магнит", logoUrl: "magnitLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                                        Shop(price: "95", name: "Лента", logoUrl: "lentaLogo",url: "https://vk.com/keril1", urlImage: "product"),
                                                        Shop(price: "85", name: "Пятерочка", logoUrl: "pyatLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                                        Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")],
                                                selectedShop: Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")
                               ), cart: .constant(["5ka": [Product(id: 1,
                                                         name: "Майонез",
                                                         description: "Нежный майонез высшего качества, приготовленный из свежих яиц, отборного растительного масла и натурального уксуса. Идеально подходит для добавления в салаты, приготовления соусов или использования в качестве дипа. Обеспечивает богатый вкус и кремовую текстуру, чтобы удовлетворить ваши гастрономические предпочтения.",
                                                         shops: [Shop(price: "75000", name: "Магнит", logoUrl: "magnitLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                                                 Shop(price: "95", name: "Лента", logoUrl: "lentaLogo",url: "https://vk.com/keril1", urlImage: "product"),
                                                                 Shop(price: "85", name: "Пятерочка", logoUrl: "pyatLogo", url: "https://vk.com/keril1", urlImage: "product"),
                                                                 Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")],
                                                         selectedShop: Shop(price: "65", name: "Светофор", logoUrl: "svetLogo", url: "https://vk.com/keril1", urlImage: "product")
                                         )]]))
}
