# Download files through FTP directory
from ftplib import FTP

from ftplib import FTP
import os


def ftpDownloader(filename,
                  host="ftp.pyclass.com",
                  user="student@pyclass.com",
                  passwd="student123"):

    ftp=FTP(host)
    ftp.login(user, passwd)
    ftp.cwd("Data")  # change to ~/Data dict
    os.chdir("C:\\CS")
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)


if __name__ == '__main__':

    ftpDownloader("isd-lite-format.pdf")

