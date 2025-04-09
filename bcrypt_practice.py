import bcrypt


my_password = "Test123!"

encoded_password = my_password.encode('utf-8')

salt = bcrypt.gensalt()

encrypted_password = bcrypt.hashpw(encoded_password, salt)

# print("Original Password:",my_password)
# print("Encrypted Password:", encrypted_password)


def check_password(user_attempt_password, saved_password):
    # user_attempt_password is here to verify that the user knows the right password.

    # Compare the encrypted user_attempt_password to encrypted current_password
    if bcrypt.checkpw(user_attempt_password.encode('utf-8'), saved_password):
        return True

    return False

print(check_password('Test123!', encrypted_password))
