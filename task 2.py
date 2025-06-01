stock_prices={
    "apple":120,
    "tesla":202,
    "google":120,
    "amezon":1220,
}
total_investment=0
n=int(input("enter how many stock enter you?:"))
input("string_number")
int("string_number")
with open("portfolio_rfeport.txt","w")as file:
    file.write("stock portfolio report\n")
    file.write("---------------------\n")
    for i in range(n):
        stock=input(f"enter a stock symbol #(i+1):").upper()
        quantity=int(input("enter a stock quatity of {stock}:"))
        if stock in stock_prices:
            price=stock_prices[stock]
            investment=price*quantity
            total_investment+=investment
            print(f"{stock}x{quantity}#{price}={investment}")
            file.write(f"{stock}x{quantity}@{price}=(investment)\n")
        else:
            print(f"sorry we dont habe any data of {stock}.")
            file.write(f"{stock}-not found in price ist\n")
            print(f"\nTotal investment :{total_investment}")
            file.write(f"\nTotal investment:{total_investment}\n")


