function CadastrarAluno()
    alunos = [""];
    notas = [0.0];
    materias = [""];
    
    a = load('Disciplinas.mat');
    materias = a.disciplinas;
    
    while true
        clc;
        prompt = 'Entre com o nome do aluno (0: sair): ';
        nome = upper(input(prompt,'s'));        
        
        if (nome == "0")
            break;
        else
            for i=1:length(materias)
                fprintf('Entre com a nota de %s \n',materias(i));
                nota = input('Nota: ');
                if (alunos(1) == "")
                    alunos(1) = nome;
                    notas(1) = nota;
                else
                    alunos(end+1) = nome;
                    notas(end+1) = nota;
                end           
            end        
        end
    end
    save('Alunos','alunos', 'notas');
    %save('Notas','notas');
end