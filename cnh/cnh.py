class Cnh:
    nome: None
    rg: None
    cpf: None
    data_nasc: None
    filiacao: None
    permissao: None
    acc: None
    cat_hab: None
    n_registro: None
    validade: None
    primeira_hab: None
    obs: None
    local: None
    dt_emissao: None

    def __init__(self, nome, rg, cpf, data_nasc, filiacao,cat_hab, n_registro, validade, primeira_hab,local, dt_emissao, permissao = False, acc = False, obs = 'SEM OBSERVAÇÃO;',):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.filiacao = filiacao
        self.cat_hab = cat_hab
        self.n_registro = n_registro
        self.validade = validade
        self.primeira_hab = primeira_hab
        self.local = local
        self.dt_emissao = dt_emissao
        self.permissao = permissao
        self.acc = acc
        self.obs = obs

    def eh_permissao(self, entrada):
        if entrada.upper() == 'S':
            self.permissao = True
    

    def eh_acc(self, entrada):
        if  entrada.upper() == 'S':
            self.acc = True

    def categoria(self, tipo):
        self.cat_hab = tipo
    
    def validade(self, data):
        self.validade = data

    def obs(self, observacao):
        self.obs = observacao

def main():
    cnh1 = Cnh('Weslley Isidorio', '34.679.566-7','375.055.588-540', '11/06/1995','Maria Madalena de Almeida Isidoro', 'A/B', 123456789, '23/07/2033', '23/02/2018', 'Teresina/PI','18/06/2023')


    print(cnh1.cat_hab)
    cnh1.categoria('C')
    print(cnh1.cat_hab)


if __name__ == '__main__':
    main()