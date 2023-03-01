# -----------------------------------------------------
# Acesse o menu de ajuda executando o comando python help.py help no terminal (apontando para a pasta do script).
# Escolha a opção de comando (orientacoes, diretorio, imagem ou banda) e execute python help.py help [COMANDO] no terminal.
# Ex: python help.py help orientacoes
# -----------------------------------------------------

import click

# creating group
@click.group()
def cli():
    pass

# creating subgroup for help
@cli.group()
def help():
  pass

# commands
@click.command()
def orientacoes():
    print('Ajuda sobre o topico orientacoes gerais.')

@click.command()
def diretorio():
    print('Ajuda sobre o topico diretorio.')

@click.command()
def imagem():
    print('Ajuda sobre o topico imagem.')

@click.command()
def bandas():
    print('Ajuda sobre o topico bandas')

help.add_command(orientacoes)
help.add_command(diretorio)
help.add_command(imagem)
help.add_command(bandas)

if __name__ == "__main__":
    cli()