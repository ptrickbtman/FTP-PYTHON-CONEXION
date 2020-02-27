from ftplib import FTP


ftp = FTP('192.168.1.6')  #ftp direccion
ftp.login(user='user@xxx.com', passwd = '*********')


ftp.cwd('/files/')  #change working directory
ftp.retrlines('LIST') #view files + permissions


def saveFile(): #download specific file


    filename = 'hello.txt'  #file dowload

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()



def placeFile(): # uploading a file

    filename = 'file2.py'  # file
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()


