import os
import csv


def get_all_result_paths(rootDir):

    file_paths = []
    for dir_, _, files in os.walk(rootDir):
        for fileName in files:
            relDir = os.path.relpath(dir_, rootDir)
            relFile = os.path.join(rootDir, relDir, fileName)

            if relFile.split('/')[-1] == 'results.csv':
                file_paths.append(relFile)

    return file_paths

def mean_result_file(result_paths):

    weeks = ['se1', 'se2', 'se3', 'se4', 'se5', 'se6', 'se7']
    classifiers = ['bayesnet', 'mlp', 'j48', 'randforest']

    for r_path in result_paths:
        file = open(r_path,'rb')
        csv_file = csv.reader(file)

        mean_file_name = '/'.join(r_path.split('/')[0:-1]) + '/mean_resuls.csv'
        mean_file = open(mean_file_name, 'wb')
        csv_mean_file = csv.writer(mean_file, delimiter=',')

        header = ['Classif','Sem','TotalInst','CCI','ICI','Kappa','MAE','A-TP-Rate','A-FP-Rate','R-TP-Rate','R-FP-Rate']
        csv_mean_file.writerow(header)

        print r_path

        for classifier in classifiers:
            for week in weeks:

                row = []
                count = 0.

                total_isnt = 0
                cci = 0
                ici = 0
                kappa = 0
                mae = 0
                a_tp_rate = 0
                a_fp_rate = 0
                r_tp_rate = 0
                r_fp_rate = 0

                for line in csv_file:
                    if line[1] == week and line[2] == classifier:
                        count += 1.

                        total_isnt += float(line[3])
                        cci += float(line[4])
                        ici += float(line[5])
                        kappa += float(line[6])
                        mae += float(line[7])
                        a_tp_rate += float(line[8])
                        a_fp_rate += float(line[9])
                        r_tp_rate += float(line[10])
                        r_fp_rate += float(line[11])

                row.append(classifier)
                row.append(week)
                row.append(round(total_isnt/count, 3))
                row.append(round(cci/count, 3))
                row.append(round(ici/count, 3))
                row.append(round(kappa/count, 3))
                row.append(round(mae/count, 3))
                row.append(round(a_tp_rate/count, 3))
                row.append(round(a_fp_rate/count, 3))
                row.append(round(r_tp_rate/count, 3))
                row.append(round(r_fp_rate/count, 3))

                csv_mean_file.writerow(row)
                file.seek(0)

        file.close()
        mean_file.close()


def mean_geral():

    paths = [ './r{}/balanceado/entre_semestres/CLEC/mean_resuls.csv',
              './r{}/balanceado/entre_semestres/CLPD/mean_resuls.csv',
              './r{}/balanceado/entre_turmas/CLEC/semestre_1/mean_resuls.csv',
              './r{}/balanceado/entre_turmas/CLEC/semestre_2/mean_resuls.csv',
              './r{}/balanceado/entre_turmas/CLPD/semestre_1/mean_resuls.csv',
              './r{}/balanceado/entre_turmas/CLPD/semestre_2/mean_resuls.csv',
              './r{}/com_atributos/entre_semestres/CLEC/mean_resuls.csv',
              './r{}/com_atributos/entre_semestres/CLPD/mean_resuls.csv',
              './r{}/com_atributos/entre_turmas/CLEC/semestre_1/mean_resuls.csv',
              './r{}/com_atributos/entre_turmas/CLEC/semestre_2/mean_resuls.csv',
              './r{}/com_atributos/entre_turmas/CLPD/semestre_1/mean_resuls.csv',
              './r{}/com_atributos/entre_turmas/CLPD/semestre_2/mean_resuls.csv',
              './r{}/sem_atributos/entre_semestres/CLEC/mean_resuls.csv',
              './r{}/sem_atributos/entre_semestres/CLPD/mean_resuls.csv',
              './r{}/sem_atributos/entre_turmas/CLEC/semestre_1/mean_resuls.csv',
              './r{}/sem_atributos/entre_turmas/CLEC/semestre_2/mean_resuls.csv',
              './r{}/sem_atributos/entre_turmas/CLPD/semestre_1/mean_resuls.csv',
              './r{}/sem_atributos/entre_turmas/CLPD/semestre_2/mean_resuls.csv'
              ]

    for path in paths:

        geral_file_path = mean_file_name ='./geral/' + '/'.join(path.split('/')[2:-1]) + '/geral_results.csv'
        geral_file = open(geral_file_path, 'wb')
        csv_geral_file = csv.writer(geral_file, delimiter=',')

        header = ['Classif','Sem','TotalInst','CCI','ICI','Kappa','MAE','A-TP-Rate','A-FP-Rate','R-TP-Rate','R-FP-Rate']
        csv_geral_file.writerow(header)

        file_r1 = open(path.format(1), 'rb')
        csv_file_r1 = csv.reader(file_r1)

        file_r2 = open(path.format(2), 'rb')
        csv_file_r2 = csv.reader(file_r2)

        file_r3 = open(path.format(3), 'rb')
        csv_file_r3 = csv.reader(file_r3)

        file_r4 = open(path.format(4), 'rb')
        csv_file_r4 = csv.reader(file_r4)

        file_r5 = open(path.format(5), 'rb')
        csv_file_r5 = csv.reader(file_r5)

        print csv_file_r1.next()
        print csv_file_r2.next()
        print csv_file_r3.next()
        print csv_file_r4.next()
        print csv_file_r5.next()

        for i in range(28):
            row = []

            row_r1 = csv_file_r1.next()
            row_r2 = csv_file_r2.next()
            row_r3 = csv_file_r3.next()
            row_r4 = csv_file_r4.next()
            row_r5 = csv_file_r5.next()

            total_isnt = (float(row_r1[2]) + float(row_r2[2]) + float(row_r3[2]) + float(row_r4[2]) + float(row_r5[2]))/5
            cci = (float(row_r1[3]) + float(row_r2[3]) + float(row_r3[3]) + float(row_r4[3]) + float(row_r5[3]))/5.
            ici = (float(row_r1[4]) + float(row_r2[4]) + float(row_r3[4]) + float(row_r4[4]) + float(row_r5[4]))/5.
            kappa = (float(row_r1[5]) + float(row_r2[5]) + float(row_r3[5]) + float(row_r4[5]) + float(row_r5[5]))/5.
            mae = (float(row_r1[6]) + float(row_r2[6]) + float(row_r3[6]) + float(row_r4[6]) + float(row_r5[6]))/5.
            a_tp_rate = (float(row_r1[7]) + float(row_r2[7]) + float(row_r3[7]) + float(row_r4[7]) + float(row_r5[7]))/5.
            a_fp_rate = (float(row_r1[8]) + float(row_r2[8]) + float(row_r3[8]) + float(row_r4[8]) + float(row_r5[8]))/5.
            r_tp_rate = (float(row_r1[9]) + float(row_r2[9]) + float(row_r3[9]) + float(row_r4[9]) + float(row_r5[9]))/5.
            r_fp_rate = (float(row_r1[10]) + float(row_r2[10]) + float(row_r3[10]) + float(row_r4[10]) + float(row_r5[10]))/5.

            row.append(row_r1[0])
            row.append(row_r1[1])
            row.append(round(total_isnt, 3))
            row.append(round(cci, 3))
            row.append(round(ici, 3))
            row.append(round(kappa, 3))
            row.append(round(mae, 3))
            row.append(round(a_tp_rate, 3))
            row.append(round(a_fp_rate, 3))
            row.append(round(r_tp_rate, 3))
            row.append(round(r_fp_rate, 3))

            print row
            csv_geral_file.writerow(row)

        geral_file.close()
        file_r1.close()
        file_r2.close()
        file_r3.close()
        file_r4.close()
        file_r5.close()


if __name__ == "__main__":

    #result_paths = get_all_result_paths('./r5/')
    #mean_result_file(result_paths)

    mean_geral()
