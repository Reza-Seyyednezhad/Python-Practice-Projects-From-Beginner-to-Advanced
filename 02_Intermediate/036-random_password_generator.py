import random
def random_password_generator(pass_length:int):
    upper_words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_words = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    sign = ".!@#$&_-"
    all_words = "".join([upper_words, lower_words, numbers, sign])
    list_of_random_pass_generated = random.sample(all_words, pass_length)
    print("".join(list_of_random_pass_generated))

# random_password_generator(16)


def random_password_generator_v2():
    upper_words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_words = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    sign = ".!@#$&_-"
    all_words = "".join([upper_words, lower_words, numbers, sign])
    try:
        user_pass_len_input = int(input("Enter Length of Password (Integer Number only): "))
        list_of_random_pass_generated = random.sample(all_words, user_pass_len_input)
        print("".join(list_of_random_pass_generated))
    except:
        print("An Integer Numbers ONLY ...................")
        

random_password_generator_v2()