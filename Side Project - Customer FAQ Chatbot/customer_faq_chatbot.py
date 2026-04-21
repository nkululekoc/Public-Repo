#Chatbot FAQs

chatbot_faqs = {
    "operating_hours": "We are open Monday to Friday from 9:00 AM to 6:00 PM, and Saturday from 9:00 AM to 2:00 PM. We are closed on Sundays and public holidays.",
    
    "branch_location": "Our main branch is located at 123 Business Street, Durban, South Africa. You can find directions on our website.",
    
    "contact_number": "You can reach us at +27 31 123 4567 during business hours.",
    
    "email_address": "For inquiries, email us at support@company.com and we will respond within 24 hours.",
    
    "delivery_time": "Standard delivery takes 3–5 business days. Express delivery options are available at checkout.",
    
    "return_policy": "We accept returns within 14 days of purchase, provided the item is unused and in its original packaging.",
    
    "payment_methods": "We accept credit/debit cards, EFT, and mobile payments such as Apple Pay and Google Pay.",
    
    "order_tracking": "Once your order is shipped, you will receive a tracking number via email to monitor your delivery.",
    
    "appointment_booking": "Appointments can be booked online through our website or by calling our customer service team.",
    
    "services_offered": "We offer consulting, product sales, and customer support services tailored to your needs.",
    
    "parking_availability": "Free parking is available at our branch for all customers.",
    
    "wifi_access": "Complimentary Wi-Fi is available in-store for customers.",
    
    "support_hours": "Customer support is available Monday to Friday from 8:00 AM to 8:00 PM.",
    
    "international_shipping": "Yes, we offer international shipping. Delivery times and fees vary depending on the destination.",
    
    "cancellation_policy": "Orders can be canceled within 2 hours of placement. After that, processing may already be underway."
}

#first chatbot message
chatbot_greeting = "Hi, my name is NK, how can I help you"
chatbot_opening = "I will tell you to ask again if I don't understand your question, type 'goodbye' to end the conversation"

question = ""

print(f"{chatbot_greeting:^90}")
print(f"{chatbot_opening:^90}")

while question != "goodbye":
    question = input("Ask: ")

    if "time" in question:
        print(chatbot_faqs["operating_hours"])
    elif "location" in question:
        print(chatbot_faqs["branch_location"])
    elif "number" in question:
        print(chatbot_faqs["contact_number"])
    elif "email" in question:
        print(chatbot_faqs["email_address"])
    elif "delivery" in question:
        print(chatbot_faqs["delivery_time"])
    elif "return" in question:
        print(chatbot_faqs["return_policy"])
    elif "payment" in question:
        print(chatbot_faqs["payment_methods"])
    elif "track" in question:
        print(chatbot_faqs["order_tracking"])
    elif "appointment" in question:
        print(chatbot_faqs["appointment_booking"])
    elif "services" in question:
        print(chatbot_faqs["services_offered"])
    elif "parking" in question:
        print(chatbot_faqs["parking_availability"])
    elif "wifi" in question:
        print(chatbot_faqs["wifi_access"])
    elif "support" in question:
        print(chatbot_faqs["support_hours"])
    elif "shipping" in question:
        print(chatbot_faqs["international_shipping"])
    elif "cancel" in question:
        print(chatbot_faqs["cancellation_policy"])
    elif "goodbye" in question:
        break
    else:
        print("I do not understand please try again")


print("goodbye")