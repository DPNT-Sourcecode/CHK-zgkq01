class CheckoutSolution:
    """
    Added more modular code to class
    """

    def __init__(self):
        self.price_dict = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10,
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 80,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 30,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 90,
            'Y': 10,
            'Z': 50

        }
        
        self.offer_dict = {
            'A': [{'type' : 'bulk', 'quantity': 5, 'price': 200},
                  {'type' : 'bulk', 'quantity': 3, 'price': 130}],

            'B': [{'type' : 'bulk', 'quantity': 2, 'price': 45}],

            'E': [{'type' : 'free', 'buy_quantity': 2, 'free_item': 'B', 'free_quantity': 1}],

            'F': [{'type' : 'free', 'buy_quantity': 2, 'free_item': 'F', 'free_quantity': 1}],

            'H': [{'type' : 'bulk', 'quantity': 10, 'price': 80},
                  {'type' : 'bulk', 'quantity': 5, 'price': 45}],
            
            'K': [{'type' : 'bulk', 'quantity': 2, 'price': 150}],

            'P': [{'type' : 'bulk', 'quantity': 5, 'price': 200}],

            'Q': [{'type' : 'bulk', 'quantity': 3, 'price': 80}],

            'V': [{'type' : 'bulk', 'quantity': 3, 'price': 130},
                  {'type' : 'bulk', 'quantity': 2, 'price': 90}],
            
            'N': [{'type' : 'free', 'buy_quantity': 3, 'free_item': 'M', 'free_quantity': 1}],

            'R': [{'type' : 'free', 'buy_quantity': 3, 'free_item': 'Q', 'free_quantity': 1}],

            'U': [{'type' : 'free', 'buy_quantity': 3, 'free_item': 'U', 'free_quantity': 1}],
            
            
            }
        
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
        
        if not skus:
            return 0
        
        sku_count = self.count_skus(skus)
        if sku_count is None:
            return -1
        
        if not sku_count:
            return -1
        
        free_items = self.calculate_free_items(sku_count)

        adjusted_count = sku_count.copy()
        for sku, free_count in free_items.items():
            if sku in adjusted_count:
                adjusted_count[sku] = max(0, adjusted_count[sku] - free_count)
        
        total_price = 0
        for sku, count in adjusted_count.items():
            if count > 0:
                cost, _ = self.apply_bulk_offers(sku, count)
                total_price += cost

        return total_price


    def count_skus(self, skus: str):
        """
        Count how many of each sku there is
        """

        sku_count = {}

        for sku in skus:
            if sku not in self.price_dict:
                return None
            
            sku_count[sku] = sku_count.get(sku, 0) + 1

        return sku_count
    

    def apply_bulk_offers(self, sku, count):
        """
        Apply bulk discount offers such as 2B for 45 etc...
        """

        if sku not in self.offer_dict:
            return count * self.price_dict[sku], 0
        
        bulk_offers = [offer for offer in self.offer_dict[sku] if offer['type'] == 'bulk']

        if not bulk_offers:
            return count * self.price_dict[sku], 0
        
        minimum_cost_for_quantity = [float('inf')] * (count + 1)
        minimum_cost_for_quantity[0] = 0

        for current_quantity in range(1, count+1):
            minimum_cost_for_quantity[current_quantity] = minimum_cost_for_quantity[current_quantity - 1] + self.price_dict[sku]
        
            for bulk_offer in bulk_offers:
                offer_quantity = bulk_offer['quantity']
                offer_price = bulk_offer['price']

                if current_quantity >= offer_quantity:
                    remaining_quantity = current_quantity - offer_quantity
                    cost_with_this_offer = minimum_cost_for_quantity[remaining_quantity] + offer_price
                    minimum_cost_for_quantity[current_quantity] = min(minimum_cost_for_quantity[current_quantity], cost_with_this_offer)
        
        return minimum_cost_for_quantity[count], 0
    

       
    
    def calculate_free_items(self, sku_count):
        """
        Calculate free items from free item offers such as 1 F free for 2F
        """
        free_items = {}

        if not sku_count:
            return free_items

        for sku, count in sku_count.items():
            if sku in self.offer_dict:
                free_offers = [offer for offer in self.offer_dict[sku] if offer['type'] == 'free']

                for offer in free_offers:
                    buy_quantity = offer.get('buy_quantity', 0)
                    free_item = offer.get('free_item')
                    free_quantity_per_set = offer.get('free_quantity', 0)
                    if free_item and buy_quantity > 0 and free_quantity_per_set > 0:
                        max_sets_from_trigger = count // buy_quantity

                        if max_sets_from_trigger > 0:
                            total_free_needed = max_sets_from_trigger * free_quantity_per_set
                            available_free_items = sku_count.get(free_item, 0)

                            if free_item == sku:
                                total_tiems_needed = max_sets_from_trigger * buy_quantity + total_free_needed
                                actual_sets = min(max_sets_from_trigger, count // (buy_quantity + free_quantity_per_set))
                                actual_free_quantity = actual_sets * free_quantity_per_set
                            else:
                                actual_free_quantity = min(total_free_needed, available_free_items)
                            
                            if actual_free_quantity > 0:
                                free_items[free_item] = free_items.get(free_item, 0) + actual_free_quantity
        
        return free_items
            
