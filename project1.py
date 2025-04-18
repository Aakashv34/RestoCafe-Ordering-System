from datetime import datetime

class RestoCafe:
    def __init__(self):
        self.cart = {}
        self.customer_name = ""
        self.Category = {
            "Meals": [("Kerala Veg Meals", 70), ("Fish Curry Meals", 110), ("Beef Curry Meals", 130), ("Chicken Curry Meals", 120)],
            "Non Veg Dishes": [("Kerala Chicken Roast", 140), ("Nadan Beef Fry", 150), ("Fish Fry (Pomfret/Avoli)", 160), ("Egg Curry", 60)],
            "Veg Dishes": [("Thoran (Cabbage/Beans)", 30), ("Avial", 40), ("Sambar", 25), ("Parippu Curry", 25)],
            "Snacks": [("Pazham Pori", 15), ("Uzhunnu Vada", 12), ("Parippu Vada", 10), ("Egg Puffs", 20)],
            "Beverages": [("Chaya (Tea)", 10), ("Kattan Chaya", 8), ("Nannari Sarbath", 15), ("Lime Juice", 20)]
        }

    def format_category_input(self, input_cat):
        return input_cat.strip().title().replace("_", " ")

    def show_menu(self):
        print("\n" + "="*40)
        print("🍴 Welcome to RestoCafe 🍴".center(40))
        print("="*40)
        print("Here's our menu:")
        for category, items in self.Category.items():
            print(f"\n📌 {category}")
            for item, price in items:
                print(f"   - {item:<30} ₹{price}")
        print("="*40)

    def order(self):
        self.customer_name = input("Enter your name: ").strip().title()
        print(f"\nHello {self.customer_name}! Let's start your order.")
        self.show_menu()

        while True:
            user_input = input("\nEnter Category (e.g. Meals, Snacks): ")
            self.user_Category = self.format_category_input(user_input)

            if self.user_Category not in self.Category:
                print("🚫 Invalid category. Please try again.")
                continue

            print(f"\n✅ Items in {self.user_Category}:")
            for item, price in self.Category[self.user_Category]:
                print(f"   - {item:<30} ₹{price}")

            self.food = input("\nEnter the name of the food you want: ").strip()
            matching_items = [i[1] for i in self.Category[self.user_Category] if i[0] == self.food]

            if not matching_items:
                print("🚫 Item not found in selected category. Please try again.")
                continue

            try:
                self.qty = int(input(f"Enter quantity for '{self.food}': "))
                if self.food in self.cart:
                    self.cart[self.food] = (self.cart[self.food][0] + self.qty, matching_items[0])
                else:
                    self.cart[self.food] = (self.qty, matching_items[0])
            except ValueError:
                print("❗ Please enter a valid number.")
                continue

            cont = input("Do you want to order more? (Y/N): ").upper()
            if cont != 'Y':
                break

    def bill(self):
        if not self.cart:
            print("🛒 No items in cart. Thank you!")
            return

        now = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        print("\n" + "="*50)
        print("🧾 Final Bill".center(50))
        print("="*50)
        print(f"Customer: {self.customer_name}")
        print(f"Date & Time: {now}")
        print("-"*50)
        print(f"{'Item':<25}{'Qty':<10}{'Price (₹)':<10}")
        print("-"*50)

        total = 0
        for item, (qty, price) in self.cart.items():
            line_total = qty * price
            total += line_total
            print(f"{item:<25}{qty:<10}{line_total:<10}")

        print("-"*50)
        print(f"{'TOTAL AMOUNT':<35} ₹{total}")
        print("="*50)
        print("🙏 Thank you for ordering from RestoCafe! 🙏")
        print("="*50)

# Run the app
if __name__ == "__main__":
    a = RestoCafe()
    a.order()
    a.bill()
