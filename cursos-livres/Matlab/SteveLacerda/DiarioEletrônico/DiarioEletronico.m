clear all;
close all;
clc;

while true
    clc;
    fprintf('DIÁRIO ELETRÔNICO\n\n');
    fprintf(' (A) CADASTRAR DISCIPLINAS\n');
    fprintf(' (B) CADASTRAR ALUNOS\n');
    fprintf(' (C) ALTERAR NOTAS INDIVIDUAIS\n');
    fprintf(' (D) EXIBIR GRÁFICO DE NOTAS\n');
    fprintf(' (X) EXCLUIR TODOS OS CADASTROS\n');
    fprintf(' (S) SAIR\n\n');
    
    opcao = upper(input('ESCOLHA SUA OPÇÃO: ','s'));
    
    switch opcao
        case 'A'
            CadastrarDisciplina();
        case 'B'
            a = load('Disciplinas.mat');
            if(length(a.disciplinas) >= 1)
                CadastrarAluno();
            end
        case 'C'
            a = load('Alunos.mat');
            if(length(a.alunos) >= 1)
                AlterarNotaIndividual();
            end
        case 'D'
            a = load('Alunos.mat');
            if(length(a.alunos) >= 1)
                ExibirGraficoNotas();
            end
        case 'X' 
            ExcluirTodosCadastros();
        case 'S'
            break;
        otherwise
            % Como não estou dando um break não faz sentido.
            fprintf('Opção inválida!');
    end
end