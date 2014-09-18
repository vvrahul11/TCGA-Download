import urllib2
import re

def get_clinical_patient_row(response_clinical, TCGA_id):
    for line_clinical_patient in response_clinical:
        if re.search(TCGA_id, line_clinical_patient):
            clinical_patient_row = line_clinical_patient.split('\n')
            clinical_patient_row = [clinical_patient.split('	') for clinical_patient in clinical_patient_row][0]
            #raw_input("enter3"); print clinical_patient_row
            return(clinical_patient_row)
            break
        else:
            pass
        
           

def read_aliquot(aliquot_id):
    aliquot = "https://tcga-data.nci.nih.gov/tcgafiles/ftp_auth/distro_ftpusers/anonymous/tumor/kirc/bcr/biotab/clin/nationwidechildrens.org_biospecimen_aliquot_kirc.txt"
    clinical_patient = "https://tcga-data.nci.nih.gov/tcgafiles/ftp_auth/distro_ftpusers/anonymous/tumor/kirc/bcr/biotab/clin/nationwidechildrens.org_clinical_patient_kirc.txt"
    response_aliquot = urllib2.urlopen(aliquot)
    response_clinical = urllib2.urlopen(clinical_patient)
    for line_aliquot in response_aliquot:
        if re.search(aliquot_id, line_aliquot):
            raw_input("yes, working")
            aliquot_row = line_aliquot.split("\n")
            aliquot_row = [aliquot.split('	') for aliquot in aliquot_row][0]
            TCGA_id = aliquot_row[0][0:12]
            #raw_input("enter2"); print TCGA_id
            clinical_patient_row = get_clinical_patient_row(response_clinical, TCGA_id)
            return(aliquot_row, clinical_patient_row)
        
