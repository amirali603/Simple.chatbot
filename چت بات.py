# چت‌باتی که جواب‌های جدید رو ذخیره می‌کنه
responses = {
    "اسم تو چیه؟": "من یه چت‌بات ساده‌ام، ولی تو می‌تونی هر اسمی روم بذاری!",
    "حالت چطوره؟": "من یه برنامه‌ام، ولی اگه بخوام بگم، خوبم!",
    "چه خبر؟": "همه چیز آرومه! خودت چه خبر؟"
}

def chatbot():
    print("سلام! من یه چت‌بات ساده‌ام. برای خروج 'خداحافظ' رو تایپ کن.")
    
    while True:
        user_input = input("تو: ").strip()
        
        if user_input.lower() in ["خداحافظ", "bye", "exit"]:
            print("چت‌بات: خوشحال شدم باهات حرف زدم! خداحافظ!")
            break
        
        elif user_input in responses:
            print(f"چت‌بات: {responses[user_input]}")
        
        else:
            print("چت‌بات: جوابشو نمی‌دونم! چی باید بگم؟")
            new_response = input("تو بگو چی جواب بدم: ").strip()
            responses[user_input] = new_response
            print("چت‌بات: ممنون! یاد گرفتم.")

chatbot()
