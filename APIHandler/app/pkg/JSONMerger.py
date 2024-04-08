import json


with open("MAGNIT.json", "r", encoding="utf-8") as file1, open(
    "PYATEROCHKA.json", "r", encoding="utf-8"
) as file2:
    products1 = json.load(file1)
    products2 = json.load(file2)


def merge_products(products1, products2):
    merged_products = []

    id = 0

    for product1 in products1:
        for product2 in products2:
            if product1["name"] == product2["name"]:
                if product1.get("price") <= product2.get("price"):
                    selectedShop = {
                        "price": product1.get("price"),
                        "name": "Magnit",
                        "logoUrl": "magnitLogo",
                        "url": product1.get("url"),
                        "urlImage": product1.get("picture"),
                    }
                else:
                    selectedShop = {
                        "price": product2.get("price"),
                        "name": "Pyatorochka",
                        "logoUrl": "pyatLogo",
                        "url": product2.get("url"),
                        "urlImage": product2.get("picture"),
                    }
                merged_product = {
                    "id": id,
                    "name": product1["name"],
                    "description": "NO DESCRIPTION",
                    "shops": [
                        {
                            "price": product1.get("price"),
                            "name": "Magnit",
                            "logoUrl": "magnitLogo",
                            "url": product1.get("url"),
                            "urlImage": product1.get("picture"),
                        },
                        {
                            "price": product2.get("price"),
                            "name": "Pyatorochka",
                            "logoUrl": "pyatLogo",
                            "url": product2.get("url"),
                            "urlImage": product2.get("picture"),
                        },
                    ],
                    "selectedShop": selectedShop,
                }
                id += 1
                merged_products.append(merged_product)
                break

    return merged_products


merged_products = merge_products(products1, products2)

with open("merged.json", "w", encoding="utf-8") as json_file:
    json.dump(merged_products, json_file, ensure_ascii=False, indent=4)

for product in merged_products:
    i = 0
    if i == 2:
        break
    i += 1
    print("id:", product["id"])
    print("name:", product["name"])
    print("description:", product["description"])
    for shop in product["shops"]:
        print("  Shop Name:", shop["name"])
        print("  Price:", shop["price"])
        print("  Logo:", shop["logoUrl"])
        print("  URL:", shop["url"])
        print("  Image URL:", shop["urlImage"])

    print("     Shop Name:", product["selectedShop"].get("name"))
    print("     Price:", product["selectedShop"].get("price"))
    print("     Logo:", product["selectedShop"].get("logoUrl"))
    print("     URL:", product["selectedShop"].get("url"))
    print("     Image URL:", product["selectedShop"].get("urlImage"))
    print()
