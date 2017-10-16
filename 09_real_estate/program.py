import csv
import os
import statistics


class Purchase:
    def __init__(self, street, city, zip, state, beds, baths, sq__ft, house_type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.house_type = house_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_purchase(purchase_data):
        street = purchase_data['street']
        city = purchase_data['city']
        zip = purchase_data['zip']
        state = purchase_data['state']
        beds = int(purchase_data['beds'])
        baths = int(purchase_data['baths'])
        sq_ft = int(purchase_data['sq__ft'])
        house_type = purchase_data['type']
        sale_date = purchase_data['sale_date']
        price = int(purchase_data['price'])
        latitude = float(purchase_data['latitude'])
        longitude = float(purchase_data['longitude'])

        return Purchase(street, city, zip, state, beds, baths, sq_ft, house_type, sale_date, price, latitude, longitude)


def print_header():
    print("--------------------------------")
    print("                 Real Estate APP")
    print("--------------------------------")


def query_data(data, beds):
    cmp_price = lambda x: x.price
    purchases = [purchase for purchase in data if purchase.beds == beds and purchase.sq__ft > 0]
    # find most expensive 2 bed room house
    most_expensive = max(purchases, key=cmp_price)
    least_expensive = min(purchases, key=cmp_price)
    mean = statistics.mean([p.price for p in purchases])
    print("Most expensive {} bedroom house cost {} dollars and has {} baths and {} sq ft".format(beds,
                                                                                                 most_expensive.price,
                                                                                                 most_expensive.baths,
                                                                                                 most_expensive.sq__ft))

    print("Least expensive {} bedroom house cost {} dollars and has {} baths and {} sq ft".format(beds,
                                                                                                  least_expensive.price,
                                                                                                  least_expensive.baths,
                                                                                                  least_expensive.sq__ft
                                                                                                  )
          )

    print("The average price of all {} bed room houses is {}".format(beds, mean))


def load_data_file():
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, 'SacramentoRealEstateTransactions2008.csv')


def get_data(filename: str):
    with open(filename, 'r') as fin:
        csv_reader = csv.DictReader(fin)
        print(csv_reader.fieldnames)
        return [Purchase.create_purchase(row) for row in csv_reader]


def main():
    print_header()
    filename = load_data_file()
    data = get_data(filename)
    query_data(data, 4)


if __name__ == '__main__':
    main()

