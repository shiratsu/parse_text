import PyPDF2

def readPdf(filename,password):
    pdfFileObj = open(filename,'rb')
    objPdf = pdf = PyPDF2.PdfFileReader(pdfFileObj)
    text = ''
    print(objPdf.isEncrypted)
    if objPdf.isEncrypted:

        ret = objPdf.decrypt(password)
        if ret:
            print('Document decryption success.')
        else:
            print('Document decryption failed.')
            raise DecryptionFailedException

    for i in range(0, objPdf.getNumPages()):
        text += objPdf.getPage(i).extractText()+"\n";
    return text


if __name__ == "__main__":
    print(readPdf("/Users/hiratsukashu/Downloads/isemura_history.pdf","geekly"))
