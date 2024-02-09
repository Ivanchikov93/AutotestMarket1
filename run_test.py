from Сreatecardcorrectiontest import Сreatecardcorrection
from Creatcardpublick import Сreatecardpublick
from modercardcorrect import Modercardcorrect
from Moder_card_publick import Moder_card_publick
from order_not_auto import Order_not_auto
from Order_auto import Order_auto
from Salesman import Sales_test
from Buyer import Buyer_test
from Review_test import review_test
def run_test():
    tests = [
        (Сreatecardpublick(), "Сreatecardpublick"),
        (Сreatecardcorrection(), "Сreatecardcorrection"),
        (Modercardcorrect(), "Modercardcorrect"),
        (Moder_card_publick(), "Moder_card_publick"),
        (Order_not_auto(), "Order_not_auto"),
        (Order_auto(), "Order_auto"),
        (Sales_test(), "Sales_test"),
        (Buyer_test(), "Buyer_test"),
        (review_test(), "review_test")
    ]

    for test, name in tests:
        try:
            print(f"Запуск теста: {name}")
            test.test_site()
            print(f"Тест {name} пройден успешно!\n")
        except Exception as e:
            print(f"Ошибка в тесте {name}: {e}\n")


if __name__ == "__main__":
    run_test()

