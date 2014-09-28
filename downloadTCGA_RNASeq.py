from sgmllib import SGMLParser
import urllib2
import re
from download_RNASeq import *
from access_clinical import *
from download_RNASeq import *


def getRnaseqData(url):
    response_rnaseq = urllib2.urlopen(url)     # File like object, catches the response
    genes_name = list()
    normalized_count = list()
    header = 1
    for line in response_rnaseq:
        if header == 1:
            header = 2
        else:
            newline = line.split('\n')
            newline = [everyword.split('\t') for everyword in newline]
            genes_name.append(newline[0])
            normalized_count.append(newline[1])            
    return(genes_name, normalized_count)
    
def mergeAll():
    Mergeall = [data_merger_aliquot_cliniPatient, RNAseq_normalized_count]
 
def get_RNASeq(databaseRNAseq):
    class URLLister(SGMLParser):
            def reset(self):
                    SGMLParser.reset(self)
                    self.urls = []

            def start_a(self, attrs):
                    href = [v for k, v in attrs if k=='href']
                    if href:
                            self.urls.extend(href)

    if __name__ == "__main__":
            usock = urllib2.urlopen(databaseRNAseq)
            for lines in usock:
                if re.match("(.*)(  <title>Index of )", lines):
                    my_string = lines
                    aliquot_id = my_string[26:-47]
                    website_name = "https://tcga-data.nci.nih.gov"
                    my_new_string = website_name + my_string[18:-9]
                    print my_new_string
                    break;
            parser = URLLister() # List URLS
            parser.feed(usock.read())
            parser.close()
            usock.close()
            file_no = 1
            rnaseq_download_choice = raw_input('Do you want to download RNASeq files?[Y/N]')  # Ask the user's choice to download RNASeq file
            data_merger = list()
            for url in parser.urls:
                #print url # add my_new_string + url then store it in a list
                if url[-29:] == "rsem.genes.normalized_results":
                    new_url = my_new_string + '/' + url
                    file_name = "%s%s%s" % ("file", file_no, ".txt")
                    if rnaseq_download_choice == 'Y':
                        download_RNAseq(new_url, file_name)
                        print new_url
                    [RNAseq_genes_name, RNAseq_normalized_count] = getRnaseqData(new_url)
                    print RNAseq_genes_name
                    print RNAseq_normalized_count
                    print url[8:44]
                    aliquot_id = url[8:44]
                    data_merger_aliquot_cliniPatient = read_aliquot(aliquot_id) # Read Clinical data       
                    
                file_no = file_no + 1

databaseRNAseq = "https://tcga-data.nci.nih.gov/tcgafiles/ftp_auth/distro_ftpusers/anonymous/tumor/kirc/cgcc/unc.edu/illuminahiseq_rnaseqv2/rnaseqv2/unc.edu_KIRC.IlluminaHiSeq_RNASeqV2.Level_3.1.5.0/"
get_RNASeq(databaseRNAseq)




