from eth_account import Account
Account.enable_unaudited_hdwallet_features()
# Запрос количества кошельков для создания
num_wallets = int(input("Введите количество кошельков для создания: "))


# Создание файла для сохранения всех секретных фраз
with open("phrase.txt", "w") as mnemonicphrase, open('addres.txt', "w") as addr:
    for i in range(num_wallets):
        # Создание нового кошелька и получение секретной фразы
        acct, mnemonic = Account.create_with_mnemonic(passphrase = '', num_words = 12, language = 'english', account_path = "m/44'/60'/0'/0/0")
        
        # Запись секретной фразы и адреса в разные файлы для удобства копирования
        mnemonicphrase.write(f"{mnemonic}\n")
        addr.write(f"{acct.address}\n")
        

        print(f"Кошелек {i + 1} создан и секретная фраза записана в phrase.txt")

print("Все кошельки созданы, и секретные фразы сохранены в phrase.txt.")



