
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
            if sku not in price_dict: # illegal characters that are not items 
                return -1
            sku_count[sku] = sku_count.get(sku, 0) + 1
        
        total_price = 0

        # For loop goign through and adding to total price based on special offers and items in the sku
        for sku, count in sku_count.items(): 
            if sku in special_offer_dict:
                offer = special_offer_dict[sku]
                offer_sets = count // offer['count']
                remaining = count % offer["count"]
                total_price += offer_sets * offer['price']
                total_price += remaining * price_dict[sku]
            else:
                total_price += count * price_dict[sku]
        
        return total_price
            


