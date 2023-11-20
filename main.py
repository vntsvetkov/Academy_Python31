from module import *


def main():

    auth = SMSAuthentication()
    payment = Payment(auth)
    card = Card()
    payment.pay(card, 1200)


if __name__ == "__main__":
    main()