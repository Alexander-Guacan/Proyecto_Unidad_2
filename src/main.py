from ShopMenu import ShopMenu, Shop, Verifier, CreditCard, Input

def main() -> None:
    shop = Shop()
    shop_menu = ShopMenu(shop)
    shop_menu.print()

if __name__ == "__main__":
    main()