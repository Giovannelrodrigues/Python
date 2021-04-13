from programaFun import *
if __name__ == '__main__':
    
    opc = 0
    while opc != 6:
        vcon = conexao()
        opc = mostrar_tela()
        if opc == 1:
            Inserir(vcon)
        
        if opc == 2:
            deletar(vcon)
    
        if opc == 3:
            atualizar(vcon)
        
        if opc ==4:
            consulta(vcon)
        
        if opc ==5:
            consultaNome(vcon)
        
        
    print('FIM DO PROGRAMA')
