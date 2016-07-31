
import re

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "INVALID"
        self.valid = False

        self.validate()



# Create and add your method called `determine_card_type` to the CreditCard class here:

# Visa must start with 4
# Mastercard must start with 51, 52, 53, 54 or 55
# AMEX must start with 34 or 37
# Discover must start with 6011


# Visa, MC and Discover have 16 digits
# AMEX has 15

    def determine_card_type(self):

            if re.match(r'4', self.card_number):
                self.card_type = "VISA"
            elif re.match(r'5[1-5]', self.card_number):
                self.card_type = "MASTERCARD"
            elif re.match(r'6011', self.card_number):
                self.card_type = "DISCOVER"
            elif re.match(r'3[47]', self.card_number):
                self.card_type = "AMEX"



# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        return len(str(self.card_number))



    def check_luhn(self):

        gen_1 = ( eval(x) for x in reversed(self.card_number) )

        gen_2 = (num * 2 if idx % 2 else num for idx, num in enumerate(gen_1) )

        self.valid = sum(eval(x) for x in "".join(str(x) for x in list(gen_2)) ) % 10 == 0



# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):

        self.check_luhn()

        if self.valid:
            self.determine_card_type()

        if not ( ( (self.card_type == "VISA" or "MASTERCARD" or "DISCOVER") and self.check_length() == 16) or (self.card_type == "AMEX" and self.check_length() == 15) ):
            self.card_type = "INVALID"
            self.valid = False





# do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
