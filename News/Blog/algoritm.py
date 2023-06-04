# import smtplib
# временно заброшенно
#
# my_email = "hanievmusa0504@gmail.com"
# my_password = "haniev2005"
# message="hello my name is Musa you my client"
# def send_email(email):
#     print(1)
#     server=smtplib.SMTP(host='smtp.gmail.com',port=587)
#     print(1)
#     server.starttls()
#     print(1)
#     server.login(my_email, my_password)
#     print(1)
#     server.sendmail(my_email, email, message.encode('utf-8'))
#     print(1)
#     server.quit()
def get_valide_post(arr,words):
    words = words.split()
    for post in arr:
        text = post.name.lower().split()
        for word in words:
            if word.lower() in text:
                break
        else:
            arr = arr.exclude(id=post.id)
    return arr

