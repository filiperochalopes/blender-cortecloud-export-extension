# Plano de corte com Blender

Após procurar minhas opções de criar um projeto em MDF notei que a maioria dos programas que são verdadeiramente úteis são pagos. Como sou hobbysta e queria fazer os móveis de minha casa, a começar pela montagem de [minha cama de parede](https://www.orangebed.com.br/pt-br). Em contato com a equipe [GMAD](https://www.gmad.com.br/gmad-feiradesantana) fui orientado no uso do [CorteCloud](https://cortecloud.com.br/) que tem suas especificações no uso de importação de arquivos de planilha para planos de corte, esse script visa se adequar às conformidades do CorteCloud utilizando um programa consagrado e OpenSource para desenvolvimento 3D, [Blender](https://www.blender.org/).

# Como usar

1. Abra o Blender, de preferência pelo terminal se quiser debugar o script e carregue o script na aba de `Editor`
2. Crie os objetos seguindo o padrão de medida em metros
3. Dê um nome à peça, esse nome deve ser a função que a peça ocupa no projeto, por exemplo: "Lateral da Caixa", peças duplicadas terão suaquantidade incrementada, por exemplo: "Lateral da Caixa" e "Lateral da Caixa.001" se tornará 2 x "Lateral da Caixa"
4. Altere no script `output_file` para o seu arquivo de saída desejado
5. Selecione os objetos que quer exportar
6. Rode o script
7. Faça o upload do arquivo no CorteCloud

# Roadmap

Transformar esse script em um plugin com seleção de pasta e arquivo csv que deve ser gerado, facilitando o flow.