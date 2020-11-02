function CadastrarDisciplina()
    %clear all;
    %close all;
    %clc;
    disciplinas = [""];
    while true
        clc;
        prompt = 'Entre com a disciplina (0: sair): ';
        str = upper(input(prompt,'s'));
        if (str == "0")
            break;
        else
            if (disciplinas(1) == "")
                disciplinas(1) = str;
            else
                disciplinas(end+1) = str;
            end
        end
    end
    save('Disciplinas','disciplinas');
end