function AlterarNotaIndividual()   
    while true
        clc; 
        a = load('Alunos.mat');        
        alunos = a.alunos;
        notas = a.notas;
        
        m = load('Disciplinas.mat');
        materias = m.disciplinas;
        qtded = length(materias);
      
        %x = size(a.alunos);
        x = length(a.alunos);

        fprintf('LISTA DE ALUNOS\n');
        fprintf('---------------------------------------------------------------------\n');        
        controle = 1;
        for i=1:x
            fprintf('Código %2d: %-25s (%-15s -> Nota: %5.2f\n',i,alunos(i), materias(controle), notas(i));
            if(controle < qtded)
                controle = controle + 1;                
            else
                controle = 1;
            end            
        end
        fprintf('---------------------------------------------------------------------\n');
        %aluno = upper(input('Alterar a nota do Aluno (0: sair): ','s'));
        codaluno = int32(input('Entre com o código da linha para alterar a nota (0: sair): '));
        %busca = strfind(alunos, aluno);
        if (codaluno == 0)
            break;
        else            
            if(codaluno > x || codaluno < 0)
                fprintf('Código inválido! ');
                %input('Pressione <Enter>');
            else
                nota = input('Entre com a nota: ');
                notas(codaluno) = nota;
            end
        end
        save('Alunos.mat', 'alunos', 'notas');
    end    
end