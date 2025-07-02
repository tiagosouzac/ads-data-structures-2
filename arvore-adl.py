class NoAVL:
    """
    Classe que representa um nó da árvore AVL.
    Cada nó contém um valor, referências para os filhos esquerdo e direito,
    e a altura do nó para facilitar o cálculo do fator de balanceamento.
    """
    def __init__(self, valor):
        self.valor = valor          # Valor armazenado no nó
        self.esquerdo = None        # Referência para o filho esquerdo
        self.direito = None         # Referência para o filho direito
        self.altura = 1             # Altura do nó (folhas têm altura 1)


class ArvoreAVL:
    """
    Implementação de uma Árvore AVL (Adelson-Velsky e Landis).
    
    Uma árvore AVL é uma árvore binária de busca auto-balanceada onde
    a diferença entre as alturas das subárvores esquerda e direita
    de qualquer nó é no máximo 1.
    
    Isso garante que as operações de busca, inserção e remoção
    tenham complexidade O(log n) no pior caso.
    """
    
    def __init__(self):
        self.raiz = None
    
    def obter_altura(self, no):
        """
        Retorna a altura de um nó.
        Se o nó for None (inexistente), retorna 0.
        """
        if not no:
            return 0
        return no.altura
    
    def obter_fator_balanceamento(self, no):
        """
        Calcula o fator de balanceamento de um nó.
        
        Fator de balanceamento = altura da subárvore esquerda - altura da subárvore direita
        
        Se o fator for:
        - 0: árvore balanceada
        - 1 ou -1: árvore aceitavelmente balanceada
        - > 1: subárvore esquerda muito alta (rotação à direita necessária)
        - < -1: subárvore direita muito alta (rotação à esquerda necessária)
        """
        if not no:
            return 0
        return self.obter_altura(no.esquerdo) - self.obter_altura(no.direito)
    
    def atualizar_altura(self, no):
        """
        Atualiza a altura de um nó baseada nas alturas de seus filhos.
        A altura de um nó é 1 + a maior altura entre seus filhos.
        """
        if no:
            no.altura = 1 + max(self.obter_altura(no.esquerdo), 
                               self.obter_altura(no.direito))
    
    def rotacao_direita(self, y):
        """
        Realiza uma rotação simples à direita.
        
        Usada quando a subárvore esquerda está muito alta.
        
        Antes:     y              Depois:    x
                  / \\                       / \\
                 x   T3                    T1  y
                / \\                           / \\
               T1  T2                        T2  T3
        """
        # Salva o filho esquerdo de y
        x = y.esquerdo
        
        # Salva a subárvore direita de x
        T2 = x.direito
        
        # Realiza a rotação
        x.direito = y
        y.esquerdo = T2
        
        # Atualiza as alturas (importante: y primeiro, depois x)
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        
        # Retorna a nova raiz desta subárvore
        return x
    
    def rotacao_esquerda(self, x):
        """
        Realiza uma rotação simples à esquerda.
        
        Usada quando a subárvore direita está muito alta.
        
        Antes:    x               Depois:     y
                 / \\                         / \\
                T1  y                       x   T3
                   / \\                     / \\
                  T2  T3                  T1  T2
        """
        # Salva o filho direito de x
        y = x.direito
        
        # Salva a subárvore esquerda de y
        T2 = y.esquerdo
        
        # Realiza a rotação
        y.esquerdo = x
        x.direito = T2
        
        # Atualiza as alturas (importante: x primeiro, depois y)
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        
        # Retorna a nova raiz desta subárvore
        return y
    
    def inserir(self, valor):
        """
        Insere um valor na árvore AVL mantendo o balanceamento.
        """
        self.raiz = self._inserir_recursivo(self.raiz, valor)
    
    def _inserir_recursivo(self, no, valor):
        """
        Função auxiliar recursiva para inserção.
        
        Passos:
        1. Inserção normal como em BST
        2. Atualizar altura do nó atual
        3. Calcular fator de balanceamento
        4. Aplicar rotações se necessário
        """
        
        # Passo 1: Inserção normal de BST
        if not no:
            return NoAVL(valor)
        
        if valor < no.valor:
            no.esquerdo = self._inserir_recursivo(no.esquerdo, valor)
        elif valor > no.valor:
            no.direito = self._inserir_recursivo(no.direito, valor)
        else:
            # Valores duplicados não são permitidos
            return no
        
        # Passo 2: Atualizar altura do nó atual
        self.atualizar_altura(no)
        
        # Passo 3: Obter o fator de balanceamento
        fator_balanceamento = self.obter_fator_balanceamento(no)
        
        # Passo 4: Se o nó está desbalanceado, há 4 casos possíveis
        
        # Caso 1: Rotação simples à direita (Left-Left case)
        if fator_balanceamento > 1 and valor < no.esquerdo.valor:
            return self.rotacao_direita(no)
        
        # Caso 2: Rotação simples à esquerda (Right-Right case)
        if fator_balanceamento < -1 and valor > no.direito.valor:
            return self.rotacao_esquerda(no)
        
        # Caso 3: Rotação dupla esquerda-direita (Left-Right case)
        if fator_balanceamento > 1 and valor > no.esquerdo.valor:
            no.esquerdo = self.rotacao_esquerda(no.esquerdo)
            return self.rotacao_direita(no)
        
        # Caso 4: Rotação dupla direita-esquerda (Right-Left case)
        if fator_balanceamento < -1 and valor < no.direito.valor:
            no.direito = self.rotacao_direita(no.direito)
            return self.rotacao_esquerda(no)
        
        # Retorna o nó (inalterado se já estava balanceado)
        return no
    
    def remover(self, valor):
        """
        Remove um valor da árvore AVL mantendo o balanceamento.
        """
        self.raiz = self._remover_recursivo(self.raiz, valor)
    
    def _remover_recursivo(self, no, valor):
        """
        Função auxiliar recursiva para remoção.
        
        Similar à inserção, mas com lógica de remoção de BST primeiro.
        """
        
        # Passo 1: Remoção normal de BST
        if not no:
            return no
        
        if valor < no.valor:
            no.esquerdo = self._remover_recursivo(no.esquerdo, valor)
        elif valor > no.valor:
            no.direito = self._remover_recursivo(no.direito, valor)
        else:
            # Este é o nó a ser removido
            
            # Nó com apenas um filho ou nenhum filho
            if not no.esquerdo:
                return no.direito
            elif not no.direito:
                return no.esquerdo
            
            # Nó com dois filhos: obter o sucessor inorder
            # (menor valor na subárvore direita)
            temp = self._obter_menor_valor(no.direito)
            
            # Copiar o valor do sucessor inorder para este nó
            no.valor = temp.valor
            
            # Remover o sucessor inorder
            no.direito = self._remover_recursivo(no.direito, temp.valor)
        
        # Se a árvore tinha apenas um nó, retorna
        if not no:
            return no
        
        # Passo 2: Atualizar altura do nó atual
        self.atualizar_altura(no)
        
        # Passo 3: Obter o fator de balanceamento
        fator_balanceamento = self.obter_fator_balanceamento(no)
        
        # Passo 4: Se o nó está desbalanceado, há 4 casos possíveis
        
        # Caso 1: Rotação simples à direita (Left-Left case)
        if fator_balanceamento > 1 and self.obter_fator_balanceamento(no.esquerdo) >= 0:
            return self.rotacao_direita(no)
        
        # Caso 2: Rotação simples à esquerda (Right-Right case)
        if fator_balanceamento < -1 and self.obter_fator_balanceamento(no.direito) <= 0:
            return self.rotacao_esquerda(no)
        
        # Caso 3: Rotação dupla esquerda-direita (Left-Right case)
        if fator_balanceamento > 1 and self.obter_fator_balanceamento(no.esquerdo) < 0:
            no.esquerdo = self.rotacao_esquerda(no.esquerdo)
            return self.rotacao_direita(no)
        
        # Caso 4: Rotação dupla direita-esquerda (Right-Left case)
        if fator_balanceamento < -1 and self.obter_fator_balanceamento(no.direito) > 0:
            no.direito = self.rotacao_direita(no.direito)
            return self.rotacao_esquerda(no)
        
        # Retorna o nó (inalterado se já estava balanceado)
        return no
    
    def _obter_menor_valor(self, no):
        """
        Encontra o nó com o menor valor na subárvore.
        Usado para encontrar o sucessor inorder na remoção.
        """
        atual = no
        while atual.esquerdo:
            atual = atual.esquerdo
        return atual
    
    def buscar(self, valor):
        """
        Busca um valor na árvore.
        Retorna True se encontrado, False caso contrário.
        """
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, no, valor):
        """
        Função auxiliar recursiva para busca.
        """
        if not no or no.valor == valor:
            return no is not None
        
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerdo, valor)
        else:
            return self._buscar_recursivo(no.direito, valor)
    
    def percorrer_inorder(self):
        """
        Percorre a árvore em ordem (esquerda, raiz, direita).
        Retorna uma lista com os valores em ordem crescente.
        """
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorder_recursivo(self, no, resultado):
        """
        Função auxiliar recursiva para percurso inorder.
        """
        if no:
            self._inorder_recursivo(no.esquerdo, resultado)
            resultado.append(no.valor)
            self._inorder_recursivo(no.direito, resultado)
    
    def percorrer_preorder(self):
        """
        Percorre a árvore em pré-ordem (raiz, esquerda, direita).
        """
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorder_recursivo(self, no, resultado):
        """
        Função auxiliar recursiva para percurso preorder.
        """
        if no:
            resultado.append(no.valor)
            self._preorder_recursivo(no.esquerdo, resultado)
            self._preorder_recursivo(no.direito, resultado)
    
    def percorrer_postorder(self):
        """
        Percorre a árvore em pós-ordem (esquerda, direita, raiz).
        """
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorder_recursivo(self, no, resultado):
        """
        Função auxiliar recursiva para percurso postorder.
        """
        if no:
            self._postorder_recursivo(no.esquerdo, resultado)
            self._postorder_recursivo(no.direito, resultado)
            resultado.append(no.valor)
    
    def imprimir_arvore(self):
        """
        Imprime a estrutura da árvore de forma visual.
        """
        if not self.raiz:
            print("Árvore vazia")
            return
        
        print("Estrutura da árvore AVL:")
        self._imprimir_recursivo(self.raiz, "", True)
    
    def _imprimir_recursivo(self, no, prefixo, eh_ultimo):
        """
        Função auxiliar recursiva para impressão visual da árvore.
        """
        if no:
            print(f"{prefixo}{'└── ' if eh_ultimo else '├── '}{no.valor} (h:{no.altura}, fb:{self.obter_fator_balanceamento(no)})")
            
            # Conta quantos filhos existem
            filhos = []
            if no.esquerdo:
                filhos.append(('esq', no.esquerdo))
            if no.direito:
                filhos.append(('dir', no.direito))
            
            # Imprime os filhos
            for i, (tipo, filho) in enumerate(filhos):
                eh_ultimo_filho = (i == len(filhos) - 1)
                novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
                self._imprimir_recursivo(filho, novo_prefixo, eh_ultimo_filho)


def exemplo_uso():
    """
    Função de demonstração do uso da árvore AVL.
    """
    print("=== Demonstração da Árvore AVL ===\n")
    
    # Criando uma nova árvore AVL
    arvore = ArvoreAVL()
    
    # Inserindo alguns valores
    valores = [10, 20, 30, 40, 50, 25]
    print("Inserindo valores:", valores)
    
    for valor in valores:
        print(f"\nInserindo {valor}...")
        arvore.inserir(valor)
        arvore.imprimir_arvore()
        print()
    
    # Testando percursos
    print("\n=== Percursos da Árvore ===")
    print("Inorder (crescente):", arvore.percorrer_inorder())
    print("Preorder:", arvore.percorrer_preorder())
    print("Postorder:", arvore.percorrer_postorder())
    
    # Testando busca
    print("\n=== Testes de Busca ===")
    valores_busca = [25, 15, 50]
    for valor in valores_busca:
        encontrado = arvore.buscar(valor)
        print(f"Buscar {valor}: {'Encontrado' if encontrado else 'Não encontrado'}")
    
    # Testando remoção
    print("\n=== Testes de Remoção ===")
    valores_remover = [30, 20]
    for valor in valores_remover:
        print(f"\nRemovendo {valor}...")
        arvore.remover(valor)
        arvore.imprimir_arvore()
        print("Inorder após remoção:", arvore.percorrer_inorder())


if __name__ == "__main__":
    exemplo_uso()