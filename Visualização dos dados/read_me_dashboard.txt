Instruções de uso e visualização do dashboard "Relatório Passos Mágicos 2020-2022"
------------------------------------------------------------------------------------
Olá, para facilitar a visualização e entendimento do dashboard criado em power BI, sem poder publicá-lo online
foi escrito este arquivo com algumas orientações básicas para auxiliar na consulta.

* As bases utilizadas para a construção desse dashboard foram os seguintes arquivos:
	- db_2020.csv;
	- db_2021.csv;
	- db_2022.csv;
	- tbAluno.csv;
	- alnos_merged.csv;

* Todas essas bases foram criadas a partir dos notebooks apresentados no relatório completo do trabalho e anexados;

* Caso queiram atualizar alguma das visualizações ou trazer uma base nova, pode-se substituir os arquivos e caminhos
dentro da query do Power BI;

* Para a elaboração deste dashboard foram utilizados os dados de 2020-2022, incialmente fornecidos pela FIAP. Devido
ao progresso do trabalho na data em que a nova base foi enviada, o grupo optou por seguirmos com a base que já estávamos
utilizando e concluir o trabalho desta forma;

* O dashboard é dividido essencialmente em 3 seguimentos, sendo eles:
	- Uma visão geral da quantidade de alunos e sua distribuição entre as categorias "Pedras" por ano;
	- Uma visão da evasão, tendo acesso à evasão por raça, genero, idade, fase e um detalhamento da quantia
	de alunos que saiu ou continuou no período;
	- Uma visão da variação de notas/índices por ano e por fase;

* Nas telas de "Índices_Fase" há botões de navegação ao lado do gráfico das notas por ano, porém para facilitar a
navegação do avaliador numa versão não publicada, individualizamos as visualizações de forma a poder ou não usar
os botões para se deslocar entre as páginas (A mesma lógica se aplica às telas de evasão);

* As bases foram todas geradas a partir dos scripts em python, com mínimas tratativas dentro da query deste BI
para melhor visualização;

* Por não possuirmos uma conta corporativa em que pudéssemos importar um visual, o pareto foi construído com
base em medidas para um maior dinamismo do dashboard;

* Apesar de os códigos utilizados dentro do BI não serem o foco do projeto, permanecemos à disposição para
quaisquer dúvidas ou sugestões;