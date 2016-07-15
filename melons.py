"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty):
        """Initialize melon traits"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self, species, qty):
        """Calculate price."""

        if species == "Christmas melons":
            base_price = 5 * 1.5
            total = (1 + self.tax) * self.qty * base_price
            
        elif qty < 10:
            base_price = 5 + 3
            total = (1 + self.tax) * self.qty * base_price
           
        else:
            base_price = 5
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        """Set domestic tax to 0.08"""

        self.order_type = "domestic"
        self.tax = 0.08
        super(DomesticMelonOrder, self).__init__(species, qty)
        # super(DomesticMelonOrder, self).get_total()
        # super(DomesticMelonOrder, self).mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty, country_code):
        """Set international tax to 0.17"""

        self.order_type = "international"
        self.country_code = country_code
        self.tax = 0.17
        super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self):
        """Get country code"""

        return self.country_code

    # def mark_shipped(self):

        # super(InternationalMelonOrder, self).mark_shipped()

        # print 'international order shipped!'



# class DomesticMelonOrder(object):
#     """A domestic (in the US) melon order."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code