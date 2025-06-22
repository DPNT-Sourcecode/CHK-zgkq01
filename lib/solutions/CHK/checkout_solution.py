
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
            'D': 15,
            'E': 40
            }
            
        sku_count = {}
        for sku in skus:
            if sku not in price_dict: # illegal characters that are not items 
                return -1
            sku_count[sku] = sku_count.get(sku, 0) + 1
        
        total_price = 0

        # Fidning best offer based on basket, 5A for 200 is better than 3A for 130 therefore we handle 5A offers on priority
        if 'A' in sku_count:
            a_count = sku_count['A']
            offer_5a = a_count // 5
            rem_a = a_count % 5
            offer_3a = rem_a // 3
            final_rem_a = rem_a % 3

            total_price += offer_5a * 200
            total_price += offer_3a * 130
            total_price += final_rem_a * 50

        # E offers, if 2 Es are bought we add to the free B
        count_free_B = 0
        if 'E' in sku_count:
            e_count = sku_count['E']
            count_free_B = e_count // 2

            total_price += e_count * 40

        #B Handling with offers and with the E offer for free Bs
        if 'B' in sku_count:
            b_count = sku_count['B']
            end_b_count = max(0, b_count - count_free_B) # Handling by removing free B from the E offer

            offer_2b = end_b_count // 2
            rem_b = end_b_count % 2

            total_price += offer_2b * 45
            total_price += rem_b * 30


        if 'C' in sku_count:
            c_count = sku_count['C']
            
            total_price += c_count * 20

        if 'D' in sku_count:
            d_count = sku_count['D']
            
            total_price += d_count * 15
            
        

        
        return total_price
            
