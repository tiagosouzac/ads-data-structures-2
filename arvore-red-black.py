class No:
    """
    Classe que representa um nó da árvore Red-Black.
    Cada nó tem uma cor (vermelho ou preto) e ponteiros para pai, filhos esquerdo e direito.
    """
    def __init__(self, valor, cor='VERMELHO'):
        self.valor = valor
        self.cor = cor  # 'VERMELHO' ou 'PRETO'
        self.pai = None
        self.esquerda = None
        self.direita = None

class ArvoreRedBlack:
    """
    Implementação de uma árvore Red-Black (Rubro-Negra).
    
    Propriedades da árvore Red-Black:
    1. Todo nó é vermelho ou preto
    2. A raiz é sempre preta
    3. Todas as folhas (NIL) são pretas
    4. Se um nó é vermelho, ambos os filhos são pretos
    5. Todo caminho de um nó até suas folhas descendentes contém o mesmo número de nós pretos
    """
    
    def __init__(self):
        # Nó NIL (sentinela) - representa folhas vazias, sempre preto
        self.NIL = No(None, 'PRETO')
        self.raiz = self.NIL
    
    def inserir(self, valor):
        """
        Insere um novo valor na árvore Red-Black.
        Primeiro insere como em uma BST normal, depois corrige as propriedades Red-Black.
        """
        # Cria um novo nó vermelho (novos nós sempre começam vermelhos)
        novo_no = No(valor, 'VERMELHO')
        novo_no.esquerda = self.NIL
        novo_no.direita = self.NIL
        
        # Encontra a posição correta para inserir (como em BST normal)
        pai = None
        atual = self.raiz
        
        while atual != self.NIL:
            pai = atual
            if novo_no.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        # Define o pai do novo nó
        novo_no.pai = pai
        
        # Se a árvore estava vazia, o novo nó se torna a raiz
        if pai is None:
            self.raiz = novo_no
        # Caso contrário, insere à esquerda ou direita do pai
        elif novo_no.valor < pai.valor:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no
        
        # Corrige as propriedades Red-Black após a inserção
        self._corrigir_insercao(novo_no)
    
    def _corrigir_insercao(self, no):
        """
        Corrige as propriedades Red-Black após uma inserção.
        O problema surge quando inserimos um nó vermelho com pai vermelho.
        """
        # Continua enquanto o pai existe e é vermelho (violação da propriedade 4)
        while no.pai and no.pai.cor == 'VERMELHO':
            # Caso 1: O pai é filho esquerdo do avô
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita  # Tio é o irmão do pai
                
                # Caso 1a: Tio é vermelho
                if tio.cor == 'VERMELHO':
                    no.pai.cor = 'PRETO'           # Pai vira preto
                    tio.cor = 'PRETO'              # Tio vira preto
                    no.pai.pai.cor = 'VERMELHO'    # Avô vira vermelho
                    no = no.pai.pai                # Continua verificando do avô
                else:
                    # Caso 1b: Tio é preto e nó é filho direito
                    if no == no.pai.direita:
                        no = no.pai
                        self._rotacao_esquerda(no)
                    
                    # Caso 1c: Tio é preto e nó é filho esquerdo
                    no.pai.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    self._rotacao_direita(no.pai.pai)
            
            # Caso 2: O pai é filho direito do avô (simétrico ao caso 1)
            else:
                tio = no.pai.pai.esquerda
                
                # Caso 2a: Tio é vermelho
                if tio.cor == 'VERMELHO':
                    no.pai.cor = 'PRETO'
                    tio.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    no = no.pai.pai
                else:
                    # Caso 2b: Tio é preto e nó é filho esquerdo
                    if no == no.pai.esquerda:
                        no = no.pai
                        self._rotacao_direita(no)
                    
                    # Caso 2c: Tio é preto e nó é filho direito
                    no.pai.cor = 'PRETO'
                    no.pai.pai.cor = 'VERMELHO'
                    self._rotacao_esquerda(no.pai.pai)
        
        # A raiz sempre deve ser preta (propriedade 2)
        self.raiz.cor = 'PRETO'
    
    def _rotacao_esquerda(self, no):
        """
        Realiza uma rotação à esquerda no nó especificado.
        
        Antes:     x              Depois:      y
                  / \                         / \
                 a   y            =>         x   c
                    / \                     / \
                   b   c                   a   b
        """
        y = no.direita              # y é o filho direito de x
        no.direita = y.esquerda     # Subárvore b vira filho direito de x
        
        if y.esquerda != self.NIL:
            y.esquerda.pai = no     # Atualiza o pai de b
        
        y.pai = no.pai              # y assume a posição de x
        
        if no.pai is None:
            self.raiz = y           # Se x era raiz, y vira raiz
        elif no == no.pai.esquerda:
            no.pai.esquerda = y     # Se x era filho esquerdo, y vira filho esquerdo
        else:
            no.pai.direita = y      # Se x era filho direito, y vira filho direito
        
        y.esquerda = no             # x vira filho esquerdo de y
        no.pai = y                  # Atualiza o pai de x
    
    def _rotacao_direita(self, no):
        """
        Realiza uma rotação à direita no nó especificado.
        
        Antes:       y            Depois:    x
                    / \                     / \
                   x   c          =>       a   y
                  / \                         / \
                 a   b                       b   c
        """
        x = no.esquerda             # x é o filho esquerdo de y
        no.esquerda = x.direita     # Subárvore b vira filho esquerdo de y
        
        if x.direita != self.NIL:
            x.direita.pai = no      # Atualiza o pai de b
        
        x.pai = no.pai              # x assume a posição de y
        
        if no.pai is None:
            self.raiz = x           # Se y era raiz, x vira raiz
        elif no == no.pai.direita:
            no.pai.direita = x      # Se y era filho direito, x vira filho direito
        else:
            no.pai.esquerda = x     # Se y era filho esquerdo, x vira filho esquerdo
        
        x.direita = no              # y vira filho direito de x
        no.pai = x                  # Atualiza o pai de y
    
    def buscar(self, valor):
        """
        Busca um valor na árvore Red-Black.
        Funciona igual a uma BST normal, já que a ordenação é mantida.
        """
        atual = self.raiz
        while atual != self.NIL:
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None
    
    def percorrer_em_ordem(self, no=None):
        """
        Percorre a árvore em ordem (esquerda, raiz, direita).
        Retorna uma lista com os valores em ordem crescente.
        """
        if no is None:
            no = self.raiz
        
        resultado = []
        if no != self.NIL:
            resultado.extend(self.percorrer_em_ordem(no.esquerda))
            resultado.append((no.valor, no.cor))
            resultado.extend(self.percorrer_em_ordem(no.direita))
        
        return resultado
    
    def imprimir_arvore(self, no=None, nivel=0, prefixo="Raiz: "):
        """
        Imprime a árvore de forma visual para facilitar a compreensão.
        """
        if no is None:
            no = self.raiz
        
        if no != self.NIL:
            print(" " * (nivel * 4) + prefixo + f"{no.valor}({no.cor})")
            if no.esquerda != self.NIL or no.direita != self.NIL:
                self.imprimir_arvore(no.esquerda, nivel + 1, "L--- ")
                self.imprimir_arvore(no.direita, nivel + 1, "R--- ")

# Exemplo de uso
if __name__ == "__main__":
    # Cria uma nova árvore Red-Black
    arvore = ArvoreRedBlack()
    
    # Insere alguns valores
    valores = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 20]
    print("Inserindo valores:", valores)
    
    for valor in valores:
        arvore.inserir(valor)
        print(f"Inserido: {valor}")
    
    print("\nÁrvore Red-Black resultante:")
    arvore.imprimir_arvore()
    
    print("\nPercurso em ordem (valor, cor):")
    print(arvore.percorrer_em_ordem())
    
    # Testa busca
    print("\nTestes de busca:")
    for valor in [5, 15, 25]:
        resultado = arvore.buscar(valor)
        if resultado:
            print(f"Valor {valor} encontrado: {resultado.valor}({resultado.cor})")
        else:
            print(f"Valor {valor} não encontrado")