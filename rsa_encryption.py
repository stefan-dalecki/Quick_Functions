import pandas as pd
import rsa
import time

class Import:
    def __init__(self, file_name):
        self.file = pd.read_csv(file_name).head()
        print(self.file)

class Encrypt:
    def __init__(self):
        self.pubkey, self.privkey = rsa.newkeys(512)
        self.date = time.strftime('%Y_%m_%d_%H_%M')

    def savekey(self, location, security):
        if security == 'public':
            with open(location+'\PublicKey_'+self.date, 'wb+') as f:
                key = rsa.PublicKey.save_pkcs1(self.pubkey, format = 'PEM')
                f.write(key)
        if security == 'private':
            with open(location+'\PrivateKey_'+self.date, 'wb+') as f:
                key = rsa.PrivateKey.save_pkcs1(self.privkey, format = 'PEM')
                f.write(key)

    def encrypt(self, df, key, *columns):
        for col in columns:
            df[col] = df[col].astype(str)
            for val in df[col]:
                enc_val = rsa.encrypt(val.encode(), key)
                df = df.replace(val, enc_val)
        self.file = df

    def priv_decrypt(privkey_file, date, df, *col):
        with open(pubkey_file) as publicfile:
            keydata = publicfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata,'PEM')
        with open('public_' + date + '.pem', 'w+') as f:
            f.write(pubkey.save_pkcs1().decode())
        for data in col:
            data = df[col]
            for val in df[col]:
                dec_val = rsa.decrypt(val, privkey).decode()
                df = df.replace(val, dec_val)
        self.file = df

class Export:
    def __init__(self, name):
        self.name = name

    def to_csv(df, file_loc):
        df.to_csv(file_loc)

    def to_pickle(df, file_loc):
        df.to_pickle(file_loc)

raw = Import(r'C:\Users\stda9924\Uni\CU\Not_PhD\MCDB\Sawyer_Rotation\Supplemental_Files\Excel\the_big_data_go_oooohhhh.csv')
today_keys = Encrypt()
save_publickey = Encrypt.savekey(today_keys, r'C:\Users\stda9924\Uni\CU\Not_PhD\MCDB\Sawyer_Rotation\Encryption', 'public')
save_privatekey = Encrypt.savekey(today_keys, r'C:\Users\stda9924\Uni\CU\Not_PhD\MCDB\Sawyer_Rotation\Encryption', 'private')
Encrypt.encrypt(raw, raw.file, today_keys.pubkey, 'BuffOne.Card.ID')
Export.to_pickle(raw.file, r'C:\Users\stda9924\Uni\CU\Not_PhD\MCDB\Sawyer_Rotation\output')
