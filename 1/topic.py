def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini
    
    

def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan

    '''
    print('----Fungsi "add_topic" dijalankan----')
    #jawaban anda di bawah ini
    

def delete_topic(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin dihapus.
    Lalu hapus topik beserta semua aktivitasnya, hapus juga data di activity, submission, dan grade untuk id aktivitas yang terdapat di topik ini
    '''
    print('----Fungsi "delete_topic" dijalankan----')
    #jawaban anda di bawah ini
    

def update_topic(list_topic):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Tampilkan data eksisting.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_topic" dijalankan----')
    #jawaban anda di bawah ini
    count_title = 1

    for dict_topic in list_topic:
        dict_topic = dict(dict_topic)
        output_title = (dict_topic['Title'])
        print('{}: {}'.format(count_title, output_title))
        count_title = count_title + 1 
        
        
    try:  
        user_input_to_update = int(input("Masukkan nomor topik yang ingin di update: "))
        if user_input_to_update in range(count_title) and user_input_to_update != 0:
            user_input_to_update = str(user_input_to_update)
            for n in user_input_to_update:
                n = int(n)
                print("data eksisting...")
                print("Masukkan data baru. Kosongkan jika tidak ingin diubah.")
                updated_title = input("Masukkan Title: ")
                updated_desc = input("Masukkan Descirption: ")
                if updated_title == "":
                    pass
                else:
                    list_topic[n-1]['Title'] = updated_title
                if updated_desc =="":
                    pass
                else:
                    list_topic[n-1]['Description'] = updated_desc
                print("Update topic selesai")
        else:
            print("Error: Topik yang anda masukkan tidak ada!")
    except ValueError:
        print("Error: Nilai yang dimasukkan harus angka!")

    print(input("\n\nTekan Enter untuk kembali ke menu..."))
    
    
    
    
    

def add_activity(list_topic, dict_activity, id_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin tambah aktifitas.
    Minta data aktifitas baru, tambahkan counter id_activity dengan 1, lalu tambahkan ke dalam dict_activity.
    Tambahkan juga id_activity ke dalam list aktifitas topik.
    Tanya jika ingin menambah aktifitas lagi

    Return: id_activity yang terakhir digunakan
    '''

    print('----Fungsi "add_activity" dijalankan----')
    #jawaban anda di bawah ini

    

def update_activity(list_topic, dict_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "udpate_activity" dijalankan----')
    #jawaban anda di bawah ini
    


def delete_activity(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, minta inputan topik. 
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Hapus activity, submission, dan grade dengan id activity yang dipilih
    '''
    print('----Fungsi "delete_activity" dijalankan----')
    #jawaban anda di bawah ini
    
    
    

    



def print_topic_to_file(list_topic, dict_activity):
    '''
    Minta nama file.
    Print setiap detail topik, beserta list aktifitasnya ke file.
    '''

    print('----Fungsi "print_topic_to_file" dijalankan----')
    #jawaban anda di bawah ini

    




    
if __name__ == "__main__":
    #type_activity = ['assignment', 'material']
    #id_activity adalah variable global untuk id unik semua activity di semua topic
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                        ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                        ('Password', '^[a-zA-Z0-9]{8,12}$')],
            'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                        '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                        '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                        }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                        1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                        2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                        }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                            '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                            '114': 'Ini jawaban mahasiswa 114'}
                    }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                }

    
    
