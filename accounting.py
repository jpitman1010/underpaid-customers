# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

def customer_sales_report(path):
  """take info from sales orders and output how much is owed if buyer didn't pay enough, or order complete if they did."""
  customer_orders=open(path)
  melon_cost = 1.00

  for line in customer_orders:
        # remove white spaces at beginning and end
    line=line.rstrip()
    # take line and split into list based on | separater
    words=line.split("|")
    # index each part of line
    customer_number=words[0]
    customer_name=words[1]
    amount_of_melons_ordered=words[2]
    payment_for_melons=words[3]

    print(f"{customer_number},{customer_name} paid ${payment_for_melons},",
          f"expected cost was ${cost_of_melons}")
    amount_expected= amount_of_melons_ordered * melon_cost
    if payment_for_melons != amount_expected:
      print(f"Customer #{customer_number} paid ${payment_for_melons},",
          f"expected ${amount_expected}"
    customer_orders.close(path)
customer_sales_report("customer_orders.txt")