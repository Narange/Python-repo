# A "select item and check out" GUI. Joke content is from the show Reno 911

from tkinter import *

root = Tk()
root.title("Zapateria La Bailarina")
root.minsize(500, 0)

# widgets: logo
image = PhotoImage(file="sign.PNG")
logo = Label(root, image=image)

# widgets: list of boots
label_boots = Label(root, text="Select boots with which to goof: ")
list_boots = Listbox(root, height=4, exportselection=False)
list_boots.insert(0, "Genuine Leather")
list_boots.insert(1, "Faux Leather")
list_boots.insert(2, "Genuine Ostrich")
list_boots.insert(3, "Faux Ostrich")

# prices of boots correspond to their position in list_boots
price_list = [200, 150, 1262.08, 100]

# widgets: list of number of payments
label_payments = Label(root, text="Select number of payments: ")
list_payments = Listbox(root, height=3, exportselection=False)
list_payments.insert(0, "1")
list_payments.insert(1, "2")
list_payments.insert(2, "3")

# label at the bottom which displays the final result of the purchase
label_result = Label(root, text="")


# Calculate the price per payment and put result in label_result. Called when main_button is clicked.
def main_button_fn():

    result_string = ""

    try:
        selected_boots = list_boots.get(list_boots.curselection()[0])
        selected_payments = list_payments.get(list_payments.curselection()[0])

        price = price_list[list_boots.curselection()[0]]
        payments = int(selected_payments)
        price_per_payment = round((price / payments), 2)

        """
        #debug print statements
        print("Main button was clicked")
        print("Boots:", selected_boots, type(selected_boots))
        print("Payments:", selected_payments, type(selected_payments))
        print(price)
        print(payments)
        print(price_per_payment)
        """

        payments_string = "payments"
        per_month_string = "per month"

        if (payments == 1):
            payments_string = "payment"
            per_month_string = ""
        result_string = f"You have purchased {selected_boots} boots for {payments} easy {payments_string} of {price_per_payment} {per_month_string}"

        if (selected_boots == "Genuine Ostrich" and payments == 3):
            result_string = "OH! " + result_string

    except Exception:
        result_string = "Select a type of boot and payment option."

    label_result["text"] = result_string


main_button = Button(root, text="Checkout", command=main_button_fn)

# pack into GUI
logo.pack()
label_boots.pack()
list_boots.pack()
label_payments.pack()
list_payments.pack()
main_button.pack()
label_result.pack()

root.mainloop()
