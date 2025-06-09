class RedeSocial:
    def __init__(self):
        # armazena os usuários da rede social
        # cada usuário tem: conjunto de amigos e lista de posts
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        # adiciona um novo usuário se ele não existir
        if nome not in self.usuarios:
            self.usuarios[nome] = {
                'amigos': set(),   # usar set para evitar repetição
                'posts': []        # lista de posts do usuário
            }

    def adicionar_amigo(self, usuario, amigo):
        # cria amizade se ambos existirem
        if usuario in self.usuarios and amigo in self.usuarios:
            self.usuarios[usuario]['amigos'].add(amigo)
            self.usuarios[amigo]['amigos'].add(usuario)

    def publicar_mensagem(self, usuario, mensagem):
        # usuário publica um post com mensagem e lista de comentários vazia
        if usuario in self.usuarios:
            post = {'mensagem': mensagem, 'comentarios': []}
            self.usuarios[usuario]['posts'].append(post)

    def comentar_post(self, usuario, dono_post, indice_post, comentario):
        # Usuário comenta em post específico de outro usuário (ou no próprio)
        if dono_post in self.usuarios and 0 <= indice_post < len(self.usuarios[dono_post]['posts']):
            post = self.usuarios[dono_post]['posts'][indice_post]
            post['comentarios'].append({'usuario': usuario, 'comentario': comentario})

    def buscar_usuario(self, nome):
        # Retorna True se usuário existe, False caso contrário
        return nome in self.usuarios

    def mostrar_posts(self, usuario):
        # Retorna lista de posts do usuário, cada post com seus comentários
        if usuario in self.usuarios:
            return self.usuarios[usuario]['posts']
        return []


if __name__ == "__main__":
    rede = RedeSocial()
    
    # adiciona usuários
    rede.adicionar_usuario('Raphaela')
    rede.adicionar_usuario('Dorival')
    rede.adicionar_usuario('Ana Livia')

    # cria amizades
    rede.adicionar_amigo('Raphaela', 'Dorival')
    rede.adicionar_amigo('Raphaela', 'Ana Livia')

    # publica posts
    rede.publicar_mensagem('Raphaela', 'Oii, quero mais nota em PWBE!')
    rede.publicar_mensagem('Dorival', 'Bom dia pessoal!')
    
    # Comenta posts
    rede.comentar_post('Dorival', 'Raphaela', 0, 'Oi Rapha! Você vai ter mais nota')
    rede.comentar_post('Ana Livia', 'Raphaela', 0, 'Você consegue!')

    # busca usuários
    print('Existe usuário "Raphaela"?', rede.buscar_usuario('Raphaela'))
    print('Existe usuário "Thifs"?', rede.buscar_usuario('Thifs'))

    # mostra posts de Raphaela
    posts_raphaela = rede.mostrar_posts('Raphaela')
    print('\nPosts de Raphaela:')
    for i, post in enumerate(posts_raphaela):
        print(f'Post {i}: {post["mensagem"]}')
        for c in post['comentarios']:
            print(f'  Comentário de {c["usuario"]}: {c["comentario"]}')
