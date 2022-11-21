import matplotlib.pyplot as plt

def resumoApostas():

    apostas1 = []
    apostas2 = []
    apostas3 = []
    for j in range(1, len(usuariosLista), 1):
        if usuariosLista[j][9] != '':
            apostas1.append(listaSelecoes()[int(usuariosLista[j][9])])
        else:
            apostas1.append('Não apostou.')
            
        if usuariosLista[j][10] != '':
            apostas2.append(listaSelecoes()[int(usuariosLista[j][10])])
        else:
            apostas2.append('Não apostou.')
            
        if usuariosLista[j][9] != '':
            apostas3.append(listaSelecoes()[int(usuariosLista[j][11])])
        else:
            apostas3.append('Não apostou.')
    
    dadosApostasIniciais = np.array([apostas1,apostas2,apostas3])
    rotuloColuna = np.delete(np.array(usuariosLista)[:,0], 0)
    rotuloLinha  = ['Campeão','Vice-campeão','Terceiro colocado']
    ncoluna = len(rotuloColuna)
    nlinha  = len(rotuloLinha)

    espacos = ncoluna*[0.25]
    
    figura = plt.figure(figsize = (6,1))
    
    font = {'family':'serif', 'color':'black', 'weight':'normal', 'size':24}
    plt.title('Apostas Iniciais', fontdict = font)
    
    tabela = plt.table(cellText = dadosApostasIniciais,
                       colWidths = espacos,#[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                       rowLabels = rotuloLinha,
                       colLabels = rotuloColuna)
    
    celula = tabela.properties()["celld"]
    for coluna in range(ncoluna):
        for linha in range(nlinha+1):
            celula[linha, coluna]._loc = 'center'
                       
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(20)
    tabela.scale(2, 4)
    plt.axis('off')
    plt.show()
    
    return figura

 figura = resumoApostas()
