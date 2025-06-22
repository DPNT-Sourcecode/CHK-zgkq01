class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus : str) -> int:
        """
        Calculates the total checkout price of the basket.

        args : 
            skus (string): string containing sku of priducts in the basket.

        returns :
            int : total checkout price of the basket or -1 for any invalid inputs.
        """
        if not isinstance(skus, str):
            return -1
        
        price_dict = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
            }
        
        special_offer_dict = {
            'A': {'count': 3, 'price': 130},
            'B': {'count': 2, 'price': 45},
            }
        
        sku_count = {}
        for sku in skus:
            if sku not in price_dict:
                return -1
            sku_count[sku] = sku_count.get(sku, 0) + 1
        
        total_price = 0

        for sku, count in sku_count.items():
            if sku in special_offer_dict:
                offer = special_offer_dict[sku]
                offer_sets = count // offer['count']
                remaining = count % offer["count"]
                total += offer_sets * offer['price']
                total += remaining * price_dict[sku]
            else:
                total += count * price_dict[sku]
        
        return total