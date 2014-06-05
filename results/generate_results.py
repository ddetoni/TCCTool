import os


def model_MultilayerPerceptron(train_path, test_path, out_path, info_name):

    header = 'arquivo_treino: {0}\narquivo_teste: {1}\n'.format(train_path, test_path)

    weka_path = '../weka.jar'
    model_attributes = '-t {0} -T {1} -c first -v -o -i'.format(train_path, test_path)
    model_command = 'weka.classifiers.functions.MultilayerPerceptron {0}'.format(model_attributes)
    java_command = 'java -classpath {0} {1}'.format(weka_path, model_command)

    final_command = '(echo \'{0}\'; {1}) > {2}{3}'.format(header, java_command, out_path, info_name)

    print 'MLP: \n{0}'.format(header)
    os.system(final_command)


def model_BayesNet(train_path, test_path, out_path, info_name):

    header = 'arquivo_treino: {0}\narquivo_teste: {1}\n'.format(train_path, test_path)

    weka_path = '../weka.jar'
    model_attributes = '-t {0} -T {1} -c first -v -o -i'.format(train_path, test_path)
    model_command = 'weka.classifiers.bayes.BayesNet {0}'.format(model_attributes)
    java_command = 'java -classpath {0} {1}'.format(weka_path, model_command)

    final_command = '(echo \'{0}\'; {1}) > {2}{3}'.format(header, java_command, out_path, info_name)

    print 'BayesNet: \n{0}'.format(header)
    os.system(final_command)

def model_J48(train_path, test_path, out_path, info_name):

    header = 'arquivo_treino: {0}\narquivo_teste: {1}\n'.format(train_path, test_path)

    weka_path = '../weka.jar'
    model_attributes = '-t {0} -T {1} -c first -v -o -i'.format(train_path, test_path)
    model_command = 'weka.classifiers.trees.J48 {0}'.format(model_attributes)
    java_command = 'java -classpath {0} {1}'.format(weka_path, model_command)

    final_command = '(echo \'{0}\'; {1}) > {2}{3}'.format(header, java_command, out_path, info_name)

    print 'J48: \n{0}'.format(header)
    os.system(final_command)


def model_RandomForest(train_path, test_path, out_path, info_name):

    header = 'arquivo_treino: {0}\narquivo_teste: {1}\n'.format(train_path, test_path)

    weka_path = '../weka.jar'
    model_attributes = '-t {0} -T {1} -c first -v -o -i'.format(train_path, test_path)
    model_command = 'weka.classifiers.trees.RandomForest {0}'.format(model_attributes)
    java_command = 'java -classpath {0} {1}'.format(weka_path, model_command)

    final_command = '(echo \'{0}\'; {1}) > {2}{3}'.format(header, java_command, out_path, info_name)

    print 'RandomForest: \n{0}'.format(header)
    os.system(final_command)


def between_groups_CLEC():
    basic_path = '../processed_data/ARFF2/CLEC/'
    path = '{0}semestre_{1}/se{2}/clec_S{1}_se{2}_t{3}.arff'

    for S in range(1,3):
        for se in range(1,8):
            out_path = 'sem_atributos/entre_turmas/CLEC/semestre_{0}/se_{1}/'.format(S,se)
            os.makedirs(out_path)

            in_path_g1 = path.format(basic_path,S,se,1)
            in_path_g2 = path.format(basic_path,S,se,2)

            model_MultilayerPerceptron(in_path_g1, in_path_g2, out_path, 'mlp_1_2.info')
            model_MultilayerPerceptron(in_path_g2, in_path_g1, out_path, 'mlp_2_1.info')

            model_BayesNet(in_path_g1, in_path_g2, out_path, 'bayesnet_1_2.info')
            model_BayesNet(in_path_g2, in_path_g1, out_path, 'bayesnet_2_1.info')

            model_J48(in_path_g1, in_path_g2, out_path, 'J48_1_2.info')
            model_J48(in_path_g2, in_path_g1, out_path, 'J48_2_1.info')

            model_RandomForest(in_path_g1, in_path_g2, out_path, 'randforest_1_2.info')
            model_RandomForest(in_path_g2, in_path_g1, out_path, 'randforest_2_1.info')


def between_groups_CLPD():
    basic_path = '../processed_data/ARFF2/CLPD/'
    path = '{0}semestre_{1}/se{2}/clpd_S{1}_se{2}_t{3}.arff'

    for S in range(1,3):
        for se in range(1,8):
            out_path = 'sem_atributos/entre_turmas/CLPD/semestre_{0}/se_{1}/'.format(S,se)
            os.makedirs(out_path)

            in_path_g1 = path.format(basic_path,S,se,1)
            in_path_g2 = path.format(basic_path,S,se,2)

            model_MultilayerPerceptron(in_path_g1, in_path_g2, out_path, 'mlp_1_2.info')
            model_MultilayerPerceptron(in_path_g2, in_path_g1, out_path, 'mlp_2_1.info')

            model_BayesNet(in_path_g1, in_path_g2, out_path, 'bayesnet_1_2.info')
            model_BayesNet(in_path_g2, in_path_g1, out_path, 'bayesnet_2_1.info')

            model_J48(in_path_g1, in_path_g2, out_path, 'J48_1_2.info')
            model_J48(in_path_g2, in_path_g1, out_path, 'J48_2_1.info')

            model_RandomForest(in_path_g1, in_path_g2, out_path, 'randforest_1_2.info')
            model_RandomForest(in_path_g2, in_path_g1, out_path, 'randforest_2_1.info')


def between_semester_CLEC():
    basic_path = '../processed_data/ARFF2/CLEC/'
    path = '{0}semestre_{1}/se{2}/clec_S{1}_se{2}_t{3}.arff'

    for se in range(1,8):
        out_path = 'sem_atributos/entre_semestres/CLEC/se{0}/'.format(se)
        os.makedirs(out_path)

        in_path_11 = path.format(basic_path,1,se, 1)
        in_path_12 = path.format(basic_path,1,se, 2)
        in_path_21 = path.format(basic_path,2,se, 1)
        in_path_22 = path.format(basic_path,2,se, 2)

        model_MultilayerPerceptron(in_path_11, in_path_21, out_path, 'mlp_11_21.info')
        model_MultilayerPerceptron(in_path_11, in_path_22, out_path, 'mlp_11_22.info')
        model_MultilayerPerceptron(in_path_12, in_path_21, out_path, 'mlp_12_21.info')
        model_MultilayerPerceptron(in_path_12, in_path_22, out_path, 'mlp_12_22.info')
        model_MultilayerPerceptron(in_path_21, in_path_11, out_path, 'mlp_21_11.info')
        model_MultilayerPerceptron(in_path_21, in_path_12, out_path, 'mlp_21_12.info')
        model_MultilayerPerceptron(in_path_22, in_path_11, out_path, 'mlp_22_11.info')
        model_MultilayerPerceptron(in_path_22, in_path_12, out_path, 'mlp_22_12.info')

        model_BayesNet(in_path_11, in_path_21, out_path, 'bayesnet_11_21.info')
        model_BayesNet(in_path_11, in_path_22, out_path, 'bayesnet_11_22.info')
        model_BayesNet(in_path_12, in_path_21, out_path, 'bayesnet_12_21.info')
        model_BayesNet(in_path_12, in_path_22, out_path, 'bayesnet_12_22.info')
        model_BayesNet(in_path_21, in_path_11, out_path, 'bayesnet_21_11.info')
        model_BayesNet(in_path_21, in_path_12, out_path, 'bayesnet_21_12.info')
        model_BayesNet(in_path_22, in_path_11, out_path, 'bayesnet_22_11.info')
        model_BayesNet(in_path_22, in_path_12, out_path, 'bayesnet_22_12.info')

        model_J48(in_path_11, in_path_21, out_path, 'j48_11_21.info')
        model_J48(in_path_11, in_path_22, out_path, 'j48_11_22.info')
        model_J48(in_path_12, in_path_21, out_path, 'j48_12_21.info')
        model_J48(in_path_12, in_path_22, out_path, 'j48_12_22.info')
        model_J48(in_path_21, in_path_11, out_path, 'j48_21_11.info')
        model_J48(in_path_21, in_path_12, out_path, 'j48_21_12.info')
        model_J48(in_path_22, in_path_11, out_path, 'j48_22_11.info')
        model_J48(in_path_22, in_path_12, out_path, 'j48_22_12.info')

        model_RandomForest(in_path_11, in_path_21, out_path, 'randforest_11_21.info')
        model_RandomForest(in_path_11, in_path_22, out_path, 'randforest_11_22.info')
        model_RandomForest(in_path_12, in_path_21, out_path, 'randforest_12_21.info')
        model_RandomForest(in_path_12, in_path_22, out_path, 'randforest_12_22.info')
        model_RandomForest(in_path_21, in_path_11, out_path, 'randforest_21_11.info')
        model_RandomForest(in_path_21, in_path_12, out_path, 'randforest_21_12.info')
        model_RandomForest(in_path_22, in_path_11, out_path, 'randforest_22_11.info')
        model_RandomForest(in_path_22, in_path_12, out_path, 'randforest_22_12.info')


def between_semester_CLPD():
    basic_path = '../processed_data/ARFF2/CLPD/'
    path = '{0}semestre_{1}/se{2}/clpd_S{1}_se{2}_t{3}.arff'

    for se in range(1,8):
        out_path = 'sem_atributos/entre_semestres/CLPD/se{0}/'.format(se)
        os.makedirs(out_path)

        in_path_11 = path.format(basic_path,1,se, 1)
        in_path_12 = path.format(basic_path,1,se, 2)
        in_path_21 = path.format(basic_path,2,se, 1)
        in_path_22 = path.format(basic_path,2,se, 2)

        model_MultilayerPerceptron(in_path_11, in_path_21, out_path, 'mlp_11_21.info')
        model_MultilayerPerceptron(in_path_11, in_path_22, out_path, 'mlp_11_22.info')
        model_MultilayerPerceptron(in_path_12, in_path_21, out_path, 'mlp_12_21.info')
        model_MultilayerPerceptron(in_path_12, in_path_22, out_path, 'mlp_12_22.info')
        model_MultilayerPerceptron(in_path_21, in_path_11, out_path, 'mlp_21_11.info')
        model_MultilayerPerceptron(in_path_21, in_path_12, out_path, 'mlp_21_12.info')
        model_MultilayerPerceptron(in_path_22, in_path_11, out_path, 'mlp_22_11.info')
        model_MultilayerPerceptron(in_path_22, in_path_12, out_path, 'mlp_22_12.info')

        model_BayesNet(in_path_11, in_path_21, out_path, 'bayesnet_11_21.info')
        model_BayesNet(in_path_11, in_path_22, out_path, 'bayesnet_11_22.info')
        model_BayesNet(in_path_12, in_path_21, out_path, 'bayesnet_12_21.info')
        model_BayesNet(in_path_12, in_path_22, out_path, 'bayesnet_12_22.info')
        model_BayesNet(in_path_21, in_path_11, out_path, 'bayesnet_21_11.info')
        model_BayesNet(in_path_21, in_path_12, out_path, 'bayesnet_21_12.info')
        model_BayesNet(in_path_22, in_path_11, out_path, 'bayesnet_22_11.info')
        model_BayesNet(in_path_22, in_path_12, out_path, 'bayesnet_22_12.info')

        model_J48(in_path_11, in_path_21, out_path, 'j48_11_21.info')
        model_J48(in_path_11, in_path_22, out_path, 'j48_11_22.info')
        model_J48(in_path_12, in_path_21, out_path, 'j48_12_21.info')
        model_J48(in_path_12, in_path_22, out_path, 'j48_12_22.info')
        model_J48(in_path_21, in_path_11, out_path, 'j48_21_11.info')
        model_J48(in_path_21, in_path_12, out_path, 'j48_21_12.info')
        model_J48(in_path_22, in_path_11, out_path, 'j48_22_11.info')
        model_J48(in_path_22, in_path_12, out_path, 'j48_22_12.info')

        model_RandomForest(in_path_11, in_path_21, out_path, 'randforest_11_21.info')
        model_RandomForest(in_path_11, in_path_22, out_path, 'randforest_11_22.info')
        model_RandomForest(in_path_12, in_path_21, out_path, 'randforest_12_21.info')
        model_RandomForest(in_path_12, in_path_22, out_path, 'randforest_12_22.info')
        model_RandomForest(in_path_21, in_path_11, out_path, 'randforest_21_11.info')
        model_RandomForest(in_path_21, in_path_12, out_path, 'randforest_21_12.info')
        model_RandomForest(in_path_22, in_path_11, out_path, 'randforest_22_11.info')
        model_RandomForest(in_path_22, in_path_12, out_path, 'randforest_22_12.info')


if __name__ == "__main__":

    between_groups_CLEC()
    between_groups_CLPD()

    between_semester_CLEC()
    between_semester_CLPD()
